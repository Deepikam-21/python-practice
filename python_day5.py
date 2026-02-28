# 1. Find Maximum Element in List
numbers = [12, 45, 7, 89, 23]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum element:", maximum)

# 2. Remove Duplicates from List

nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
print("List after removing duplicates:", unique_nums)