from os import times_result

has_high_income = False
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

    '''Condition= if applicant has high income or good credit, then eligible for loan
    Condition= if applicant has high income and good credit, then eligible for loan
    AND= both conditions must be true
    OR= at least one condition must be true
    NOT= negates the condition,means reverse the boolean value (if it's true then it will read false)'''

    has_good_credit = True
    has_criminal_record = True

    if has_good_credit and not has_criminal_record:
        print("Eligible for loan")
