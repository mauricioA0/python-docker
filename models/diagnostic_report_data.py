from app import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class DiagnosticReportDataModel(db.Model):
    __tablename__ = "diagnostic_report_data"

    diagnostic_report_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    active = Column(String)
    date = Column(DateTime)
    results = Column(String)
    patient_id = Column(Integer, ForeignKey("patient.patient_id", ondelete="cascade"), nullable=False)
