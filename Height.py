while True:
    Conversion = input("Convert 1.(Foot/inch to m/cm) or 2.(m/cm to Foot/inch) [Press 1/2]: ")
    if Conversion == "1":  # Height from Foot/inch to m/cm
        f = float(input("Height(in Foot) :"))
        g = f * 12
        h = g * 2.54
        print("Height in cm: ", h)
        i = h / 100
        print("Height in meters: ", i)
    if Conversion == "2":  # Height from m/cm to Foot/inch
        Check = input("The Height u want to enter is in meter or cm (m/cm): ")
        if Check == "cm":
            x = float(input("Height(in cm) :"))
            y_inch = x / 2.54  # 1inch = 2.54cm ,1foot = 12inch
            z_foot = y_inch / 12
            print("Height in foot:", z_foot, "Height in inch:", y_inch)
            Repeat_Process = input("Do you want to convert Height again (Yes/No): ")
            if Repeat_Process != "Yes" or "yes":
                print("I am glad to help you")
            else:
                x = float(input("Height(in cm) :"))
                y_inch = x / 2.54  # 1inch = 2.54cm 1foot = 12inch
                z_foot = y_inch / 12
                print("Height in foot:", z_foot, "Height in inch:", y_inch)
        else:
            a = float(input("Height(in m) :"))
            b = a * 100
            y_inch = b / 2.54  # 1inch = 2.54cm ,1foot = 12inch
            z_foot = y_inch / 12
            print("Height in foot:", z_foot, "Height in inch:", y_inch)
            Repeat_Process = input("Do you want to convert Height again (Yes/No): ")
            if Repeat_Process != "Yes" or "yes":
                print("I am glad to help you")
            else:
                a = float(input("Height(in m) :"))
                b = a * 100
                y_inch = b / 2.54  # 1inch = 2.54cm ,1foot = 12inch
                z_foot = y_inch / 12
                print("Height in foot:", z_foot, "Height in inch:", y_inch)

    Repeat_Process = input("Do you want to convert height again (Yes/No): ")
    if Repeat_Process == "Yes" or Repeat_Process == "yes":
        continue
    else:
        print("End Process")
        break
