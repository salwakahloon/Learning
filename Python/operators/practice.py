# plus operator
a:int = 10
b:int = 20
c = a + b
print(c) 

a:str = "hello"
print(a)

# minus operator
a:int = 40
b:int = 20
c = a - b
print(c)

# user input
a:int = int(input("enter your first value"))
b:int = int(input("enter your second value"))

# mul operator
print(a*b)
a =input("enter your first value: ")
b =input("enter your second value: ")
print(int(a) * int(b))
print("hello " * 10)

# div operator
a = 20
b = 0
# print(a/b)
print(b/a)
print(b//a)

# modulus
print(50 % 30)


# And truth table
print("__" * 16)
print(f"| True   |  True  | {True and True}        |")
print(f"| True   |  False | {True and False}       |")
print(f"| False  | True   | {False and True}       |")
print(f"| False  | False  | {not (True and True)}       |")
print("__" * 16)


# Or Truth table
print("__" * 12)
print(f"| True  | True  | {True or True}     |")
print(f"| True  | False | {True or False}     |")
print(f"| False | True  | {False or True}     |")
print(f"| false | false | {False or False}    |")
print("__" * 12)

# not Truth table
print("__" * 12)
print(f"| True  | {not True}        |")
print(f"| False | {not False}         |")
print("__" * 12)

a = 30
b = 45

print(a > b)
print( a < b)
print(a >= b)
print(a <= b)
print(a == b)












