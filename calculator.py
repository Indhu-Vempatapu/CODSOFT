#Defining function to perform addition operation
def add(x,y):
    return x+y

#Defining function to perform subtraction operation
def subtract(x,y):
    return x-y

#Defining function to perform multiplication operation
def multiply(x,y):
    return x*y

#Defining function to perfrom division operation
def divide(x,y):
    return x/y

#Defining function to perform floordivision operation
def modulo_div(x,y):
    return x%y

print("Select Operation:")
print("1.Addition(+):") 
print("2.Subtraction(-):")
print("3.Multiplication(*):")
print("4.Division(/):")
print("5.ModuloDivision(%)")
print("\n")

while True:
    #Taking input from the user
    user_choice=input("Enter  your choice:")

    #To check the user choice is one among five
    if user_choice in ('1','2','3','4','5'):
      
      #Taking input numbers from the user
      num1=float(input("Enter first number:"))
      num2=float(input("Enter second number:"))

      if user_choice=='1':
          #Addition Operation
          print(num1,"+",num2,"=",add(num1,num2))
          print("\n")

      elif user_choice=='2':
          #Subraction Operation
          print(num1,"-",num2,"=",subtract(num1,num2))
          print("\n")

      elif user_choice=='3':
          #Multiplication Operation
          print(num1,"*",num2,"=",multiply(num1,num2))
          print("\n")

      elif user_choice=='4':
          #Division Operation
          if num2==0:
              print("Division by zero is not possible")
              print("\n")
          else:
              print(num1,"/",num2,"=",divide(num1,num2))
              print("\n")    

      elif user_choice=='5':
          #Modulo Division Operation
          print(num1,"%",num2,"=",modulo_div(num1,num2))
          print("\n")        
          
      next_calculation=input("Do you want to continue ? [yes/no]:")

      if next_calculation=="no":
           break
    else:
          print("Wrong Choice")
    