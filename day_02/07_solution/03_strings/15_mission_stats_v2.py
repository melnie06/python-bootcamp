mission = "Orbiter Alpha"
distance_km = 1500000.4567
days = 92.5
speed = distance_km / (days * 24)
completion = 0.35123

width = 30  # total line width

print(f'{"":=^{width}}')
print(f'{mission:=^{width}}')
print(f'Distance: {distance_km:,.1f} km')
print(f'Duration: {days:.2f} days')
print(f'Speed: {speed:.2f} km/h')
print(f'Completion: {completion:.3%}')
print(f'{"":=^{width}}')
