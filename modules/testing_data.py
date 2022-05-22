from datetime import time

CLIENTS = (
    "John Doe",
    "Rico Mullen",
    "Cosmo Fraser"
)

SPECIALISMS = (
    "ADHD",
    "Anxiety",
    "Depression",
    "Trauma",
    "Stress"
)

THERAPISTS = (
    ("Chris Stokes", ["Depression"]),
    ("Andy Conroy", ["ADHD"]),
    ("Donnell Johnson", ["Anxiety"]),
    ("Rosanna Sadler", ["ADHD", "Trauma"]),
    ("Sumaya Fellows", ["Depression", "Stress"])
)

APPOINTMENTS = (
    ("2022-05-23T17:30:00", True, "60", "one-off", None, "Andy Conroy"),
    ("2022-05-24T17:30:00", True, "60", "one-off", None, "Andy Conroy"),
    ("2022-05-25T17:30:00", False, "60", "one-off", "Rico Mullen", "Andy Conroy"),
    ("2022-05-26T17:30:00", True, "60", "one-off", None, "Andy Conroy"),
    ("2022-05-23T13:30:00", True, "90", "one-off", None, "Donnell Johnson"),
    ("2022-05-23T15:30:00", True, "90", "consultation", None, "Donnell Johnson"),
    ("2022-05-23T17:30:00", True, "90", "consultation", None, "Donnell Johnson"),
    ("2022-05-26T13:30:00", True, "90", "one-off", None, "Donnell Johnson"),
    ("2022-05-26T15:30:00", True, "90", "consultation", None, "Donnell Johnson"),
    ("2022-05-26T17:30:00", True, "90", "consultation", None, "Donnell Johnson"),
    ("2022-05-29T13:30:00", True, "90", "one-off", None, "Donnell Johnson"),
    ("2022-05-29T15:30:00", True, "90", "consultation", None, "Donnell Johnson"),
    ("2022-05-29T10:30:00", True, "90", "consultation", None, "Donnell Johnson"),
    ("2022-05-23T10:30:00", True, "30", "consultation", None, "Rosanna Sadler"),
    ("2022-05-24T10:30:00", True, "30", "consultation", None, "Rosanna Sadler"),
    ("2022-05-25T10:30:00", False, "30", "consultation", "Cosmo Fraser", "Rosanna Sadler"),
    ("2022-05-26T10:30:00", True, "30", "consultation", None, "Rosanna Sadler"),
    ("2022-05-27T10:30:00", True, "30", "consultation", None, "Rosanna Sadler"),
    ("2022-05-23T12:30:00", True, "30", "one-off", None, "Rosanna Sadler"),
    ("2022-05-24T12:30:00", True, "30", "one-off", None, "Rosanna Sadler"),
    ("2022-05-25T12:30:00", True, "30", "one-off", "Cosmo Fraser", "Rosanna Sadler"),
    ("2022-05-26T12:30:00", False, "30", "one-off", None, "Rosanna Sadler"),
    ("2022-05-27T12:30:00", True, "30", "one-off", None, "Rosanna Sadler"),
    ("2022-05-23T09:15:00", True, "45", "one-off", None, "Sumaya Fellows"),
    ("2022-05-23T09:15:00", True, "45", "one-off", None, "Sumaya Fellows"),
    ("2022-05-23T09:15:00", True, "45", "one-off", None, "Sumaya Fellows"),
    ("2022-05-23T09:15:00", True, "45", "one-off", None, "Sumaya Fellows"),
    ("2022-05-23T09:15:00", True, "45", "one-off", None, "Sumaya Fellows"),
    ("2022-05-23T13:00:00", True, "60", "consultation", None, "Sumaya Fellows"),
    ("2022-05-23T13:00:00", True, "60", "consultation", None, "Sumaya Fellows"),
    ("2022-05-23T13:00:00", True, "60", "consultation", None, "Sumaya Fellows"),
    ("2022-05-23T13:00:00", True, "60", "consultation", None, "Sumaya Fellows"),
    ("2022-05-23T13:00:00", True, "60", "consultation", None, "Sumaya Fellows"),
)
