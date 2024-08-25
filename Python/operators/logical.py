b = 3
a = 2
print(a and b)
print(a or b)
print(b and a)

# --------------
print(not a)
print(not 0)
print(not (True + True - (True - True)))
print(not  not a)


# And Truth Table
print("__" * 16)
print(f"| True   |  True  | {True and True}        |")
print(f"| True   |  False | {True and False}       |")
print(f"| False  | True   | {False and True}       |")
print(f"| False  | False  | {not (True and True)}       |")
print("__" * 16)


# And Truth Table
print("__" * 16)
print(f"| True   |  True  | {True or True}        |")
print(f"| True   |  False | {True or False}        |")
print(f"| False  | True   | {False or True}        |")
print(f"| False  | False  | {not (True or True)}       |")
print("__" * 16)


# And Truth Table
print("__" * 12)
print(f"| True  | {not True}        |")
print(f"| False | {not False}         |")
print("__" * 12)