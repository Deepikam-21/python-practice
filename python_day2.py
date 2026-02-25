# palindrome number
num=int(input("enter a number:"))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
    print("the number is palindrome")
else:
    print("the number is not palindrome")

# count digits in a number
n=int(input("enter a number:"))
count=0
while n>0:
    n=n//10
    count=count+1
print("total digits:",count)
      
# sum of digits in a number
num=int(input("enter a number:"))
sum_digits=0
while num>0:
    digit=num%10
    sum_digits=sum_digits+digit
    num=num//10
print("sum of digits:",sum_digits)

# fibonacci series
n=int(input("enter a numbers:"))
a=0
b=1
print("fibonacci series")
for i in range(n):
    print(a,end=" ")
    next_num=a+b
    a=b
    b=next_num

    