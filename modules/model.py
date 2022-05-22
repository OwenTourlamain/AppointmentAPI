from dateutil.parser import isoparse

from peewee import *

from . import test_data, config

db = SqliteDatabase(config.DB_PATH)
    
def init(test):
    '''
    Initialises database connection and makes sure tables are created.

    Parameters:
    - test: indicates test mode which loads test data into the database if it was empty.
    '''
    if db.get_tables() != ['appointment', 'client', 'specialism', 'therapist', 'therapistspecialism']:
        db.create_tables([Client, Specialism, Therapist, TherapistSpecialism, Appointment])
        if test:
            populate_test_data()    

def populate_test_data():
    '''
    Reads the test data file and loads it into the database.
    '''
    with db.atomic(): # Tells Peewee to use one transaction for all of these commands
        for name in test_data.CLIENTS:
            client = Client.create(name=name)

        for name in test_data.SPECIALISMS:
            specialism = Specialism.create(name=name)

        for name, specialisms in test_data.THERAPISTS:
            therapist = Therapist.create(name=name)
            for name in specialisms:
                specialism = Specialism.get(Specialism.name == name)
                therapist_specialism = TherapistSpecialism.create(therapist=therapist, specialism=specialism)

        for date_str, availiable, duration, type, client_name, therapist_name in test_data.APPOINTMENTS:
            date_time = isoparse(date_str)
            if client_name: 
                client = Client.get(Client.name == client_name)
            therapist = Therapist.get(Therapist.name == therapist_name)
            appointment = Appointment.create(date_time=date_time, availiable=availiable, duration=duration, type=type, client=client, therapist=therapist)

def get_appointments(from_date, to_date, type, specialisms):
    '''
    Retrieve availiable appointments. 
    
    Optional parameters:
    - from_date: Datetime object indicating the earliest date to include in the results.  
    - to_date: Datetime object indicating the latest date to include in the results.
    - type: String indicating the type of appointment to search for. Possible values are: one-off and consultation.
    - specialisms: List of specialisms to search for. results will include appointments that match any of the given specialisms. Current specialisms are: ADHD, Anxiety, Depression, Trauma and Stress.

    Returns:
    - List of availiable appointments
    '''
    query = (
        Appointment
        .select(Therapist, Appointment.date_time, Appointment.type, Appointment.duration)
        .join(Therapist)
        .where(Appointment.availiable == True)
        .where(Appointment.date_time.between(from_date, to_date))
    )

    if type in ["one-off", "consultation"]:
        query = query.where(Appointment.type == type)

    query_list = []
    for appointment in query:

        # Filtering by specialism should be done in the queery, but Peewee 
        # requires an instantiated object for many-to-many relationships
        spec_list = [] 
        for spec in appointment.therapist.specialisms:
            spec_list.append(spec.specialism.name)

        # Only filter by specialisms if we were given any
        if not specialisms or any(specialism in specialisms for specialism in spec_list):
            appointment_dict = {
                "therapist": appointment.therapist.name,
                "date": appointment.date_time.strftime("%Y-%m-%d"),
                "time": appointment.date_time.strftime("%H:%M"),
                "duration": appointment.duration,
                "type:": appointment.type
            }
            query_list.append(appointment_dict)

    return list(query_list)

class BaseModel(Model):
    '''
    Base class to set up the database connetcion for all model classes
    '''
    class Meta:
        database = db

class Client(BaseModel):
    name = CharField()

class Specialism(BaseModel):
    name = CharField()

class Therapist(BaseModel):
    name = CharField()

class TherapistSpecialism(BaseModel):
    therapist = ForeignKeyField(Therapist, backref='specialisms')
    specialism = ForeignKeyField(Specialism, backref='therapists')

class Appointment(BaseModel):
    date_time = DateTimeField()
    availiable = BooleanField()
    duration = IntegerField()
    type = CharField()
    client = ForeignKeyField(Client, backref='appointments', null=True)
    therapist = ForeignKeyField(Therapist, backref='appointments')