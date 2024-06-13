def fact(number):
    result=1
    if(number<0):
        print('factorial error')
    elif(number==0):
        print('factorial is 1')
    else:
        for i in range(1,number+1):
            result=number*=i
            return result


x=int(input("Enter a number:\n"))

print("Factorial is ",fact(x))
    
