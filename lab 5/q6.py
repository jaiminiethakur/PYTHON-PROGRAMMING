fahrenheit_temps = [32, 50, 77, 104, 212]
celsius_temps = []

for f in fahrenheit_temps:
    c = (f - 32) * 5 / 9
    celsius_temps.append(c)

print(celsius_temps)