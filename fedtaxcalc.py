from bisect import bisect


def get_income():
    """Establish user's Taxable Income for tax expense estimation.

    :input: users adjusted gross income (AGI) entered
        as a whole number.
    :returns: taxable_income (int)
    """
    while True:
        try:
            taxable_income = int(input(
                "Enter your Taxable Income as a whole number: "
            ))
            taxable_income = int(taxable_income)
            break
        except ValueError:
            print("Not a valid integer! Please try again ...")
    return taxable_income


def print_data(taxable_income, filing_status, fed_tax_yr):
    """Prints to user Taxable Income, Filing Status, estimated Federal Tax.

    :param taxable_income: (int) user input adjusted gross income, or AGI
    :param filing_status: (str) user input 'single' or 'married'
    :param fed_tax_yr: (int) estimated federal tax calculation
    :print: AGI, Filing Status, estimated Federal Income tax
    """
    print(f"Annual Gross Income: $ {taxable_income:.2f}"
          f"\nFiling status: {filing_status.title()}"
          f"\n__________ "
          f"\n\nYour estimated federal income taxes are $ {fed_tax_yr:.2f}")


def get_filing_status():
    """Establish user's Filing Status for correct tax bracket.

    :input: (str) filing status, Single or Married
    :return: (str) filing_status, in lowercase
    """
    filing_status = ""
    while filing_status.casefold() not in ['single', 'married']:
        filing_status = input(
            "What is your filing status? "
            "\nEnter 'single' or 'married': ")
    return filing_status.casefold()


def calc_fed_tax(filing_status, taxable_income):
    """Provides calculated estimate of federal taxes based off of the 2021
    USA tax brackets for filing as Single or Married.

    :param filing_status: (str) user input 'single' or 'married'.
    :param taxable_income: (int) user input adjusted gross income (AGI).
    :return: fed_tax_yr (flt): total estimated federal taxes
    """    
    # 2021 USA Tax Rates
    rates = [.10, .12, .22, .24, .32, .35, .37]  

    if filing_status == "married":
        brackets = [19900, 81050, 172750, 329850, 418850, 628300]
        base_tax = [1990, 9328, 29502, 67206, 95686, 168993.50]

    elif filing_status == "single":
        brackets = [9950, 40525, 86375, 164925, 209425, 523600]
        base_tax = [995, 4464, 14751, 33603, 47843, 157804.25]

    # else is unnecessary but remains for above if/elif readability
    else:
        print("Unknown filing status.")
        return 0

    i = bisect(brackets, taxable_income)
    # if in first tax bracket ONLY
    if i == 0:
        fed_tax_yr = taxable_income * rates[0]
        return fed_tax_yr
    # if in any other tax bracket
    rate = rates[i]
    bracket = brackets[i - 1]
    income_in_bracket = taxable_income - bracket
    tax_in_bracket = income_in_bracket * rate
    fed_tax_yr = base_tax[i - 1] + tax_in_bracket
    return fed_tax_yr


def print_net_income_mo(net_income_mo):
    """Prints Yearly Net Income and Monthly Net Income to user.

    :param inc_net_mo: (flt) monthly net income after estimated federal taxes
    :print: monthly net income; available income to invest.
    """
    print(f"Your yearly net income is $ {(net_income_mo * 12):.2f}")
    print(f"Your monthly net income is $ {net_income_mo:.2f}")


def net_income_func(taxable_income, fed_tax_yr):
    """Quick calculation to share with user via print function. User provided
    income minus estimated federal taxes.

    :param taxable_income: (int), user input adjusted gross income (AGI)
    :param fed_tax_yr: (flt), estimated federal taxes based off 2021 tax rates
    :return: (flt) inc_net_mo, monthly net income after estimated federal taxes
    """
    net_income_mo = (taxable_income - fed_tax_yr) / 12
    return net_income_mo

def tax_calc():
    """Invokes functions above; runs program."""
    taxable_income = get_income()
    filing_status = get_filing_status()
    fed_tax_yr = calc_fed_tax(filing_status, taxable_income)
    net_income_mo = net_income_func(taxable_income, fed_tax_yr)
    print_data(taxable_income, filing_status, fed_tax_yr)
    print_net_income_mo(net_income_mo)

# Auto-run program on open. Comment below line out to run unit tests
# tax_calc()
