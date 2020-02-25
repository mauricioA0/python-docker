import os
import requests
from flask import request
from flask_restful import Resource

from app import db

from decorators import abort_if_not_exist
from models import PatientsModel
from schemas import PatientSchema

API_ROOT = os.getenv("API_ROOT")

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)


def save_patient(response):
    patient_temp = {}

    req = response.json()

    patient_temp["patient_id"] = req["id"]
    patient_temp["name"] = req["name"][0]["given"][0]
    patient_temp["last_name"] = req["name"][0]["family"]

    if "address" in req:
        city = req["address"][0]["city"]
        state_or_country = req["address"][0].get("country", req["address"][0].get("state", None))
        patient_temp["address"] = "{}, {}".format(city, state_or_country)
    else:
        patient_temp["address"] = None

    patient = PatientsModel(
        patient_id=patient_temp["patient_id"],
        name=patient_temp["name"],
        last_name=patient_temp["last_name"],
        address=patient_temp["address"]
    )

    db.session.add(patient)
    db.session.commit()

    return patient_temp


class PatientByIdResource(Resource):
    decorators = [abort_if_not_exist(entity="Patient")]

    @classmethod
    def get(cls, patient_id):

        patient_query = PatientsModel.query.filter_by(patient_id=patient_id).first()

        patient = None

        if patient_query is not None and isinstance(patient_query, PatientsModel):
            patient = patient_schema.dump(patient_query)

            return {"code": 200, "data": patient}, 200

        request_patient = requests.get("{}/Patient/{}?_format=json".format(API_ROOT, patient_id))

        if request_patient.status_code == 200 and patient is None:
            patient = patient_schema.dump(save_patient(request_patient))

        return {"code": 200, "data": patient}, 200


class PatientListByIdResource(Resource):
    @classmethod
    def get(cls):
        ids = request.args.get("ids")
        # size   = request.args.get("size", 20)
        # offset = request.args.get("offset", 0)

        ids_transformed = list(map(lambda number: int(number), ids.split(",")))

        patients_query = PatientsModel.query.filter(PatientsModel.patient_id.in_(ids_transformed)).all()

        ids_found_in_db = list(map(lambda item: item.patient_id, patients_query))

        ids_to_look_for = list(set(ids_found_in_db).symmetric_difference(ids_transformed))

        if not ids_to_look_for:
            patients = patients_schema.dump(patients_query)

            return {"code": 200, "data": patients}, 200

        for id in ids_to_look_for:

            request_in_fhir = requests.get("{}/Patient/{}?_format=json".format(API_ROOT, id))

            if request_in_fhir.status_code == 200:
                patient = save_patient(request_in_fhir)

                patients_query.append(patient)

        patients = patients_schema.dump(patients_query)

        return {"code": 200, "data": patients}, 200
