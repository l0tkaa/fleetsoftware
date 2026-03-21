import numpy as np
from models.maintenance import MaintenanceLog

def sample_maintenance_cost(session, vehicle_id, size):
    """
    Sample historical maintenance costs for a vehicle.

    - Uses actual maintenance history from CSV/DB
    - Falls back to zero if no records exist
    """
    records = session.query(MaintenanceLog).filter_by(vehicle_id=str(vehicle_id)).all()

    if not records:
        return np.zeros(size)

    costs = [r.cost for r in records if r.cost is not None]
    return np.random.choice(costs, size=size)