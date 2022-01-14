#A program written in Python that calculates the mortgage payments over the payment term
#It asks the user to input the payment term, the principal and the interest rate and if he/she would like anniversary payments
#The program outputs the month and the remaining principal in that month, it also prints out the anniversay payments if chosen "yes"
#It prints out the total cost of mortgage, the total monthly payments, the total interest payments, and total aniversay payments if made
#First portion of code used from classroom example. The insturctions said you are allowed to use the classroom example. 
# by Matthew Mamelak for CISC101

def main():
    # Obtain inputs from the user and check to see if the inputs fall within the bounds
    # Asks user for Payment Term in years
    inputOK = False
    while not inputOK :
        try :
            paymentTerm = int(input("Enter payment term in years: "))
            if paymentTerm < 1 or paymentTerm > 30 :
                print("Input must be between 1 and 30. Please try again")
            else :
                inputOK = True
        except ValueError :
            print("You did not enter a number, please try again.")
            
    # Asks user for Annual interest rate
    inputOK = False
    while not inputOK :
        try :
            annualInterestPercent = float(input("Enter annual interest rate as %: "))
            if annualInterestPercent < 1 or annualInterestPercent > 10 :
                print("Input must be between 1 and 10. Please try again")
            else :
                inputOK = True
        except ValueError :
            print("You did not enter a number, please try again.")

    # Asks user for Principal
    inputOK = False
    while not inputOK :
        try :
            principal = float(input("Enter principal amount in $: "))
            if principal < 1000 or principal > 500000 :
                print("Input must be between 1000 and 500000. Please try again")
            else :
                inputOK = True
        except ValueError :
            print("You did not enter a number, please try again.")

    # Calculate the monthly payment and total interest
    termInMonths = 12 * paymentTerm
    monthlyInterestRate = annualInterestPercent / 1200
    monthlyPayment = principal * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** -termInMonths)
    totalInterest = termInMonths * monthlyPayment - principal

    # Display the calculated results to two decimal places
    print("\nMonthly payment is ${0:.2f}".format(monthlyPayment))
    
    # Asks  user if he/she would like to make anniversary payments
    userAnswer = str(input("Enter 'y' to make anniversary payments, 'n' otherwise: "))
    counter = 1
    #If user chooses not to make anniversary payments
    if userAnswer == "n":
        interestTotal = 0
        while counter <= termInMonths : #While loop that will run until the counter = total paymnt term 
            monthlyInterest = monthlyInterestRate * principal #Calculates monthly interest payment
            remainingPrincipal = monthlyPayment - monthlyInterest #Calculates remaining principal after monthly payment and interest
            if remainingPrincipal > principal:
                principal = 0
            else:
                principal = principal - remainingPrincipal 
            print("Month:", counter, "  Principal: $ {:.2f}".format(round(principal, 2))) #Prints the Month, and the principal at that given month
            counter += 1
            interestTotal = monthlyInterest + interestTotal #Calculation for the total interest over the entire payment term
        print(35 * "_")
        print("Total interest payments: $ {:.2f}".format(round(interestTotal, 2)))
        monthlyTotal = termInMonths * monthlyPayment #Calculates the monthly total payment and mortgage total payment
        print("Total monthly payments: $ {:.2f}".format(round(monthlyTotal, 2)))
        print("Total cost of mortgage: $ {:.2f}".format(round(monthlyTotal, 2)))
    #If user chooses to make anniversary payments       
    elif userAnswer == "y":
        #Declaring variables for later calculations (Total Interest, Mortgage Total...)
        AniversaryPayment = 5000 
        AniversaryTotal = 0
        interestTotal = 0
        monthlyTotal = 0
        mortgageTotal = principal
        while principal > 0:
            monthlyInterest = monthlyInterestRate * principal #Calculates monthly interest payment
            remainingPrincipal = monthlyPayment - monthlyInterest #Calculates remaining principal after monthly payment and interest
            if remainingPrincipal > principal:
                principal = 0
            else:
                principal = principal - remainingPrincipal
            print("Month:", counter, "  Principal: $ {:.2f}".format(round(principal, 2)))

            if counter % 12 == 0: #Checks to see if the counter (the current month) is divisble by 12 with no remained
                if principal < 100000: #If statement if the principal is less than 100000
                    AniversaryPayment = principal * 0.05 #Calculates aniversary payment at that given month 
                    principal = principal - AniversaryPayment #Calculates new princial after aniversary payment is made
                elif AniversaryPayment > principal:
                    principal = 0
                else: #else statement if the principal is greater than 100000 
                    principal = principal - AniversaryPayment #Calculates new princial after aniversary payment is made
                print ("Anniversary payment: $ {:.2f}".format(round(AniversaryPayment, 2)), "Remaining principal: ${:.2f}".format(round(principal, 2)))
                AniversaryTotal = AniversaryPayment + AniversaryTotal #AniversaryTotal variable stores all aniversary payments
            counter += 1 
            counter1 = counter - 1
            months_saved = termInMonths - counter1 #Determines how many months were saved by implementing aniversary payments
            interestTotal = monthlyInterest + interestTotal #interestTotal variable stores all monthly interest payments
        print(35 * "_")
        mortgageTotal = interestTotal + mortgageTotal #mortgageTotal variable stores the principal and the total interest payment
        monthlyTotal = mortgageTotal - AniversaryTotal #Calculates monthly payments based on mortgage total and aniversary total
        print("Paid mortgage off", months_saved, "months early.") #Prints out how many motnhs were saved used aniversary payments
        #Prints out total cost of mortgage, interest payments, monthly payments and anniversary payments
        print("Total anniversary payment: $ {:.2f}".format(round(AniversaryTotal, 2)))
        print("Total interest payments: $ {:.2f}".format(round(interestTotal, 2)))
        print("Total monthly payments: $ {:.2f}".format(round(monthlyTotal, 2)))
        print("Total cost of mortgage: $ {:.2f}".format(round(mortgageTotal, 2)))
        
    else:
        print("Input invalid.")
        

main()


