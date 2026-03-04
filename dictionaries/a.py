""" # ------------ Q4 Write a program to sort a dictionary by its values. 
    # ------------ Q9 Write a program to count the frequency of characters in a string using a dictionary.

3 times 

Dictionary creation
Update
Delete
Merge
Sorting
Frequency problems
Inversion
Comparison
"""

# ------------ Q1 Write a program to create a dictionary from two lists.
# ------------ Q2 Write a program to merge two dictionaries.
# ------------ Q3 Write a program to check if a key exists in a dictionary.
# ------------ Q4 Write a program to sort a dictionary by its values. 
# ------------ Q5 Write a program to add a new key-value pair to a dictionary.
# ------------ Q6 Write a program to delete a key from a dictionary. 
# ------------ Q7 Write a program to find the maximum and minimum value in a dictionary.
# ------------ Q8 Write a program to invert a dictionary (swap keys and values).
# ------------ Q9 Write a program to count the frequency of characters in a string using a dictionary.
# ------------ Q10 Write a program to find the common keys in two dictionaries.


# ------------ Q1 Write a program to create a dictionary from two lists.

a=[4,5,6,7,8,10]
b=[1,2,3,4,5]

minxx = min(len(a),len(b))

d={}
for i in range(minxx):
        d[a[i]] = b[i]
        
print(d)

# ------------ Q2 Write a program to merge two dictionaries.
d1={'a':1,'b':2,'c':3,'d':4}
d2 ={1:'a',2:'b',3:'c',4:'d'}
d={}
# """ mth1 """
for k,v in d1.items():
    d[k]= v
    
for k,v in d2.items():
    d[k]=v
print(d)

# """ mth2 """
for i in d1:
    d[i]=d1[i]

for j in d2:
    d[j]=d2[j]
print(d)

# ------------ Q3 Write a program to check if a key exists in a dictionary.

d1={'a':1,'b':2,'c':3,'d':4}
key=input("enter the key:" )
b=False
for i in d1:
    if i == key:
       b=True

if b == True:
    print("keys exists")
else:
    print("keys don't exists")

# ------------ Q4 Write a program to sort a dictionary by its values.


d1={'a':8,'b':1,'c':9,'d':5,'e':3,'f':4}
print("before sorted",d1)
l=[]
d2={}
for i,j in d1.items():
    l.append((i,j))

for  i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i][1]>l[j][1]:
            temp = l[i]
            l[i]=l[j]
            l[j]=temp

for m,n in l:
    d2[m]=n
print("after sorted",d2)

# ------------ Q5 Write a program to add a new key-value pair to a dictionary.
d={'a':1,'b':2,'c':3,'d':4}
key = input()
value = int(input())
d[key]=value
print(d)

# ------------ Q6 Write a program to delete a key from a dictionary.

#   1.  Using del keyword
#         del d[key]
#     2.  Using pop() method
#         pop() also removes the key

#     3. d = {'a': 10, 'b': 20, 'c': 30}
#         d.popitem()
#         Removes the last inserted key-value pair

d={'a':1,'b':2,'c':3,'d':4}

"""mth 1"""
key = input()
del d[key]
print(d)

"""mth2 """

 

# ------------ Q7 Write a program to find the maximum and minimum value in a dictionary.
d={'a':1,'b':2,'c':3,'d':4}
maxx=d['a']
minx=d['a']

for i in d:
    if d[i]>maxx:
        maxx=d[i]

    if d[i]<minx:
        minx=d[i]
print("max value",maxx) 
print("min value",minx)


# ------------ Q8 Write a program to invert a dictionary (swap keys and values).
d={'a':1,'b':2,'c':3,'d':4}

new_dic ={}
for k,v in d.items():
    new_dic[v]=k
print(new_dic)

# ------------ Q9 Write a program to count the frequency of characters in a string using a dictionary.
s="abcdabcd"
d={}
c=0
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

# ------------ Q10 Write a program to find the common keys in two dictionaries.
d1={'a':1,'b':2,'v':3,'d':4}
d2={'g':1,'n':2,'v':3,'a':4,'h':0}

v=[]
for i in d2:
    if i in d1:
        v.append(i)
print(v)