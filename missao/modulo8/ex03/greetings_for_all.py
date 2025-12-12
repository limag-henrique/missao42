#!/usr/bin/python3
def greetings(name = None):
    if isinstance(name, str) == True:
        print(f"Hello, {name}!")
    elif name == None:
        print("Hello, noble stranger!")
    else:
        print("Error! This is not a name!")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)