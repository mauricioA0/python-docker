from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class PatientSchema(ma.Schema):
    patient_id = fields.Integer(required=True)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    address = fields.String()
