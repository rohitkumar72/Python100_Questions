# 1. Write a program to create a tuple and print its elements.
# 2. Write a program to find the length of a tuple.
# 3. Write a program to find the maximum and minimum elements in a tuple.
# 4. Write a program to check if an element exists in a tuple.
# 5. Write a program to convert a list into a tuple.
# 6. Write a program to find the sum of elements in a tuple.
# 7. Write a program to concatenate two tuples.
# 8. Write a program to convert a tuple to a string.
# 9. Write a program to slice a tuple.
# 10. Write a program to find the index of an element in a tuple.

# 1. Write a program to create a tuple and print its elements.


"""
t = (0) * len(l) does not create a tuple.
(0) is just an integer, not a tuple
"""
# i=0

# for k in range(len(l)):
#     t[i]=l[k] 
#     """   t[0] = l[0]   # ❌ Error
#                     Tuples cannot be changed after creation """
#     i+=1

# print(t)

# sol: --

t=(1,2,3,4,5)
for i in t:
    print(i,end="")

"""
l=[1,2,3,4,5]
t=()
for i in l:
    t=t+(i,)
print(t)



Explanation
t = () → start with an empty tuple
(i,) → creates a single-element tuple
t + (i,) → creates a new tuple and adds the element
So every iteration:
() + (10,) → (10,)
(10,) + (20,) → (10,20)
(10,20) + (30,) → (10,20,30)"""

# 2. Write a program to find the length of a tuple.
"""len() returns the number of elements inside a collection."""
t=(1,2,3,4,5)
print(len(t))
t=(1,2,3,4,5)
c=0
for i in t:
    c+=1
print(c)

# 3. Write a program to find the maximum and minimum elements in a tuple.

t=(1,2,3,4,5)
maxx= t[0]
minxx = t[0]
for i in range(len(t)):
    if t[i]>maxx:
        maxx= t[i]

    if t[i]<minxx:
        minxx = t[i]

print("maximum element",maxx)
print("minimum element",minxx)


# 4. Write a program to check if an element exists in a tuple.
a=int(input())
t=(1,2,3,4,5)
b = True

if a not in  t:
        b=False
print(b)

# 5. Write a program to convert a list into a tuple.
l=[1,2,3,4,5]
t=()
for i in l:
    t = t+ (i,)
print(t)

# 6. Write a program to find the sum of elements in a tuple.
t=(1, 2, 3, 4, 5)
s=0
for i in t:
    s+=i
print(s)

# 7. Write a program to concatenate two tuples.
t=(1, 2, 3, 4, 5)
t2=(6,7,8,9,10,11)
print(t+t2)


# 8. Write a program to convert a tuple to a string.
t=(1, 2, 3, 4, 5)
s=""
for i in range(len(t)):
    s=s+str(t[i])
print(s)
print(type(s))

# 9. Write a program to slice a tuple.

"""Tuple slicing can be done in several ways using the slice syntax:
tuple[start : end : step]"""

t=(1,2,3,4,5)
print(t[2:4:1])

# 10. Write a program to find the index of an element in a tuple.
t=(1,2,3,4,5)
x=int(input("enter the element:",))
for i in range(len(t)):
    if t[i]==x:
        print("index",i)