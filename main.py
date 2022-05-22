from os import remove, path
from argparse import ArgumentParser
from datetime import datetime, timedelta
from json import dumps

from flask import Flask, request
from dateutil.parser import isoparse
from peewee import *

from modules import config, model

# Set up the reset flag
parser = ArgumentParser("An API for therapy appointments")
parser.add_argument("-r", "--reset", help="Reset DB before starting", action='store_true')
args = parser.parse_args()

if args.reset and path.exists(config.DB_PATH):
    remove(config.DB_PATH)

# Initialise the model, connects to the DB, creates tables if needed and populates test data if required
model.init(test=config.TEST)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    '''
    Render home route

    - currently unimplemented
    '''
    return ""

# Retrieve appointments
@app.route('/api/get/appointments', methods=['GET'])
def get_appointments():
    '''
    Retrieve availiable appointments. 
    
    Optional parameters:
    - fromdate: ISO 8601 formatted date string indicating the earliest date to include in the results. Defaults to the current date.  
        - Example: 2022-05-25
    - todate: ISO 8601 formatted date string indicating the latest date to include in the results. Defaults to fromdate plus two weeks.
        - Example: 2022-05-29
    - type: String indicating the type of appointment to search for. Possible values are: one-off and consultation.
        - Example: consultation
    - specialisms: Comma-delimited list of specialisms to search for. results will include appointments that match any of the given specialisms. Current specialisms are: ADHD, Anxiety, Depression, Trauma and Stress.
        - Example: Anxiety,Trauma,Stress

    Returns:
    - JSON list of appointments
    '''
    from_date_str = request.args.get('fromdate')
    to_date_str = request.args.get('todate')
    type = request.args.get('type')
    specialisms = request.args.get('specialisms')

    if specialisms: 
        specialisms = specialisms.split(',')
    else:
        specialisms = []

    if from_date_str:
        from_date = isoparse(from_date_str)
    else:
        from_date = datetime.now()
    
    #SQlite between doesn't include the higher end so add one day to compensate 
    if to_date_str:
        to_date = isoparse(to_date_str) + timedelta(days=1)
    else:
        to_date = from_date + timedelta(weeks=2, days=1)
    
    results = model.get_appointments(from_date, to_date, type, specialisms)        
    print(results)
    return dumps(results)

app.run()