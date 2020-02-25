import os
from datetime import datetime
import requests
from flask_restful import Resource

from app import db

from decorators import abort_if_not_exist
from models import DiagnosticReportDataModel
from schemas import DiagnosticReportDataSchema

diagnostics_report_data_schema = DiagnosticReportDataSchema(many=True)

API_ROOT = os.getenv("API_ROOT")


def save_diagnostic_report(patient_id, response):
    req = response.json()

    diagnostics = []

    if "entry" in req:
        for item in req["entry"]:
            diagnostic_report = DiagnosticReportDataModel(
                name=item["resource"]["code"]["coding"][0]["display"],
                active=item["resource"]["status"],
                date=datetime.strptime(item["resource"]["issued"], "%Y-%m-%dT%H:%M:%S"),
                results=", ".join(item["reference"] for item in item["resource"]["result"]),
                patient_id=patient_id
            )

            diagnostics.append(diagnostic_report)

            db.session.add(diagnostic_report)
            db.session.commit()

    return diagnostics


class PatientsByIdWithDiagnosticReportResource(Resource):
    decorators = [abort_if_not_exist(entity="Diagnostic report")]

    @classmethod
    def get(cls, patient_id):

        diagnostic_query = DiagnosticReportDataModel.query.filter_by(patient_id=patient_id).all()

        diagnostic = None

        if diagnostic_query is not None and isinstance(diagnostic_query, DiagnosticReportDataModel):
            diagnostic = diagnostics_report_data_schema.dump(diagnostic_query)

        request_diagnostic = requests.get("{}/DiagnosticReport?subject={}&_format=json".format(API_ROOT, patient_id))

        if request_diagnostic.status_code == 200 and request_diagnostic.json()["total"] > 0:
            diagnostic = diagnostics_report_data_schema.dump(save_diagnostic_report(patient_id, request_diagnostic))

        return {"code": 200, "data": diagnostic}, 200
