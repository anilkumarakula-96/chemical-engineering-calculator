print("CHEMICAL ENGINEERING HEAT CALCULATOR")
print("------------------------------------")

mass = float(input("Enter mass (kg): "))
cp = float(input("Enter specific heat capacity (kJ/kg K): "))
t1 = float(input("Enter initial temperature (C): "))
t2 = float(input("Enter final temperature (C): "))

if mass <= 0:
    print("Error: Mass must be positive.")

elif cp <= 0:
    print("Error: Specific heat capacity must be positive.")

elif t2 < t1:
    print("Error: Final temperature must be greater than or equal to initial temperature.")

else:
    heat = mass * cp * (t2 - t1)

    print("------------------------------------")
    print("Heat required =", heat, "kJ")
    print("Calculation completed successfully!")
