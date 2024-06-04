n = 10
for i in range(1, n + 1):
    for k in range(1, n - i + 1):
        print(" ", end=' ')
    for j in range(1, (2 * i - 1) + 1):
        print("*", end=' ')

    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or j == 1 or i == n or j == n:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

# --------------------------------------------------------
# CODE FOR LETTER Z
row = int(input("No. of rows : "))
for i in range(1, row + 1):  # Row run horizontal
    for j in range(1, row + 1):  # Column run vertical
        if i == 1 or i == row or i + j == row + 1:
            print("*", end=" ")
        else:
            print(" ", end=' ')
    print()

# --------------------------------------------------------
# CODE FOR LETTER A
row = int(input("No. of rows : "))
for i in range(1, row + 1):  # Row run horizontal
    for j in range(1, row + 1):  # Column run vertical
        for k in range(5, 12, +2):
            if i+j == (5, 6, 7, 8, 9) or i+j == 5 or i + j == k:
                print("*", end=" ")
            else:
                print(" ", end=' ')
    print()
