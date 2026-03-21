import pandas as pd
from models.fleet import FleetVehicle

def load_fleet_data(csv_path, session):
    """
    Load fleet CSV into the database.

    CSV columns: vehicle_type, category, mileage, mpg, value
    """
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        vehicle = FleetVehicle(
            vehicle_type=row.get("vehicle_type", "light"),
            category=row.get("category", "unknown"),
            mileage=int(row.get("mileage", 50000)),
            fuel_efficiency=float(row.get("mpg", 25)),
            estimated_value=float(row.get("value", 10000))
        )
        session.add(vehicle)
    session.commit()