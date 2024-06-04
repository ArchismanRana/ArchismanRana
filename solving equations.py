from sympy import *

while True:
    Quadratic_Eq = (input("Enter a Quadratic Eq. (ax^2 + bx + c = 0): "))
    a = int(input("Enter the value of a in ax^2 : "))
    b = int(input("Enter the value of b in bx : "))
    c = int(input("Enter the value of c in c : "))
    x = symbols("x")
    E_q = Eq(Quadratic_Eq)
    sol_ = solve(E_q),(x)
    print(sol_)
