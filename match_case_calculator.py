#Prompts the user for two numbers and an operation, performs the calculation,
#and displays the result.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation +, -, *, /:" )

match operator:
    case "+":
        print("The result is" , num1 + num2)

    case "-":
        print("The result is" , num1 - num2)    

    case "*":
        print("The result is" , num1 * num2)

    case "/":
        if num2== 0:
            print("Please Cannot divide by zero")
        else:
            print("You entered the wrong operation") 



