# ------------ Q1 Write a function to find the maximum of two numbers.
# ------------ Q2 Write a function to find the greatest common divisor (GCD) of two numbers.
# ------------ Q3 Write a function to convert decimal numbers to binary.
# ------------ Q4 Write a function to calculate the power of a number.
# ------------ Q5 Write a function to calculate the sum of all elements in a list.
# ------------ Q6 Write a function to check if a string is a palindrome.
# ------------ Q7 Write a function to calculate the average of numbers in a list.
# ------------ Q8 Write a function to find the largest element in a list.
# ------------ Q9 Write a function to return the reverse of a string.
# ------------ Q10 Write a function to count the number of vowels in a string.


# ------------ Q1 Write a function to find the maximum of two numbers.
"""mth1 """
def mth(a,b):
    return max(a,b)

a=int(input())
b=int(input())
print("maximum B/W two no: ",mth(a,b))

""" mth 2"""
def mth(a,b):
    if a>b:
        return a
    else:
        return b

a=int(input())
b=int(input())
print("maximum B/W two no: ",mth(a,b))

# ------------ Q2 Write a function to find the greatest common divisor (GCD) of two numbers.
def mth(a,b):
    """ here logic 
        if a == 0:
            return b
        if b == 0:
            return a

        mathematically:
            gcd(0, b) = b
            gcd(a, 0) = a

        ex: 
            0 % 5 = 0
            0 % 1 = 0
            0 % 100 = 0
    """
    if a==0:
        return b
    
    if b==0:
        return a
    
    minx=min(a,b)
    g=1
    for i in range(1,minx+1):
        if a% i==0  and b% i==0 :
            g=i
    return g
a=int(input())
b=int(input())
print(mth(a,b))

# ------------ Q3 Write a function to convert decimal numbers to binary.
def mth(n):
    l=[]
    r=1
    while n>0:
        r=n%2
        l.append(r)
        n=n//2

    for i in range(len(l)-1,-1,-1):
        print(l[i],end="")
 
n =int(input())
mth(n)

# ------------ Q4 Write a function to calculate the power of a number.
def mth(b,p):
    return b**p

b=int(input())
p=int(input())
print(mth(b,p))

# ------------ Q5 Write a function to calculate the sum of all elements in a list.
def mth(l):
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s
l=[1,2,4,4,5]
print(mth(l))

# ------------ Q6 Write a function to check if a string is a palindrome.
def mth(s):
    org = s
    
    rev=""
    for i in range(len(s)-1,-1,-1):
        rev+=s[i]
    
    if org == rev:
        return True
    else:
        return False
    
s=input()
print(mth(s))

# ------------ Q7 Write a function to calculate the average of numbers in a list.
def mth(l):

    s=0
    for i in l:
        s+=i
    
    return s/len(l)

l=[4,8,9]
print(mth(l))

# ------------ Q8 Write a function to find the largest element in a list.
def mth(l):
    
    m=0
    for i in l:
        if i>m:
            m=i

    return m
l=[5,9,9238,6,4]
print(mth(l))
"""Note:  m = 0 ❌ This fails if list contains negative numbers.
    Example: l = [-10, -5, -1]
    It will return 0 (wrong).
"""
def mth(l):
    
    m=l[0]
    for i in l:
        if i>m:
            m=i

    return m
l=[5,9,9238,6,4]
print(mth(l))

# ------------ Q9 Write a function to return the reverse of a string.
def mth(s):
    print(s)
    rev=""
    for i in range(len(s)-1,-1,-1):
        rev+=s[i]
    return rev
s=input()
print(mth(s))

# ------------ Q10 Write a function to count the number of vowels in a string.
def mth(s):

    c=0
    v= "aeiou"
    l=[]
    for i in s:
        if i in v:
            c+=1
            l.append(i)

    return c,l
s=input()
print(mth(s))