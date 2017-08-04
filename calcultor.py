print("welcome")
n1 = input("enter the first number")
operator = input("division, multiplication,addition,subtraction,exponential, modulus")
n2 = input("enter the second number")

n1 = float(n1)
n2 = float(n2)

if (operator == 'division'):
    print(n1 / n2)
elif (operator == 'multiplication'):
    print(n1 * n2)
elif (operator == 'subtraction'):
    print(n1 - n2)
elif (operator == 'addition'):
    print(n1 + n2)
elif (operator == 'exponentiation'):
    print(n1 ** n2)
elif (operator == 'modulus'):
    print(n1 % n2)



# exponentiation - **
# modulus (or remainder) - %