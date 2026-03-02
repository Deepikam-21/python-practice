# 1. Sum of First N Natural Numbers using Recursion

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
print("Sum of first 5 numbers:", sum_n(5))

# 2. Power of a Number using Recursion

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
print("2 power 4:", power(2, 4))

# 3. Sort List using Lambda

numbers = [(1, 3), (2, 1), (4, 2)]
sorted_list = sorted(numbers, key=lambda x: x[1])
print("Sorted by second element:", sorted_list)

# 4. Map Function Example (Square numbers)

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print("Squared list:", squared)