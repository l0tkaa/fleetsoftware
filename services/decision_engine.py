import numpy as np
from simulation.monte_carlo import run_simulation

def analyze_vehicle(vehicle, session, num_samples=1000):
    """
    Returns decision for a single vehicle:

    - "SELL" if expected loss > resale value
    - "KEEP" otherwise

    Also returns risk profile: min, max, std deviation of losses
    """
    losses = run_simulation(vehicle, session, num_samples)
    expected_loss = np.mean(losses)

    risk_profile = {
        "min_loss": float(np.min(losses)),
        "max_loss": float(np.max(losses)),
        "std_dev": float(np.std(losses))
    }

    decision = "SELL" if expected_loss > vehicle.current_value else "KEEP"

    return {
        "decision": decision,
        "expected_loss": float(expected_loss),
        "resale_value": vehicle.current_value,
        "risk_profile": risk_profile
    }