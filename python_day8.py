# 1. Write and Read from File

with open("sample.txt", "w") as file:
    file.write("Hello \n")
    file.write("This is text file.\n")
print("File written successfully!")
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)

# 2. Handle Division Exception

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Enter integers only.")
finally:
    print("Execution completed.")