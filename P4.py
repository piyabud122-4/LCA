v = float(input("Enter voltage (V): "))
i = float(input("Enter current (A): "))
time = float(input("Enter operating time (h): "))
power = v*i
energy = power*time
cost = (energy/1000)*4
print("The cost is",cost)