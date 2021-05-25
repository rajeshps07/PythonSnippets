# compute recurring deposit the traditional way (w/o formulas)
import math

p = float(input("Enter the monthly investment (in Rs): "))
r = float(input("Enter the Rate of interest (in %): "))
n = int(input("Enter no. of installments (in months): "))


def invested():
    invest = p * n
    return invest


def rdWoFormula():
    """ Compute the total amount for recurring deposit\
    where interest compounded quarterly without the use \
    of formulas """

    compounding = 4
    duration = n
    amount = 0
    for i in range(duration):
        exponent = (duration * compounding) / 12
        base = 1 + (r / (compounding * 100))
        frac = math.pow(base, exponent)
        duration -= 1
        interest = p * frac
        amount += interest
    return amount


def rdWFormula():
    compounding = 4
    time = n / 12
    base = 1 + (r / (compounding * 100))
    num = p * (math.pow(base, 4 * time) - 1)
    den = 1 - math.pow(base, -1 / 3)
    amount = num / den
    return amount


rd_amount = rdWoFormula()
investment = invested()


def interestGained():
    int_gain = rd_amount - investment
    return int_gain


interest_gain = interestGained()


def main():
    rdWoFormula()
    invested()
    interestGained()
    print()
    print("Total investment: ", round(investment, 2))
    print("Maturity amount: ", (round(rd_amount, 2)))
    print("Interest: ", round(interest_gain, 2))


if __name__ == "__main__":
    main()
