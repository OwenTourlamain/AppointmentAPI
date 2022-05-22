from dateutil.parser import isoparse

from ..modules import model

model.init(test=True)

def test_get_appointments():
    from_date = isoparse("2022-05-26")
    to_date = isoparse("2022-05-27")
    type = "one-off"
    specialisms = ["ADHD"]
    results = model.get_appointments(from_date, to_date, type, specialisms)
    assert results == [{'therapist': 'Andy Conroy', 'date': '2022-05-26', 'time': '17:30', 'duration': 60, 'type:': 'one-off'}]