from sqlalchemy import Column, Integer, Float, String
from .db import Base

class Vehicle(Base):
    """
    Table representing a single vehicle for Monte Carlo simulation.
    """
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    vehicle_type = Column(String)           # e.g., truck, light, offroad
    current_value = Column(Float)           # Resale value in dollars
    mileage = Column(Integer)               # Odometer reading
    repair_cost_low = Column(Float)         # Minimum estimated repair cost
    repair_cost_high = Column(Float)        # Maximum estimated repair cost
    fuel_cost = Column(Float)               # Base fuel cost per period
    insurance_coverage = Column(Float)      # Insurance coverage in dollars
    month = Column(Integer)                 # Current month for seasonal effects