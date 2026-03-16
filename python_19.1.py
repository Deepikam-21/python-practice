# Check uppercase or lowercase

ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
else:
    print("Not an alphabet")