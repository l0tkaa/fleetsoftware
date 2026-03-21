import pandas as pd
from models.fuel import FuelRecord

def load_fuel_data(csv_path, session):
    """
    Load fuel efficiency records into DB.
    Used to sample fuel costs in Monte Carlo.
    """
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        record = FuelRecord(
            mpg=float(row["mpg"]),
            vehicle_type=row.get("vehicle_type", "light")
        )
        session.add(record)
    session.commit()