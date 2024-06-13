def add(a,b):
    print("Addition is"  ,a+b)

def subtract(a,b):
    print("Subtraction is ", a-b)

def multiply(a,b):
    print("Multiplication is ", a*b)

def divide(a,b):
    print("Division is ", a/b)

'''
def modulus(a,b):
    print("Modulus is ", a%b)

def exponentiation(a,b):
    print("Exponentiation is ",a**b)

def floor division(a,b):
    print("Floor division is ", a//b)
'''

while True:
    print('1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit')
    n=int(input("Enter your choice: "))
    
    if n==1:
        num1=int(input("Enter number 1:"))
        num2=int(input("Enter number 2:"))
        add(num1,num2)

    elif n==2 :
        num1=int(input("Enter number 1:"))
        num2=int(input("Enter number 2:"))
        subtract(num1,num2)

    elif n==3:
        num1=int(input("Enter number 1:"))
        num2=int(input("Enter number 2:"))
        multiply(num1,num2)

    elif n==4:
        num1=int(input("Enter number 1:"))
        num2=int(input("Enter number 2:"))
        divide(num1,num2)

    elif n==5:
        print("Exit")
        break

    else:
        print("Invalid input")
