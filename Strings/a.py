# 1. Write a program to find the length of a string without using `len()`.
# 2. Write a program to check if two strings are anagrams.
# 3. Write a program to remove vowels from a string.
# 4. Write a program to count the number of words in a string.
# 5. Write a program to replace all spaces with underscores in a string.
# 6. Write a program to find the longest word in a sentence.
# 7. Write a program to check if a string contains only digits.
# 8. Write a program to remove the punctuation from a string.

# 1. Write a program to find the length of a string without using `len()`.

a="appleed23424f%"
c=0
for i in a:
    c+=1
print(c)


# 2. Write a program to check if two strings are anagrams.
s1=input()
s2=input()

"""b=True
if len(s1)==len(s2):
    for i in s1:                --- this is useless in code -- Because dictionary frequency comparison already handles this.
        if i not in s2:
            b=False"""
if len(s1)!=len(s2):
     print("not anagram ")
    
d1={}
d2={}
for i in s1:
        if i in d1:
            d1[i]+= 1
        else:
            d1[i]= 1

for j in s2:
        if j in d2:
            d2[j]+=1
        else:
            d2[j]=1
      
if d1 == d2:
    print("anagram")
else:
    print("not anagram")


""" problem 1
 b=True is reset again and again in the loop.
    Example:
s1 = "rat"
s2 = "car"
Loop steps:
i	i in s2	b
r	yes	True
a	yes	True
t	no	False
But if the last character matched, it could wrongly become True.

problem 2

Issue 2

It does not check frequency.
Example:
s1 = "aab"
s2 = "abb"
Your code will return True, but it is not an anagram.
"""


"""
Basic logic 
s1 = "aab"
s2 = "bba"

d1={}
d2={}
for i in s1:
    if i in d1:
        d1[i]+= 1
    else:
        d1[i]= 1

for j in s2:
    if j in d2:
        d2[j]+=1
    else:
        d2[j]=1
---------------------------------------above the we are checking the freq from both the string by using dict-----------------------------------------------------------------------------------------      

print(d1)
print(d2)

--------------------------------------------shortcut way od checking the keys and value of two dict ------------------------------------------
--------------------------------------task see how this will work
print(d1==d2)


----------------------naive method to check keys and value in two dict -------------------------------------------------------
b=True
for i in d1:
    if i not in d2 or d1[i]!=d2[j]:
        b=False
    print(b)
"""


# 3. Write a program to remove vowels from a string.
a="aeiouvbnmlkjh"
v="aeiou"
for i in a:
    if i not in v:
        print(i,end="")


# 4. Write a program to count the number of words in a string.
"""use case of boolean value logic """
a="ram is a boy"
c=0
inward = False
for i in a:
    if i !=" " and inward==False:
        c+=1
        inward = True
    elif i== " ":
        inward= False
print(c)
        
# 5. Write a program to replace all spaces with underscores in a string.
a="ram is a boy "
b=""
for i in a:
    if i ==" ":
        i="__"
        b+=i
    else:
        b+=i
print(b)

# 6. Write a program to find the longest word in a sentence.
s="my name is rohit kumar"
l=s.split()

lar=s[0]
for i in range(len(l)):
    if l[i]>lar:
        lar = l[i]
print(lar)


"""correct version"""

s = "my name is rohit kumar"
l = s.split()

lar = l[0]
for word in l:
    if len(word) > len(lar):
        lar = word
print(lar)
# 7. Write a program to check if a string contains only digits.

a="111%vvsh12345"
b=True
for i in a:
    if not ('0' <= i<='9') :
        b=False
        
print(b)

# 8. Write a program to remove the punctuation from a string.
a="1292,02 # 3i409c jie !!!"
for i in a:
    if i.isalnum()or i==" ":
        print(i,end="") 