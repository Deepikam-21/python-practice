# reverse a number
n=int(input("enter a number:"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print("reversed number:",reverse)

# check a prime number or not
num=int(input("enter a number:"))
if num<=1:
    print("the given number is not prime number.")
else:
    for i in range(2,num):
        if num%i==0:
            print("not prime number")
            break
    else:
        print("the given number is a prime number")

# factorial
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("the factorial of the number:",fact) 

# large among 3 numbers
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if a>=b and a>=c:
    print("a is largest")
elif b>=a and b>=c:
    print("b is largest")
else:
    print("c is largest")