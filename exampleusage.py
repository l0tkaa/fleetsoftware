from vehicle_loss_minimization import vehicle_loss_minimization, Range

vehicle_value = 3000
mileage = 95000
vehicle_type = "truck"
repair_range = Range(low=500, high=2500)
fuel_cost = 150
insurance_coverage = 200
month = 1  # January (Winter)

result = vehicle_loss_minimization(
    vehicle_type=vehicle_type,
    current_value=vehicle_value,
    mileage=mileage,
    repair_cost_range=repair_range,
    fuel_cost=fuel_cost,
    insurance_coverage=insurance_coverage,
    month=month,
    num_samples=1000,
    future_periods=1
)

print(result)
