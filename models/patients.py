from app import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey


class PatientsModel(db.Model):
    __tablename__ = "patient"

    patient_id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    address = Column(String)
    diagnosticreports = Column(String)
