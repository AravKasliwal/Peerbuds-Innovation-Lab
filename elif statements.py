#class group A 8-19 b 19-23
age = int(input("What is your age?"))

if age >= 8 and age <= 19:
    print("Elif you will be in class A")
elif age >= 19 and age <= 23:
    print("Elif you will be in class B")
else:
    print("If you are ot 8-23 you are not elegible to be in any of our classes")
