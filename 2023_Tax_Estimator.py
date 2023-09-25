class tax_calc ():

    button = "Calculate refund"
    title = """
    2023 Federal Tax Calculator and Refund Estimator.
    """
    content = """
    Answering a few questions about your life, income
    and expenses with our tax calculator will answer the
    questions we all want answers to: Will I get a refund
    or owe the IRS? How much?
    """
    print(title)
    print(content)
    print(button)
    print("=======================================")

    user_responses = {}

    # Q1 filing status
    question1 = "Are you single or married?"
    explain1 = "This will help us determine your filing status, standard deduction, and which credits you can claim."
    print(question1)
    print(explain1)
    print("1. Single")
    print("2. Married")

    # saved in dic
    user_input1 = input("Please enter the number corresponding to your choice: ")

    if user_input1 == "1":
        user_responses["marital_status"] = "Single"
    elif user_input1 == "2":
        user_responses["marital_status"] = "Married"
    else:
        print("Invalid choice. Please enter 1 for Single or 2 for Married.")
        exit()  #exit 

    # Q2 Hoh
    question2 = "Are you the head of household?"
    explain2 = "Head of Household is a filing status for unmarried persons with a qualified person."
    print(question2)
    print(explain2)
    print("1. Yes")
    print("2. No")

    # Q2
    user_input2 = input("Please enter the number corresponding to your choice: ")

    if user_input2 == "1":
        user_responses["head_of_household"] = "Yes"
    elif user_input2 == "2":
        user_responses["head_of_household"] = "No"
    else:
        print("Invalid choice. Please enter 1 for Yes or 2 for No.")

    # Q3 age
    question3 = "Enter your age as of Jan 1, 2023."
    explain3 = "This helps us determine which age-specific tax breaks you might qualify for."
    print(question3)
    print(explain3)


    user_age = input("Please enter your age as of Jan 1, 2023: ")
    user_responses["age_as_of_2023"] = user_age

    # Q4 w2 income
    question4 = "Do you have your W-2(s) on hand?"
    explain4 = "Select Yes to enter each W-2 separately. Otherwise, select No to enter the amount, or estimate in aggregate."
    print(question4)
    print(explain4)
    print("1. Yes")
    print("2. No")


    w2_input = input("Please enter the number corresponding to your choice: ")

    if w2_input == "1":
        user_responses["has_w2"] = "Yes"
    elif w2_input == "2":
        user_responses["has_w2"] = "No"
    else:
        print("Invalid choice. Please enter 1 for Yes or 2 for No.")

    question5 = "Enter your W-2 info."
    explain5 = "Enter employment income and federal withholdings for each W-2 you received this year."
    print(question5)
    print(explain5)

    jobs = []
    while True:
        job_info = {}
        job_info["wages"] = input("Wages, tips, other compensation (Box 1): ")
        job_info["withheld"] = input("Federal income taxes withheld (Box 2): ")
        job_info["state_tax"] = input("State income tax (W-2 box 17): ")
        jobs.append(job_info)

        another_job = input("Add another job? (yes/no): ")
        if another_job.lower() != "yes":
            break

    user_responses["w2_info"] = jobs

    #calc refund
    print("Here's your estimated refund so far.")
    print("$321")
    print("""
    Your estimate is based on what you've told us to this point. Want a more
    accurate number? Answer a few more questions about your income and
    expenses. You can also save and finish up later.
    """)
    print("Ready to make that refund a reality? You can file your taxes now.")
    print("1. Start your taxes")
    print("2. Next")
    input()

    # dependents credits
    question6 = "Do you have dependents?"
    explain6 = "Enter any qualifying children, relatives, or household members whom you support financially and plan to claim."
    print(question6)
    print(explain6)
    print("Your estimated federal refund:\t$122")
    print("1. Yes")
    print("2. No")

    dependents_input = input("Please enter the number corresponding to your choice: ")

    if dependents_input == "1":
        user_responses["has_dependents"] = "Yes"
    elif dependents_input == "2":
        user_responses["has_dependents"] = "No"
    else:
        print("Invalid choice. Please enter 1 for Yes or 2 for No.")

    question7 = "Tell us about your dependents."
    explain7 = """
    This helps us determine which dependent-related tax breaks you might
    qualify for (Child and Dependent Care Credit, Elderly and Disabled Tax
    Credit, EITC, Lifetime Learning Credit, Tuition Deduction etc.).
    """
    print(question7)
    print(explain7)

    dependents_info = []

    while True:
        dependent_info = {}
        dependent_info["age"] = input("Dependent's age as of Jan 1, 2023: ")

        print("Choose one for the dependent:")
        print("1. Student")
        print("2. Disabled")
        print("3. Dependent lives with me")
        choice = input("Please enter the number corresponding to your choice: ")

        if choice == "1":
            dependent_info["status"] = "Student"
        elif choice == "2":
            dependent_info["status"] = "Disabled"
        elif choice == "3":
            dependent_info["status"] = "Dependent lives with me"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        dependents_info.append(dependent_info)

        add_another = input("Add another dependent (yes/no): ")
        if add_another.lower() != "yes":
            break


    user_responses["dependents_info"] = dependents_info

    # estimate 2023 based on 2022 incomes
    question8 = "Choose all 2022 income that you received."
    explain8 = """
    If you don't see your source of income listed here, choose None apply. This
    refund estimator accounts for the most common tax situations, but H&R Block
    can help with all income -- no matter how unique or complex.
    """
    print(question8)
    print(explain8)

    #income types
    income_types = []
    print("Choose the income types you received (enter numbers separated by spaces):")
    print("1. Unemployment")
    print("2. Combat pay")
    print("3. Social security")
    print("4. Investments")
    print("5. Business or other")
    print("6. None apply")

    income_choices = input("Enter the numbers corresponding to your income types (e.g., '1 2 3'): ")

    income_choices = income_choices.split()  

    for choice in income_choices:
        if choice == "1":
            income_types.append("Unemployment")
        elif choice == "2":
            income_types.append("Combat pay")
        elif choice == "3":
            income_types.append("Social security")
        elif choice == "4":
            income_types.append("Investments")
        elif choice == "5":
            income_types.append("Business or other")
        elif choice == "6":
            income_types.append("None apply")
        else:
            print("Invalid choice. Please enter valid numbers.")


    user_responses["income_types"] = income_types

    # other incomes
    question9 = "Enter all 2022 unemployment income."
    explain9 = """
    This is the total amount of unemployment benefits you (and your spouse)
    received in 2022. Don't include any workers' compensation or disability
    payments.
    """
    print(question9)
    print(explain9)

    # if have 1099G - unemployment income
    unemployment_info = []

    while True:
        unemployment_entry = {}
        unemployment_entry["total_unemployment_income"] = input("2022 total unemployment (1099-G, Box 1): ")
        unemployment_entry["federal_withheld"] = input("Federal income taxes withheld (1099-G, Box 4): ")
        unemployment_entry["state_withheld"] = input("State income tax withheld (1099-G, Box 11): ")

        unemployment_info.append(unemployment_entry)

        add_another_1099g = input("Add another 1099-G (yes/no): ")
        if add_another_1099g.lower() != "yes":
            break


    user_responses["unemployment_info"] = unemployment_info

    # NT
    question10 = "Enter all 2022 nontaxable combat pay."
    explain10 = """
    This is the total amount of nontaxable combat pay you (and your spouse)
    received in 2022. You can find this on your W-2, Box 12, Code Q.
    """
    print(question10)
    print(explain10)


    combat_pay_info = {}

    combat_pay_info["total_nontaxable_combat_pay"] = input("2022 total nontaxable combat pay (W-2, Box 12, Code Q): ")

    nontaxable_combat_pay_choice = input("Include my nontaxable combat pay in my earned income credit calculation? (yes/no): ")
    if nontaxable_combat_pay_choice.lower() == "yes":
        combat_pay_info["include_in_eic_calculation"] = "Yes"
    else:
        combat_pay_info["include_in_eic_calculation"] = "No"


    user_responses["combat_pay_info"] = combat_pay_info

    # determain deductions - expenses
    question11 = "Choose all 2022 expenses that apply."
    explain11 = """
    If you don't see an expense you want to report listed here, choose Other
    expenses. You can enter any additional credits, deductions, adjustments, or tax
    amounts you think we should include in our calculation there.
    """
    print(question11)
    print(explain11)


    expense_types = []
    Multiple_choice_content = """
    1.Home ownership
    2.Childcare
    3.Education
    4.Medical expenses
    5.Charitable donations
    6.Other expenses
    7.None apply
    """
    print(Multiple_choice_content)

    expense_choices = input("Enter the numbers corresponding to your expense types (e.g., '1 2 3'): ")

    expense_choices = expense_choices.split()  

    for choice in expense_choices:
        if choice == "1":
            expense_types.append("Home ownership")
        elif choice == "2":
            expense_types.append("Childcare")
        elif choice == "3":
            expense_types.append("Education")
        elif choice == "4":
            expense_types.append("Medical expenses")
        elif choice == "5":
            expense_types.append("Charitable donations")
        elif choice == "6":
            expense_types.append("Other expenses")
        elif choice == "7":
            expense_types = ["None apply"]
        else:
            print("Invalid choice. Please enter valid numbers.")


    user_responses["expense_types"] = expense_types

    # Q12 homeowner exps - Sch C
    question12 = "Enter your homeowner expenses."
    print(question12)


    homeowner_expenses = {}

    homeowner_expenses["mortgage_interest"] = input("Mortgage interest (1098, Box 1): ")
    homeowner_expenses["real_estate_taxes"] = input("Real estate taxes (1098, Box 10): ")
    homeowner_expenses["homebuyer_credit_repayment"] = input("Repayment of homebuyer credit: ")


    user_responses["homeowner_expenses"] = homeowner_expenses

    # Q13 child expenses
    question13 = "Enter your total childcare expenses."
    explain13 = """
    Include any 2022 expenses you paid to provide care for a qualified
    dependent while you (and your spouse) worked or looked for work
    (Ex: fees paid to a licensed daycare center or babysitter). This helps us
    estimate your child and dependent care credit.
    """
    print(question13)
    print(explain13)

    childcare_expenses = input("Childcare expenses for 2022: ")

    user_responses["childcare_expenses"] = childcare_expenses

    estimated_refund = 112

    print("Your estimated total federal refund is \t $", estimated_refund)

    result = """
    Taxable Income: \t\t $0
    Taxes owed: \t\t $0
    Tax credit: \t\t $2
    Taxes paid: \t\t $140
    """
    print(result)

    print("1. File taxes")
    print("2. Print your results")
    user_choice = input("Please enter the number corresponding to your choice: ")

    if user_choice == "1":
    
        print("Processing tax filing...")
    
        print("Tax filing complete.")
    elif user_choice == "2":
        
        print("Printing your results...")
        
        print("Results printed.")
    else:
        print("Invalid choice. Please enter 1 to file taxes or 2 to print your results.")

    c1_row12 = [140, 2, 112]

    about_you = ["Head of Household", 1, 21, 120]
    your_incom = [21, 500, 0, 0 ,0]
    your_expenses = [260, 50, 0, 0, 0, 0]

    taxable_income = [0, 42, 19400, 0]
    taxable_owed = [0, 0 ,10]
    tax_credits = [2, 0, 0, 0]
    taxes_paid = [140, 140, 32]


    result = """
    --------------------------------------------Your summary--------------------------------------------

    What you paid in taxes:              ${c1_row120}         Your estimated
    Tax credit you received this year:   ${c1_row121}           federal refund:  ${c1_row122}

    -------------What you told us------------         ---------Based upon your answers------------------
                                                    We have provided estimates of your tax outcome for
                                                    this year and how tax reform could affect your
                                                    outcome next year.
    About you
    -----------------------------------------         Taxable income                                  ${taxable_income0}
    Filing status           {about_you0}         --------------------------------------------------
    Dependents                              {about_you1}         Adjusted Gross Income (AGI)                    ${taxable_income1}
    Total wages                           ${about_you2}         Greater of Itemized or Std. Deduction      ${taxable_income2}
    Federal witholdings                  ${about_you3}         Qualified Business Income Deduction             ${taxable_income3}



    Your incom                                        Taxable owed                                    ${taxable_owed0}
    -----------------------------------------         --------------------------------------------------
    Unemployment                          ${your_incom0}         Taxable income                                  ${taxable_owed1}
    Combat pay                           ${your_incom1}         Estimated tax rate                             {taxable_owed2}%
    Social Security                        ${your_incom2}
    Investments                            ${your_incom3}
    Business/self-employed                 ${your_incom4}
                                                    Tax credits                                     ${tax_credits0}
                                                    --------------------------------------------------
                                                    Child tax credit                                ${tax_credits1}
    Your expenses                                     Lifetime learning credit                        ${tax_credits2}
    -----------------------------------------         Refundable American Opportunity Tax Credit      ${tax_credits3}
    Home ownership                       ${your_expenses0}
    Childcare                             ${your_expenses1}
    Education                              ${your_expenses2}
    Medical expenses                       ${your_expenses3}         Taxes paid                                    ${taxes_paid0}
    Charitable donations                   ${your_expenses4}         --------------------------------------------------
    Other expenses                         ${your_expenses5}         Federal income taxes withheld                 ${taxes_paid1}
                                                    State and local taxes paid                     ${taxes_paid2}



    * This is an estimate for informational purposes only. Consult your tax professional regarding your
    individual tax situation
    """.format(c1_row120 = c1_row12[0], c1_row121 = c1_row12[1], c1_row122 = c1_row12[2],
                about_you0 = about_you[0], about_you1 = about_you[1], about_you2 = about_you[2], about_you3 = about_you[3],
                your_incom0 = your_incom[0], your_incom1 = your_incom[1], your_incom2 = your_incom[2], your_incom3 = your_incom[3], your_incom4 = your_incom[4],
                your_expenses0 = your_expenses[0], your_expenses1 = your_expenses[1], your_expenses2 = your_expenses[2],
                your_expenses3 = your_expenses[3], your_expenses4 = your_expenses[4], your_expenses5 = your_expenses[5],
                taxable_income0 = taxable_income[0], taxable_income1 = taxable_income[1], taxable_income2 = taxable_income[2], taxable_income3 = taxable_income[3],
                taxable_owed0 = taxable_owed[0], taxable_owed1 = taxable_owed[1], taxable_owed2 = taxable_owed[2],
                tax_credits0 = tax_credits[0], tax_credits1 = tax_credits[1], tax_credits2 = tax_credits[2], tax_credits3 = tax_credits[3],
                taxes_paid0 = taxes_paid[0], taxes_paid1 = taxes_paid[1], taxes_paid2 = taxes_paid[2])

    print(result)



    print("User end result:")
    print(user_responses)