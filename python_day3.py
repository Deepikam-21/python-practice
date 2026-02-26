# 1. Right Triangle Pattern
rows = 6
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2. Inverted Triangle Pattern
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 3. Number Pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 4. Floyd’s Triangle
rows = 4
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()