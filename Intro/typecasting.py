
name = input ("Enter your name:")
age = int(input("Enter your age:"))

prize = 100
print(f"Your name is {name}")
age += 1
print(f"You are {age} years old")

if age >= 18:
    print("You are an adult")
    print(f"The ticket prize is {prize}")
elif age < 0:
    print("You havent been born yet!")
else:
    print("You are a child.")
    print(f"The ticket prize is {prize * 0.75}")

#OUTPUT
'''
Enter your name:Pavi
Enter your age:34
Your name is Pavi
You are 35 years old
You are an adult
The ticket prize is 100

Enter your name: Groot
Enter your age:3
Your name is Groot
You are 4 years old
You are a child.
The ticket prize is 75.0
'''
#Logical Operators
#OR = one of  the condition true
#AND = both conditions must be true
#NOT = if true inverts to false - does the opposite


