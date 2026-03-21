from sqlalchemy import Column, Integer, Float, String
from .db import Base

class FuelRecord(Base):
    """
    Stores fuel efficiency records for sampling in Monte Carlo.
    """
    __tablename__ = "fuel_records"

    id = Column(Integer, primary_key=True)
    mpg = Column(Float)                     # Miles per gallon
    vehicle_type = Column(String)           # e.g., truck, light