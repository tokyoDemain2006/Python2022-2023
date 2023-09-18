print ("Calculator")
import random
number1=int(input("enter 1st numb:"))
number2=int(input("enter 2nd numb:"))
list1 = ["+","-","*","/"]
operator = random.choice(list1)

if operator=="+":
    print("the operator used was add")
    answer=number1+number2
elif operator=="-":
    print("the operator used was minus")
    answer=number1-number2
elif operator=="*":
    print("the operator used was multiply")
    answer=number1*number2
elif operator=="/":
    print("the operator used was divide")
    answer=number1/number2 
print("answer="+str(answer))

        
