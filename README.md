### How to run

1. `docker-compose up -d`
2. Test request `GET http://localhost:5000/api/patient/625233`
3. Test response 
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