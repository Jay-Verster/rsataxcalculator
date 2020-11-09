## Notes: A welcome message will be displayed to the user.

print("\nWelcome to the Python Tax Calculator! Get a summary of your income \
taxes by entering your gross salary below.")

## Notes: The below code will request the user's salary through an integer input from the user, which will later be used to calculate their tax information.

salary = float(input("\nPlease enter how your Gross annual salary, before \
deductions. (Please use only numberical digits) \nGross Salary: R"))

if salary < 1:
    print("You do not fall under any of the thresholds!")
elif salary > 1 and salary < 205900:
    annual_tax = (salary * 18 / 100)
    monthly_tax = annual_tax / 11
    annual_nett_pay = salary - annual_tax
    monthly_nett_pay = annual_nett_pay / 12
    print(f"\nYour tax summary is as follows:\n \nAnnual Tax: R{annual_tax:.2f} \
    \nMonthly Tax: R{monthly_tax:.2f} \nAnnual Nett Pay: R{annual_nett_pay:.2f} \
    \nMonthly Nett Pay: R{monthly_nett_pay:.2f}")
elif salary > 205901 and salary < 321600:
    deductions = salary * (27.4 / 100)
    annual_tax = salary * (26 / 100) + 37062 - deductions
    monthly_tax = annual_tax / 11
    annual_nett_pay = salary - annual_tax
    monthly_nett_pay = annual_nett_pay / 12
    print(f"\nYour tax summary is as follows:\n \nAnnual Tax: R{annual_tax:.2f} \
    \nMonthly Tax: R{monthly_tax:.2f} \nAnnual Nett Pay: R{annual_nett_pay:.2f} \
    \nMonthly Nett Pay: R{monthly_nett_pay:.2f}")
elif salary > 321601 and salary < 445100:
    deductions = salary * (27.4 / 100)
    annual_tax = (salary * 31 / 100) + 67144 - deductions
    monthly_tax = annual_tax / 11
    annual_nett_pay = salary - annual_tax
    monthly_nett_pay = annual_nett_pay / 12
    print(f"\nYour tax summary is as follows:\n \nAnnual Tax: R{annual_tax:.2f} \
    \nMonthly Tax: R{monthly_tax:.2f} \nAnnual Nett Pay: R{annual_nett_pay:.2f} \
    \nMonthly Nett Pay: R{monthly_nett_pay:.2f}")
elif salary > 445101 and salary < 584200:
    deductions = salary * (27.4 / 100)
    annual_tax = (salary * 36 / 100) + 105429 - deductions
    monthly_tax = annual_tax / 11
    annual_nett_pay = salary - annual_tax
    monthly_nett_pay = annual_nett_pay / 12
    print(f"\nYour tax summary is as follows:\n \nAnnual Tax: R{annual_tax:.2f} \
    \nMonthly Tax: R{monthly_tax:.2f} \nAnnual Nett Pay: R{annual_nett_pay:.2f} \
    \nMonthly Nett Pay: R{monthly_nett_pay:.2f}")
elif salary > 584201 and salary < 744800:
    deductions = salary * (27.4 / 100)
    annual_tax = (salary * 39 / 100) + 155505 - deductions
    monthly_tax = annual_tax / 11
    annual_nett_pay = salary - annual_tax
    monthly_nett_pay = annual_nett_pay / 12
    print(f"\nYour tax summary is as follows:\n \nAnnual Tax: R{annual_tax:.2f} \
    \nMonthly Tax: R{monthly_tax:.2f} \nAnnual Nett Pay: R{annual_nett_pay:.2f} \
    \nMonthly Nett Pay: R{monthly_nett_pay:.2f}")
elif salary > 744801 and salary < 1577300:
    deductions = salary * (27.4 / 100)
    annual_tax = (salary * 41 / 100) + 218139 - deductions
    monthly_tax = annual_tax / 11
    annual_nett_pay = salary - annual_tax
    monthly_nett_pay = annual_nett_pay / 12
    print(f"\nYour tax summary is as follows:\n \nAnnual Tax: R{annual_tax:.2f} \
    \nMonthly Tax: R{monthly_tax:.2f} \nAnnual Nett Pay: R{annual_nett_pay:.2f} \
    \nMonthly Nett Pay: R{monthly_nett_pay:.2f}")
elif salary > 1577301:
    deductions = salary * (27.4 / 100)
    annual_tax = (salary * (45 / 100)) + 559464 - deductions
    monthly_tax = annual_tax / 11
    annual_nett_pay = salary - annual_tax
    monthly_nett_pay = annual_nett_pay / 12
    print(f"\nYour tax summary is as follows:\n \nAnnual Tax: R{annual_tax:.2f} \
    \nMonthly Tax: R{monthly_tax:.2f} \nAnnual Nett Pay: R{annual_nett_pay:.2f} \
    \nMonthly Nett Pay: R{monthly_nett_pay:.2f}")
    
print("\nThis calcullator assumes that you contribute 27.4% of your \
gross salary towards Medical Aid, UIF and a Provident Fund or Retirement Scheme.")

print("\nSource: https://www.sars.gov.za/Tax-Rates/Income-Tax/Pages/Rates%20of%20Tax%20for%20Individuals.aspx ")
