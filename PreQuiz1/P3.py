v = float(input("Enter voltage (V): "))
i = float(input("Enter current (A): "))
time = float(input("Enter operating time (h): "))
power = v*i
energy = power*time
print("The energy consumed is", energy, "Wh")