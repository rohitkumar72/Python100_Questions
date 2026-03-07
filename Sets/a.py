# 1. Write a program to find the union of two sets.
# 2. Write a program to find the intersection of two sets.
# 3. Write a program to find the difference between two sets.
# 4. Write a program to check if one set is a subset of another.
# 5. Write a program to remove duplicates from a list using a set.
# 6. Write a program to check if two sets are disjoint.
# 7. Write a program to create a set of squares of numbers from 1 to 10.
# 8. Write a program to find the symmetric difference between two sets.
# 9. Write a program to check if a set is empty.
# 10. Write a program to convert a set to a list.


# 1. Write a program to find the union of two sets.
s={1,2,3,4,5}
s1={5,6,7,8,9}

print(s|s1)
print(s.union(s1))

"""mth2"""
s3=set()
for i in s:
    s3.add(i)
for i in s1:
    s3.add(i)
print(s3)

# 2. Write a program to find the intersection of two sets.
s={1,2,3,4,5}
s1={5,6,7,8,9}
print(s.intersection(s1))

"""mth2"""
s3=set()
for i in s:
    if i  in s1:
        s3.add(i)
print(s3)

# 3. Write a program to find the difference between two sets.
"""The difference between two sets means:
Elements that are in the first set but NOT in the second set."""

s={1,2,3,4,5}
s1={5,6,7,8,9}

print(s-s1)
print(s.difference(s1))

# 4. Write a program to check if one set is a subset of another.
"""A subset means all elements of one set exist in another set.
"""
A = {1,2,3}
B = {1,2,3,4,5}

b= True
for i in A:
    if i not in B:
        b= False   
        """avoid unnecessary check"""
        break                       
print(b)

"""mth2"""
print(A.issubset(B))

# 5. Write a program to remove duplicates from a list using a set.

a = [1,2,3,3,4,5,5]
b=set()
for i in a:
    b.add(i)
print(b)

# 6. Write a program to check if two sets are disjoint.

""" two set are said to disjoint if they dont have common elements """

a={1,2,3,4,5}
b={6,7,8,9,5}

v= True
for i in a:
    if i in b:
        v=False

print(v)
print(a.isdisjoint(b))

# 7. Write a program to create a set of squares of numbers from 1 to 10.

s=set()
n=0
for i in range(1,11):
    n=i**2
    s.add(n)
print(s,end="")
# # 8. Write a program to find the symmetric difference between two sets.
""" The symmetric difference between two sets means:
 Elements that are in either set A or set B, but NOT in both."""
"""remove common from both the set """


A = {1,2,3,4}
B = {3,4,5,6}

s3=set()

for i in A:
    if i not in B:
        s3.add(i)

for i in B:
    if i not in A:
        s3.add(i)
print(s3)


# 9. Write a program to check if a set is empty.
s=set()
b=False
if s==" ":
    b=True

print(b)
"""
if s == " "
You are comparing a set with a string.
s → set
" " → string
So this condition will always be False.
"""
s= set()
if len(s)==0:
    print("set is empty")
else:
    print("set is not empty")
"""
Note :
Quick rule
len(collection) = number of elements inside it
Works for:
list
tuple
set
dictionary
string

Example:
len([1,2,3]) → 3
len("hello") → 5
len(set())   → 0

"""
# 10. Write a program to convert a set to a list.
s={1,2,4,5,6}
l=[]
for i in s:
    l.append(i)
print(l)
