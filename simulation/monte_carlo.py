import numpy as np
from simulation.fuel_model import sample_fuel_cost
from simulation.maintenance_model import sample_maintenance_cost
from simulation.weather_model import weather_risk_from_db

def run_simulation(vehicle, session, num_samples=1000):
    """
    Monte Carlo simulation for a single vehicle.

    Steps:
    1. Sample repair costs uniformly between low/high estimates
    2. Sample fuel costs based on real fuel records
    3. Sample maintenance costs based on real maintenance logs
    4. Multiply total costs by weather risk multipliers
    5. Return array of total simulated losses
    """
    repair_costs = np.random.uniform(vehicle.repair_cost_low, vehicle.repair_cost_high, num_samples)
    fuel_costs = sample_fuel_cost(session, vehicle, num_samples)
    maintenance_costs = sample_maintenance_cost(session, vehicle.id, num_samples)
    weather_multiplier = weather_risk_from_db(session, num_samples)

    total_losses = (repair_costs + fuel_costs + maintenance_costs) * weather_multiplier
    return total_losses