# logical operators ~ and, or, not

high_income = True
good_credit = True
is_not_student = False

if not is_not_student:
    if high_income and good_credit:  # if (high_income && good_credit) {} in js
        print("You are eligible for the loan")
    else:
        print("You are not eligible for the loan")
else:
    print("You must be a student to apply for this loan")


def ask_yes_no_question(question):
    while True:
        answer = input(question + " (y for Yes / n for No): ").strip().lower()
        if answer in ['y', 'n']:
            # if answer == "x" or answer == "y"
            return answer
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")


print("Please answer with y (Yes) or n (No)")

is_income_high = ask_yes_no_question("Is your income higher than 12K?")
is_credit_good = ask_yes_no_question("Is your credit good?")
is_student = ask_yes_no_question("Are you a student?")

if is_student:
    if is_income_high == "y" and is_credit_good == "y":
        print("You are eligible for the loan")
    else:
        print("You are not eligible for the loan")
else:
    print("You must be a student to apply for this loan")
