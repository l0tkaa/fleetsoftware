from models.fleet import FleetVehicle
from services.decision_engine import analyze_vehicle

def analyze_fleet(session):
    """
    Run Monte Carlo analysis for all vehicles in the fleet.
    Returns list of tuples: (vehicle_id, analysis result)
    """
    vehicles = session.query(FleetVehicle).all()
    results = []

    for v in vehicles:
        result = analyze_vehicle(v, session)
        results.append((v.id, result))

    # Sort by expected loss descending
    results.sort(key=lambda x: x[1]["expected_loss"], reverse=True)
    return results