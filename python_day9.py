# 1. Create a BankAccount Class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")
# Create object
account1 = BankAccount("Deepika", 5000)
account1.deposit(1000)
account1.withdraw(2000)
account1.display_balance()

# 2. Inheritance Example

class Student(BankAccount):
    def __init__(self, name, balance, usn):
        super().__init__(name, balance)
        self.usn = usn
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"USN: {self.usn}")
        print(f"Balance: {self.balance}")
student1 = Student("Deepika", 3000, "1PE23XX001")
student1.display_details()