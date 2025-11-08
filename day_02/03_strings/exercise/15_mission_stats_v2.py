mission = "Orbiter Alpha"
distance_km = 1500000.4567
days = 92.5
speed = distance_km / (days * 24)
completion = 0.35123

print(" Mission Log ")
print(f"Mission: {mission}")
print(f"Distance: {distance_km} km")
print(f"Duration: {days} days")
print(f"Speed: {speed} km/h")
print(f"Completion: {completion}")

# TODO: Follow the given format:
"""
    ====== Mission Log ======
    Orbiter Alpha ===========
    Distance: 1,500,000.5 km
    Duration: 92.50 days
    Speed: 675.68 km/h
    Completion: 35.123%
    =========================
"""
