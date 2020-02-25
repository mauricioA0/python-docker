from flask import Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from resources.Patients import PatientByIdResource, PatientListByIdResource
from resources.DiagnosticReportData import PatientsByIdWithDiagnosticReportResource

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# [GET] /patient?ids={patient_id_1},{patient_id_2}&size={size}&offset={offset}
api.add_resource(PatientListByIdResource, "/patient")

# [GET] /patient/{patient_id}
api.add_resource(PatientByIdResource, "/patient/<int:patient_id>")

# [GET] /patient/{patient_id}/diagnostic_report
api.add_resource(PatientsByIdWithDiagnosticReportResource, "/patient/<int:patient_id>/diagnostic_report")
