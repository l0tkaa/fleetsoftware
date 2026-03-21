from sqlalchemy import Column, Integer, Float, String, Date
from .db import Base

class MaintenanceLog(Base):
    """
    Stores per-vehicle maintenance history.
    Used to sample realistic maintenance costs.
    """
    __tablename__ = "maintenance_logs"

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(String)             # ID matching fleet vehicle
    maintenance_date = Column(Date)         # Date of maintenance
    maintenance_type = Column(String)       # e.g., Oil Change, Brake Repair
    cost = Column(Float)                    # Cost of maintenance
    odometer = Column(Float)                # Vehicle mileage at maintenance
    parts_replaced = Column(String)         # Parts replaced