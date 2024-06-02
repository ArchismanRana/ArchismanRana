# Area and Volume of Cube, Cuboid, Cylinder, Sphere, Prism, Pyramid, Regular Polyhedron
import math
from math import *

while True:
    Shape = (input(
        'For which shape you want to find area and volume? (Cube/Cuboid/Cylinder/Sphere/Prism/Pyramid/Cone) :'))
    if Shape == "Cube" or Shape == "cube":
        side = (float(input("Enter length of Cube\n")))
        Area_Cube = (6 * (side ** 2))
        print("Area of your cube is : ", Area_Cube)  # Area
        Volume_Cube = side * side * side  # Volume
        print("Volume of your cube is : ", Volume_Cube)

    if Shape == "Cuboid" or Shape == "cuboid":
        Length = (float(input("Enter Length of Cuboid\n")))
        Breadth = (float(input("Enter Breadth of Cuboid\n")))
        Height_Cuboid = (float(input("Enter Height of Cuboid\n")))
        Area_Cuboid = 2 * ((Length * Breadth) + (Breadth * Height_Cuboid) + (Height_Cuboid * Length))
        print("Area of your cuboid is : ", Area_Cuboid)  # Area
        Volume_Cuboid = Length * Breadth * Height_Cuboid
        print("Volume of your cuboid is : ", Volume_Cuboid)  # Volume

    if Shape == "Cylinder" or Shape == "cylinder":
        Radius = (float(input("Enter Radius of Cylinder\n")))
        Height_Cylinder = (float(input("Enter Height of Cuboid\n")))
        Area_Cylinder = (2 * 3.14 * Radius * Height_Cylinder) + (2 * 3.14 * Radius * Radius)
        print("Area of your cylinder is : ", Area_Cylinder)  # Area
        Volume_Cylinder = 3.14 * (Radius ** 2) * Height_Cylinder
        print("Volume of your cylinder is : ", Volume_Cylinder)  # Volume

    if Shape == "Sphere" or Shape == "sphere":
        r = (float(input("Enter radius of sphere:")))
        area = 4 * pi * (r ** 2)
        volume = 4 / 3 * pi * pow(r, 3)
        print("Area of the sphere :", area, "units square")
        print("Volume of the sphere :", volume, "units cube")

    if Shape == "Cone" or Shape == "cone":
        r = (float(input("Enter radius of cone:")))
        h = (float(input("Enter height of cone:")))
        l = math.sqrt(h ** 2 + r ** 2)
        area = (pi * r * l) + (pi * r * r)
        volume = 1 / 3 * pi * r * r * h
        print("Area of the cone :", area, "units square")
        print("Volume of the cone :", volume, "units cube")

    if Shape == "Prism" or Shape == "prism":
        b = (float(input("Enter base of prism:")))
        h = (float(input("Enter height of prism:")))
        x = (float(input("Enter length of prism:")))
        area = (b * h) + ((b + b + b) * h)
        volume = 1 / 2 * b * h * x
        print("Area of the prism :", area, "units square")
        print("Volume of the prism :", volume, "units cube")

    if Shape == "Pyramid" or Shape == "pyramid":
        r = (float(input("Enter radius of sphere:")))
        area = 4 * pi * (r ** 2)
        volume = 4 / 3 * pi * pow(r, 3)
        print("Area of the sphere :", area, "units square")
        print("Volume of the sphere :", volume, "units cube")

    Repeat_Process = input("Do you want to find area and vol for another shape (Yes/No): ")
    if Repeat_Process == "Yes" or Repeat_Process == "yes":
        continue
    else:
        print("I am glad to help you!!")
        break
