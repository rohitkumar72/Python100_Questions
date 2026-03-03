""" 1.cd BasicPython
    2.git add .
    3.git commit -m "Added new file inside src folder "
    4.git push origin main
"""

# ------------ Q1 Write a program to swap two variables
# ------------ Q2 Write a program to check if a number is even or odd.
# ------------ Q3 Write a program to find the square root of a number
# ------------ Q4 Write a program to find the area of a triangle.
# ------------ Q5 Write a program to check if a number is a palindrome.
# ------------ Q6 Write a program to convert temperatures from Celsius to Fahrenheit.
# ------------ Q7 Write a program to calculate the factorial of a number.
# ------------ Q8 Write a program to find the greatest of three numbers.
# ------------ Q9 Write a program to print all prime numbers between 1 and 100.
# ------------ Q10 Write a program to generate a Fibonacci sequence up to n terms.


# ------------ Q1 Write a program to swap two variables
"""mth 1:"""
a=int(input())
b= int(input())
print("No's before Swap:",a,b)
temp = a
a = b
b = temp

print("No's After Swap",a,b)

""" In this question logic is one value is stored in separately , one value is assign to other variable"""

"""mth 2"""

a=int(input())
b= int(input())
print("No's before Swap:",a,b)

b=a+b
a=b-a
b=b-a

print("No's after swap:",a,b)

"""In this logic, we add both numbers and store the result in one variable. Then we subtract one number to get the other, which helps us swap the values without using a third variable"""


# ------------ Q2 Write a program to check if a number is even or odd.
def mth(n):
    if n % 2==0:
        return "even"
    else:
        return "odd"

n=int(input("enter the number:",))
print(mth(n))

# ------------ Q3 Write a program to find the square root of a number
import math
def mth(n):
    return math.sqrt(n)
n=int(input())
print(mth(n))


"""mth2"""

def mth(n):
    return n**0.5

n=int(input())
print(mth(n))

"""
Here:
** means "power"
(1/2) means half power
Half power = square root

"""
# ------------ Q4 Write a program to find the area of a triangle.
base = int(input("enter the base:",))
height = int(input("enter the height:",))
ar = 0.5 * base * height
print("area of triangle:",ar)


# ------------ Q5 Write a program to check if a number is a palindrome.
def mth(n):
    org =n
    s=0
    r=0
    while n>0:
        r = n%10
        s=s*10+r
        n=n//10
    
    if org == s:
        return True
    else:
        return False

n=int(input())
print(mth(n))

# ------------ Q6 Write a program to convert temperatures from Celsius to Fahrenheit.
c=int(input("enter the Celsius: ", ))
f = (c *9/5)+32
print(f,"F")

"""formula of conversion celcius to fahrenheit ---> F=(C*9/5)+32 """

# ------------ Q7 Write a program to calculate the factorial of a number.

def mth(n):
    s=1
    while n>0:
        s=s*n
        n=n-1
    return s
n =int(input("enter the number :",))
print(mth(n))

# ------------ Q8 Write a program to find the greatest of three numbers.

def mth(a,b,c):
    if a>b and a>c:
        return "a is greater"
    elif b>a and b>c:
        return "b is greater"
    else:
        return "c is greater"
    
a=int(input("enter the first no: ",))
b=int(input("enter the 2nd number: ",))
c=int(input("enter the 3rd number: ",))
print(mth(a,b,c))

# ------------ Q9 Write a program to print all prime numbers between 1 and 100.

print("list of the prime numbers form 1 to 100 :")
for i in range(2, 101):
    s=0
    c=0
    for j in range(1,101):
        if i%j==0:
            c+=1
    if c==2:
        print(i,end=" ")

# ------------ Q10 Write a program to generate a Fibonacci sequence up to n terms.
# 0 1 1 2 3 5 8 13 21 34

c=0
a=0
b=1
print(a,b,end=" ")
n=int(input())
for i in range(n):
    c= a+b
    print(c,end=" ")
    a=b
    b=c

"""core logic in this assign one value to another value 

    ex: -- a=b
           b=c
"""