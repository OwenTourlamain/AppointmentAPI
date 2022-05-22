# ApointmentAPI

This Flask app provides an API to search for availiable appointments that fit certain criterea.

## Endpoints

Currently the app provides a single endpoint `/api/get/appointments`,
which accepts the following optional paramenters:
- `fromdate`: ISO 8601 formatted date string indicating the earliest date to include in the results. Defaults to the current date.  
    - Example: `?fromdate=2022-05-25`
- `todate`: ISO 8601 formatted date string indicating the latest date to include in the results. Defaults to `fromdate` plus two weeks.
    - Example: `?todate=2022-05-29`
- `type`: String indicating the type of appointment to search for. Possible values are: `one-off` and `consultation`.
    - Example: `?type=consultation`
- `specialisms`: Comma-delimited list of specialisms to search for. results will include appointments that match any of the given specialisms. Current specialisms are: `ADHD`, `Anxiety`, `Depression`, `Trauma` and `Stress`.
    - Example: `?specialisms=Anxiety,Trauma,Stress`

The example query: http://localhost:5000/api/get/appointments?fromdate=2022-05-25&todate=2022-05-29&type=consultation&specialisms=Anxiety,Trauma,Stress gives the following results:
```
[
    {
        "therapist": "Donnell Johnson", 
        "date": "2022-05-26", 
        "time": "15:30",
        "duration": 90,
        "type:": "consultation"
    },
    {
        "therapist": "Donnell Johnson",
        "date": "2022-05-26",
        "time": "17:30",
        "duration": 90,
        "type:": "consultation"
    },
    {
        "therapist": "Rosanna Sadler",
        "date": "2022-05-26",
        "time": "10:30",
        "duration": 30,
        "type:": "consultation"
    },
    {
        "therapist": "Rosanna Sadler",
        "date": "2022-05-27",
        "time": "10:30",
        "duration": 30,
        "type:": "consultation"
    }
]
```

## Set Up

This appliction requires a Python 3 installation, it has been tested working with Python 3.7.3.

To install dependancies run `pip install -r requirements.txt` (Note: depending on your Python installation you may need to run `pip3` instead).

## Testing

To run the test suite, run `pytest` in the root of the repository. 

## Running

To launch the application, run `python main.py`.

The application accepts one optional flag, `-r`, which wipes the database before launching. This is to aid development and has no practical effect yet as there is no way to modify the data through the application.

Once launched, the api will be availiable at: http://localhost:5000/