import pandas as pd
from models.maintenance import MaintenanceLog

def load_maintenance_csv(csv_path, session):
    """
    Load historical maintenance costs into DB.
    Used to sample realistic maintenance expenses.
    """
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        log = MaintenanceLog(
            vehicle_id=row.get("vehicle_id"),
            maintenance_date=row.get("maintenance_date"),
            maintenance_type=row.get("maintenance_type"),
            cost=float(row.get("cost", 0)),
            odometer=float(row.get("odometer_reading", 0)),
            parts_replaced=row.get("parts_replaced", "")
        )
        session.add(log)
    session.commit()