# 1. Write a program to print a multiplication table for a given number.
# 2. Write a program to print the sum of all numbers in a range provided by the user.
# 3. Write a program to reverse a given number.
# 4. Write a program to check if a number is an Armstrong number.
# 5. Write a program to find the sum of digits of a number.
# 6. Write a program to print the first n prime numbers.
# 7. Write a program to print Pascal’s triangle.
# 8. Write a program to check if a year is a leap year.
# 9. Write a program to print the sum of even and odd numbers in a given range.
# 10. Write a program to print a pyramid pattern using stars.


# 1. Write a program to print a multiplication table for a given number.

n = int(input())
s=0
for i in range(1,11):
    s=n*i
    print(f"{n} * {i} = {s}")

# 2. Write a program to print the sum of all numbers in a range provided by the user.
n = int(input())
s=0
for i in range(n+1):
    s+=i
print(s)

# 3. Write a program to reverse a given number.
"""mth1"""
r=0
s=0
n=int(input())
org =n
while n !=0:
    r=n%10
    s=s*10+r
    n=n//10
print("original no: ",org)
print("reverse no: ", s)

"""mth2"""
r=0
s=0
n=int(input())
org= n
n=str(n)
for i in range(len(n)-1,-1,-1):
    r=int(n[i])
    s=s*10+r
print("original no: ",org)
print("reverse no: ", s)

# 4. Write a program to check if a number is an Armstrong number.
n=int(input())
original=n
org = n
c=0
while n>0:
    n=n//10
    c+=1


r=0
s=0
while org>0:
    r=org%10
    s=s+r**c
    org=org//10

if original == s:
    print("Armstrong")
else:
    print("Not armstrong")

# 5. Write a program to find the sum of digits of a number.
n=int(input())
print(n)
r=0
s=0
while n > 0:
    r=n%10
    s=s+r
    n=n//10
print(s)

# 6. Write a program to print the first n prime numbers.

n=int(input())

for i in range(2,n+1):
    c=0
    for j in range(1,i+1):
        if i % j ==0: 
            c+=1


    if c==2:
        print(i, end=" ")

"""correct verions """
n = int(input())  # number of primes to print
count = 0
i = 2
while count < n:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
        count += 1
    i += 1

"""output:10
2 3 5 7 11 13 17 19 23 29 
"""
# 8. Write a program to check if a year is a leap year.
a=int(input())

if a%400==0 or (a%100!=0 and a%4==0):
    print("leap year", a)
else:
    print("Not year")

# 9. Write a program to print the sum of even and odd numbers in a given range.
n=int(input())
e=0
o=0
for i in range(1,n+1):
    if i % 2==0:
        e+=i
    else:
        o+=i

print("even no till n :",e)
print("odd no till n: ",o)

# 10. Write a program to print a pyramid pattern using stars.

# ex: --If the number of rows is 5, the pyramid will look like this:

#     *
#    ***
#   *****
#  *******
# *********

# Pseudo code 
# i =0  j =0  space n-i  1 star
# i= 1  j=1   sapce n-i  3 star 
# i= 2  j=2   space n-i  5 star

n=int(input())
for i in range(n):
    for j in range(1,n-i-1):
        print(" ",end="")
  
    for j in range(2*i+1):
        print("*",end="")
    print()


