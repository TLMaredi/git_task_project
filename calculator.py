# Print the menu of operations
print("*****OPERATORS*****")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("5 = Show previous equations")
print("0 = Exit")

# Prompt the user to enter an option from the menu
user_input = input("Please enter your option: ")

# Start a loop that continues until the user enters '0'
while user_input != "0":
    # If the user chooses '1', perform addition
    if user_input == "1":
        try:
            # Prompt the user to enter the first and second number
            number1 = float(input("Please enter the first number: "))
            number2 = float(input("Please enter the second number: "))
            # Calculate the sum
            result = number1 + number2
            # show the result
            print("The sum is: " + str(result))
            # Open the 'equation.txt' file in append mode
            with open('equation.txt', 'a') as file:
                # Write the equation to the file
                file.write(str(number1) + " + " + str(number2) + " = " + str(result) + "\n")
        
        except ValueError:
            print("Invalid input, please enter a valid number.")
    # If the user chooses '2', perform subtraction
    elif user_input == "2":
        try:
            # Similar structure as the '1' case, but for subtraction
            number1 = float(input("Please enter the first number: "))
            number2 = float(input("Please enter the second number: "))
            # Calculate the difference
            result = number1 - number2
            # Display the result
            print("The difference is: " + str(result))
            # Open the 'equation.txt' file in append mode
            with open('equation.txt', 'a') as file:
                # Write the equation to the file
                file.write(str(number1) + " - " + str(number2) + " = " + str(result) + "\n")
        except ValueError:
            print("Invalid input, please enter a valid number.")
    # If the user chooses '3', perform multiplication
    elif user_input == "3":
        try:
            # Similar structure as the '1' case, but for multiplication
            number1 = float(input("Please enter the first number: "))
            number2 = float(input("Please enter the second number: "))
            # Calculate the product
            result = number1 * number2
            # Display the result
            print("The product is: " + str(result))
            # Open the 'equation.txt' file in append mode
            with open('equation.txt', 'a') as file:
                # Write the equation to the file
                file.write(str(number1) + " * " + str(number2) + " = " + str(result) + "\n")
        except ValueError:
            print("Invalid input, please enter a valid number.")
    # If the user chooses '4', perform division
    elif user_input == "4":
        try:
            # Similar structure as the '1' case, but for division
            number1 = float(input("Please enter the first number: "))
            number2 = float(input("Please enter the second number: "))
            if number2 == 0:
                # Handle the ZeroDivisionError
                print("Cannot divide by zero, please enter a non-zero number.")
            else:
                # Calculate the answer
                result = number1 / number2
                # Display the result
                print("The quotient is: " + str(result))
                # Open the 'equation.txt' file in append mode
                with open('equation.txt', 'a') as file:
                    # Write the equation to the file
                    file.write(str(number1) + " / " + str(number2) + " = " + str(result) + "\n")
        except ValueError:
            print("Invalid input, please enter a valid number.")
    # If the user chooses '5', display previous equations
    elif user_input == "5":
        try:
            # Open the 'equation.txt' file in read mode
            with open('equation.txt', 'r') as file:
                # Read all lines from the file
                lines = file.readlines()
                print("The previous equations are:")
                # Loop through each line and print it
                for line in lines:
                    print(line.strip())
        # Handle the error if 'equation.txt' does not exist
        except FileNotFoundError:
            print("No previous equations found.")
    # If the user enters an invalid choice, prompt them to try again
    else:
        print("Invalid choice, please try again.")

    # Ask the user to enter another option or exit
    user_input = input("Please enter your option: ")

# Print a goodbye message when the user exits the loop
print("Goodbye!")

   
           
