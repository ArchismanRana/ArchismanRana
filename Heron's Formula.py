# Area of triangle when 3 sides are given by using Heron's Formula

while True:
    a = float(input('Enter length of side 1: '))
    b = float(input('Enter length of side 2: '))
    c = float(input('Enter length of side 3: '))

    s = float((a + b + c) / 2)
    Area_square = (s * (s - a) * (s - b) * (s - c))
    area = (Area_square)**0.5
    print('Area of the triangle is : ', area)

    Repeat_Process = input("Do you want to find area of another triangle (Yes/No): ")
    if Repeat_Process == "Yes" or Repeat_Process == "yes":
        continue
    else:
        print("End Process")
        break
