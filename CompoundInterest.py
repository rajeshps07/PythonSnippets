# compute compound interest the traditional way \
# (w/o formulas)

import math

p = float(input("Enter Principal(in Rs.): "))
r = float(input("Enter Rate (in %): "))
n = float(input("Enter Duration (in years): "))


com = 4
rate = (1 + r / (com * 100))

def ciwoformula():
    """ Compute the total amount for fixed deposit\
    where interest compounded quarterly without the \
    use of formulas """

    amount = 0
    i = 1
    while i <= (com*n):
        calc = math.pow(rate, i)
        amount = p * calc
        #print(i, round(amount, 2))
        i += 1
    return amount

def ciwformula():
    amount = p * math.pow((1 + r / 400), 4 * n)
    return amount


def main():
    amount = ciwoformula()
    print()
    print("Amount: ", round(amount, 2))
    print("Interest: ", round(amount - p, 2))

if __name__ == "__main__":
    main()
