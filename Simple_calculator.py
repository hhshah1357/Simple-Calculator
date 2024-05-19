#simple python calculator
def menu():
    #Ask the user for an input
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")

    #Convert to correct data type
    a = float(a)
    b = float(b)

    #Provide user with options
    print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
    """)

    #Receive operation number as an input
    operation = int(input("Enter the number for the desired operation: "))

    return a, b, operation



def calculation():
    a, b, operation = menu()
    if operation == 1:
        print("Sum: {} + {} = {}".format(a,b,a+b))
    elif operation == 2:
        print("Difference: {} - {} = {}".format(a,b,a-b))
    elif operation == 3:
        print("Product: {} * {} = {}".format(a,b,a*b))
    elif operation == 4:
        print("Power: {}^{} = {}".format(a,b,a**b))
    elif operation == 5:
        try:
            print("Quotient: {} / {} = {}".format(a,b,a/b))
        except:
            print("Division by 0 not possible!")
    elif operation == 6:
        try:
            print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
        except:
            print("Divsion by 0 not possible!")
    else:
        print("No such choice!")

    loop()



def loop():
    decide = input("Do you wish to continue? Y/N: ")
    if decide.upper() == "Y":
        calculation()
    elif decide.upper() == "N":
        print("Goodbye!")
    else:
        print("Invalid input!")
        loop()


        
#Run main function!
calculation()


