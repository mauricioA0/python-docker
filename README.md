### How to run

1. `source venv/bin/activate`
2. `python3 migrate.py db init`
3. `python3 migrate.py db migrate`
5. `python3 migrate.py db upgrade`
6. `python3 run.py`
7. Test request `GET http://localhost:5000/api/patient/625233`
8. Test response 
``
{
    "code": 200,
    "data": {
        "name": "Jonas",
        "patient_id": 625233,
        "address": "Seattle, US",
        "last_name": "Kanhwald"
    }
}
``