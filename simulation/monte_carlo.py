import numpy as np
from models.weather import WeatherData

def weather_risk_from_db(session, size):
    """
    Returns a weather multiplier array for Monte Carlo simulation.
    1. Fetches historical weather data
    2. Uses temperature and precipitation to adjust risk
    3. Returns array of multipliers of length 'size'
    """
    records = session.query(WeatherData).all()
    if not records:
        return np.ones(size)  # no effect

    temps = [r.avg_temp for r in records]
    precips = [r.precipitation for r in records]

    avg_temp = np.mean(temps)
    avg_precip = np.mean(precips)

    # heat increases risk slightly
    heat_factor = np.random.normal(1.08, 0.02, size) if avg_temp > 90 else np.ones(size)
    # heavy precipitation increases risk
    storm_factor = np.random.normal(1.10, 0.05, size) if avg_precip > 2 else np.ones(size)

    return heat_factor * storm_factor