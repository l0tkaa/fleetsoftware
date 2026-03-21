import numpy as np
from models.fuel import FuelRecord

def sample_fuel_cost(session, vehicle, size):
    """
    Sample fuel cost for Monte Carlo simulation.

    1. Select fuel records for the vehicle type.
    2. Randomly sample 'size' values.
    3. Calculate fuel cost assuming 100 miles per period.
    """
    records = session.query(FuelRecord).filter_by(
        vehicle_type=vehicle.vehicle_type
    ).all()

    if not records:
        # fallback: use base fuel cost
        return np.full(size, vehicle.fuel_cost)

    mpg_values = [r.mpg for r in records]
    sampled_mpg = np.random.choice(mpg_values, size=size)

    fuel_price_per_gallon = 3.5  # USD
    return fuel_price_per_gallon * (100 / sampled_mpg)  # cost for 100 miles