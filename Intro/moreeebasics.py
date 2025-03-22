#While loop
name = input("Enter your name:")
while name == "":
    print("Enter your name:")

age = int(input("Enter your age:"))
while age < 0:
    print("Age cannot be less than 0.")
    age = int(input("Enter your age:"))

print(f"Hello {name}!")
print(f"Your age is {age}")

#For loop
for i in range(10):
    print(i)
for o in range(1,12,2):
    print(o)


for l in name:
    print(l)

import time
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!!")

#OUTPUT
'''
Enter your name:Pavithra
Enter your age:17
Hello Pavithra!
Your age is 17
0
1
2
3
4
5
6
7
8
9
1
3
5
7
9
11
P
a
v
i
t
h
r
a
10
9
8
7
6
5
4
3
2
1
Happy New Year!!
'''

#List - mutable & flexible
fruits = ["apple","orange","banana","cherry"]

for fruit in fruits:
    print(fruit, end= " ")

#Tuple - immutable
fruits = ("apple","orange","banana","cherry")

#Sets - mutable unordered no duplicated allowed
f = {"apple","orange","banana","cherry"}
fruit = input("Enter fruit name to search: ")
if  fruit in f:
    print(f"{fruit} is in stock")
else:
    print(f"{fruit} is not in stock")

#OUTPUT
'''
apple orange banana cherry 
Enter fruit name to search: peach
peach is not in stock
'''
