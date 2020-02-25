from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class DiagnosticReportDataSchema(ma.Schema):
    diagnostic_report_id = fields.Integer()
    name = fields.String()
    active = fields.Boolean()
    date = fields.DateTime()
    results = fields.String()
    patient_id = fields.Integer()
