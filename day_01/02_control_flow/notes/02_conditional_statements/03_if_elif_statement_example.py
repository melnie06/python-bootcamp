battery = int(input("Battery percentage: "))

if battery >= 80:
    print("Full Battery")
elif battery >= 40:
    print("Good Battery")
elif battery >= 15:
    print("Low Battery")
elif battery > 0:
    print("Critically Low Battery")
