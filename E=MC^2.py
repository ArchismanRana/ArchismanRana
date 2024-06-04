# Program for E=MC^2
while True:
    Given = str(input("What values do u have? (Energy/Mass) : "))
    if Given == "Energy" or Given == "energy":
        Value_energy = float(input("Enter the value of Energy in Joules(J) : "))
        Mass = Value_energy / ((3 * (10 ** 8)) ** 2)
        print("Value of Mass in Kg : ", Mass, "Kg")
    if Given == "Mass" or Given == "mass":
        Value_Mass = float(input("Enter the value of Mass in Kg : "))
        Energy = Value_Mass * ((3 * (10 ** 8)) ** 2)
        print("Value of Energy in Joules(J) : ", Energy, "J")
    Repeat_Process = input("Do you want to find roots of another Quadratic Eq. (Yes/No): ")
    if Repeat_Process == "Yes" or Repeat_Process == "yes":
        continue
    else:
        print("End Process")
        break
