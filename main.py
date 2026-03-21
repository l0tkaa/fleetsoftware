from models.db import Base, engine, SessionLocal
from utils.fleet_loader import load_fleet_data
from utils.fuel_loader import load_fuel_data
from utils.maintenance_loader import load_maintenance_csv
from services.fleet_analysis import analyze_fleet

def main():
    # 1. Create DB tables
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    # 2. Load CSV data
    load_fleet_data("fleet.csv", session)
    load_fuel_data("fuel.csv", session)
    load_maintenance_csv("maintenance.csv", session)

    # 3. Run fleet-wide Monte Carlo analysis
    results = analyze_fleet(session)

    # 4. Print results for each vehicle
    for vid, res in results:
        print(f"Vehicle {vid}: {res}")

if __name__ == "__main__":
    main()