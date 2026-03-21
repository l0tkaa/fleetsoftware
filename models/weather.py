from sqlalchemy import Column, Integer, Float, Date
from .db import Base

class WeatherData(Base):
    """
    Stores weather data to model risk multipliers.
    Used to adjust Monte Carlo results for extreme conditions.
    """
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    avg_temp = Column(Float)                # Daily or monthly average temperature
    precipitation = Column(Float)           # Rainfall / snow (inches)