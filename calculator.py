print("*****OPERATORS*****")
print("1 = Add")
print("2 = Subtract")
print("3 = multiply")
print("4 = divide")
print("5 = Show previous equations")
print("0 = Exit")

user_input = input("please enter your option :")

while user_input != "0": # loop until user enters 0
    if user_input == "1" :
        try :
            num1 = float (input("please enter first number :" ))
            num2 = float (input ("please enter second number"))
            result = num1 + num2
            print("The sum is :" + str(result))
            file = open('equation.txt','a')
            file.write (str(num1) + " + " + str(num2) + " = " + str(result) + "\n")
            file.close ()
        except ValueError :
            print("invalid input,please enter a valid number. ")
    elif user_input == "2" :
        try :
            num1 = float (input("please enter first number :" ))
            num2 = float (input ("please enter second number"))
            result = num1 - num2
            print("The difference is :" + str(result))
            file = open('equation.txt','a')
            file.write (str(num1) + " - " + str(num2) + " = " + str(result) + "\n")
            file.close ()
        except ValueError :
            print("invalid input, please enter a valid number.")
    elif user_input == "3" :
        try :
            num1 = float (input("please enter first number :" ))
            num2 = float (input ("please enter second number"))
            result = num1 * num2
            print("The product is :" + str(result))
            file = open('equation.txt','a')
            file.write (str(num1) + " * " + str(num2) + " = " + str(result) + "\n")
            file.close ()
        except ValueError :
            print("invalid input ,please enter a valid number.")
    elif user_input == "4" :
        try :
            num1 = float (input("please enter first number :" ))
            num2 = float (input ("please enter second number"))
            result = num1 / num2
            print("The result is :" + str(result))
            file = open('equation.txt','a')
            file.write (str(num1) + " / " + str(num2) + " = " + str(result) + "\n")
            file.close ()
        except ValueError :
            print("invalid input, please enter a valid number.")
        except ZeroDivisionError:
            print("invalid input, cannot divide by zero.")
    elif user_input == "5":
        try:
            file = open('equation.txt','r')
            lines = file.readlines()
            print("The previous equations are:")
            for line in lines:
                print(line.strip())
            file.close()
        except FileNotFoundError:
            print("No previous equations found.")

    else :
        print ("invalid choice,please try again.")

    user_input = input("please enter your option :")

print("goodbye!")



