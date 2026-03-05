# ------------ Q1 Write a program to create a list of the first 10 even numbers
# ------------ Q2 Write a program to remove duplicates from a list.
# ------------ Q3 Write a program to find the second-largest number in a list.
# ------------ Q4 Write a program to merge two sorted lists into one sorted list.
# ------------ Q5 Write a program to find the frequency of each element in a list.
# ------------ Q6 Write a program to check if two lists are equal.
# ------------ Q7 Write a program to flatten a nested list.
# ------------ Q8 Write a program to rotate a list by n positions.
# ------------ Q9 Write a program to find the cumulative sum of elements in a list.
# ------------ Q10 Write a program to find the intersection of two lists.

# ------------ Q1 Write a program to create a list of the first 10 even numbers

l=[]
for i in range(1,101):
    if i % 2==0:
       l.append(i)

for j in range(10):
    print(l[j],end=" ")

# ------------ Q2 Write a program to remove duplicates from a list.
l=[4,5,5,2,24,2,1,6,78,4]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)

print(l2)
   
# ------------ Q3 Write a program to find the second-largest number in a list.
"""this fails in large number"""
l=[4,5,5,2,24,2,1,6,78,4]
lar =l[0]
Sec_lar =l[0]

for i in range(len(l)):
    if l[i]>lar:
        lar=l[i]

    if l[i]>Sec_lar and l[i]<lar:
        Sec_lar=l[i]

print(l)
print("Largest_element",lar)
print("Second_Largest",Sec_lar)
"""
optimise varsion 
"""

l=[4,5,5,2,24,2,1,6,78,4]

lar = l[0]
sec = -999999

for i in l:
    if i > lar:
        sec = lar
        lar = i
    elif i > sec and i != lar:
        sec = i

print("Largest:", lar)
print("Second Largest:", sec)
# ------------ Q4 Write a program to merge two sorted lists into one sorted list.

"""core logic 
    ek element pick karo 
    check karo one time list ke ek dsre element ke saath 
    then check karo 2nd list ke elements ke saath
"""
l1=[1,5,9,12]
l2=[2,3,4,6]

i=0
j=0

l3=[]

while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i += 1
    else:
        l3.append(l2[j])
        j += 1

while i < len(l1):
    l3.append(l1[i])
    i += 1

while j < len(l2):
    l3.append(l2[j])
    j += 1
print(l3)

# ------------ Q5 Write a program to find the frequency of each element in a list.
"""
core logic 1. unique vales store karta hai or duplicates ko remove karta hai 
unique vales store karne ke baad check value exits  h count karo or print karo then add the unique vale in list
"""

"""mth1 """
l=[1,2,3,4,4,5,6,7,8,1]
l.sort()
print(l)
v=[]
for i in l:
    if i not in v:
        count =0
        for j in l:
            if i == j:
                count+=1
        print((i,count),end=" ")
    
        v.append(i)
"""mth2"""
l=[9,9,12,12,13,13,13,13,13,13,4,4,3,3,5,5,6]
l.sort()
print(l)
d={}
c=0
for i in l:
    if i not in d:
        d[i]=c

for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


# ------------ Q6 Write a program to check if two lists are equal.

"""
Inside the loop you are resetting b every time.
So even if earlier elements were different, the last comparison decides the result.
Example:
l1 = [1,2,3,77]
l2 = [1,2,5,77]
"""
l1=[1,2,3,77]
l2=[1,2,5,77]

b=True
if len(l1)==len(l2):
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            b=False
else:
    b=False
    
print(b)
# ------------ Q7 Write a program to flatten a nested list.

"""core logic 
    element ko pick karo 
    type check karo 
    if list then iterate again and add to list 
    else if not list add element
"""

l = [1, 2, [3,4],9,[4,5],99,[2,3,4,5]]
l2=[]
for element in l:
    if type(element) == list:
        for i in element:
            l2.append(i)
    else:
        l2.append(element)
print(l2)

# ------------ Q8 Write a program to rotate a list by n positions.
l=[1,2,3,4,5]
k = int(input()) % len(l)
for i in range(k):
    temp=0
    for j in range(len(l)-1):
        temp=l[j]
        l[j]=l[j+1]
        l[j+1]= temp

print(l)




# ------------ Q9 Write a program to find the cumulative sum of elements in a list.

"""
Cumulative sum means:
Each element becomes the sum of all previous elements including itself.
🔹 Example
Input:
l = [1, 2, 3, 4]
Output:
[1, 3, 6, 10]

"""
s=0
l2=[]
l = [1, 2, 3, 4]
for i in range(len(l)):
    s+=l[i]
    l2.append(s)
print(l2)
# ------------ Q10 Write a program to find the intersection of two lists.
"""bug"""
l1=[1,2,5,7,8]
l2=[1,2,3]
l3=[]

if len(l1)<len(l2):
    minx=l1
else:
    minx=l2

if len(l1)>len(l2):
    maxx= l1
else:
    maxx= l2
for i in range(len(minx)):
    if i in maxx:
        l3.append(i)
print(l3)

"""correct """
l1=[1,2,5,7,8]
l2=[1,2,3]

l3=[]

for i in l1:
    if i in l2:
        l3.append(i)

print(l3)
