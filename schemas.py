from marshmallow import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class PatientSchema(ma.Schema):
    patient_id = fields.Integer(required=True)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    address = fields.String()


class DiagnosticReportDataSchema(ma.Schema):
    diagnostic_report_id = fields.Integer()
    name = fields.String()
    active = fields.Boolean()
    date = fields.DateTime()
    patient_id = fields.Integer()
