#i = 13
#while(12<i<19):
#    i = i +1
#    if i%2==0:
#        print(i)

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
def evens(num1 , num2):
    i=num1+1
    while(num1<i<num2-1):
        i = i +1
        if i%2==0:
            print(i)
            
evens(num1 , num2)

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
def evens(num1 , num2):
    
    while(num2-1>num1+1):
        
        if (num2-1)%2==0:
            print(num2)
        num2 -=1
            
evens(num1 , num2)

    