from sqlalchemy import Column, Integer, Float, String
from .db import Base

class FleetVehicle(Base):
    """
    Stores information for each vehicle in the fleet.
    Used for fleet-wide analysis.
    """
    __tablename__ = "fleet_vehicles"

    id = Column(Integer, primary_key=True)
    vehicle_type = Column(String)           # truck, light, offroad
    category = Column(String)               # pickup, sedan, SUV
    mileage = Column(Integer)
    fuel_efficiency = Column(Float)         # MPG
    estimated_value = Column(Float)         # Current resale value