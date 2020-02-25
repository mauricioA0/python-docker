from app import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey


class PatientsModel(db.Model):
    __tablename__ = "patient"

    patient_id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    address = Column(String)
    diagnosticreports = Column(String)


class DiagnosticReportDataModel(db.Model):
    __tablename__ = "diagnostic_report_data"

    diagnostic_report_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    active = Column(String)
    date = Column(DateTime)
    results = Column(String)
    patient_id = Column(Integer, ForeignKey("patient.patient_id", ondelete="cascade"), nullable=False)
