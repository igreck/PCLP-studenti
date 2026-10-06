nume = input("Cum te numești? ")
celsius = float(input("Temperatura în Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{nume}, temperatura este {fahrenheit:.1f} F")
if celsius < 0:
    print("Temperatura este sub zero grade Celsius.")
else:
    print("Temperatura este cel puțin zero grade Celsius.")
