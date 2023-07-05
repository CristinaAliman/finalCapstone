import math

# Declare the value of one pound in pence to be used for conversion
POUND_CONVERTER = 100
PERCENTAGE_CONVERTER = 100

# The user is asked to chose which type of investment calculation they want to do
inv_type = input(f'''investment - to calculate the amount of interest you'll earn on your investment 
\nbond - to calculate the amount you will have to pay on a home loan
\nEnter either 'investment' or 'bond' from the menu above to proceed: ''').lower()

if inv_type == "investment":
    # The user is asked to input the variables required to perform the 
    # investment calculation (amount, interest, number of years and interest type)
    try:
        dep_amount = float(input("Enter the amount i you want to deposit in £: "))*POUND_CONVERTER
        int_rate = float(input("Enter the interest rate as a number without % (examples: 2, 0.3, 1.2): "))/PERCENTAGE_CONVERTER
        years = int(input("Enter the number of years you want to invest your money for as a number: "))
    except ValueError: 
        print("Please try again and enter a number.")
        exit(1)
    
    # User is asked to input interest type (simple/compound)
    int_type = str(input(f"Enter the type of interest for your deposit (simple / compound): ")).lower()

    # Calculates final amount for simple interest, converts to £ and prints the output  
    if int_type == "simple": 
        total_simple = float(dep_amount * (1 + int_rate * years))/POUND_CONVERTER
        print(f"You're final amound after {years} years will be: £{total_simple}")
    
    # Calculates final amount for compound interest, converts to £ and prints the output  
    elif int_type == "compound": 
        total_compound = float(dep_amount * math.pow((1 + int_rate), years))/POUND_CONVERTER
        print(f"You're final amound after {years} years will be: £{total_compound}")

elif inv_type == "bond": 
    # asks the user to input the house value, interest rate and no of repayment months 
    # to calc monthly payments
    try:
        house_value = float(input("Enter the house value in £: "))
        monthly_int_rate = int(input("Enter the interest rate: "))/PERCENTAGE_CONVERTER
        months = int(input("The number of months you plan to repay the bond: "))
    except ValueError: 
        print("Please try again and enter a number")
        exit(1)

    # Calculates and prints the monthly repayment value based on user input
    monthly_payment = (house_value * (monthly_int_rate))/(1 - (1 + monthly_int_rate)**(-months))
    print(f"The amount you need to repay each month is: £{monthly_payment}")
