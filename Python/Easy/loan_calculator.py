import sys
import math

mode = None
loan_principal = None           # P
annuity_payment = None          # A
number_of_payments = None       # n
loan_interest = None            # i
overpayment = None

for x in sys.argv:

    if "--type=" in x:
        mode = x.replace("--type=", "")
    if "--payment=" in x:
        annuity_payment = float(x.replace("--payment=", ""))
    if "--principal=" in x:
        loan_principal = float(x.replace("--principal=", ""))
    if "--periods=" in x:
        number_of_payments = int(x.replace("--periods=", ""))
    if "--interest=" in x:
        loan_interest = float(x.replace("--interest=", "")) / (12 * 100)

if len(sys.argv) < 5 or \
   loan_interest is None or \
   mode != "annuity" and mode != "diff" or \
   type == "diff" and annuity_payment or \
   (loan_principal is not None and loan_principal < 0 or \
   annuity_payment is not None and annuity_payment < 0 or \
   number_of_payments is not None and number_of_payments < 0 or \
   loan_interest is not None and loan_interest < 0):

    print("Incorrect parameters")

else:

    if mode == "diff":

        overpayment = -loan_principal

        for current_payment in range(1, number_of_payments + 1):

            differentiate_payment = loan_principal / number_of_payments + \
                loan_interest * (loan_principal - \
                (loan_principal * (current_payment - 1)) / number_of_payments)
            differentiate_payment = math.ceil(differentiate_payment)

            overpayment += differentiate_payment

            print(f"Month {current_payment}: payment is {differentiate_payment}")

    else:

        if loan_principal is None:

            loan_principal = annuity_payment / ((loan_interest * math.pow(1 + loan_interest, number_of_payments)) /
                                                (math.pow(1 + loan_interest, number_of_payments) - 1))
            loan_principal = math.floor(loan_principal)  # P

            print(loan_principal)

        elif number_of_payments is None:

            number_of_payments = math.log((annuity_payment /  # n
                (annuity_payment - loan_interest * loan_principal)), (1 + loan_interest))
            number_of_payments = math.ceil(number_of_payments)
            years = number_of_payments // 12
            months = number_of_payments % 12

            output_message = "It will take"
            if years:
                output_message += f" {years} year" if years == 1 else f" {years} years"
            if months and months != 12:
                output_message += f" and {months} month" if months == 1 else f" and {months} months"
            output_message += " to repay this loan!"

            print(output_message)

        elif annuity_payment is None:

            annuity_payment = loan_principal * loan_interest * math.pow(1 + loan_interest, number_of_payments) / \
                              (math.pow((1 + loan_interest), number_of_payments) - 1)
            annuity_payment = math.ceil(annuity_payment)  # A

            print(f"Your monthly payment = {annuity_payment}!")

        overpayment = annuity_payment * number_of_payments - loan_principal

    print(f"\nOverpayment = {overpayment}")