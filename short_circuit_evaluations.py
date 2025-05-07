# short circuit evaluations ~ in python logical operators are short circuit evaluations

high_income = False
good_credit = True
is_student = True

if high_income and good_credit and is_student:
    # The evaluation break in high_income itself
    print("Eligible for loan")

if good_credit or high_income:
    # The evaluation break in good_credit itself
    print("Eligible for loan")
