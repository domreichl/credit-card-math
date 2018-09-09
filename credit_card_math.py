# credit_card_math.py by Dom Reichl
# two recursive functions for calculating credit card debt

def calc_balance(bal, minPR, mIR, month, payments):
    '''
    Calculates the credit card balance after X months for
    a person who only pays the minimum monthly payment.
    It also builds a list of monthly payments.
    '''
    
    month -= 1
    if month < 0:
        return round(bal, 2), payments # base case
    else:
        minP = minPR * bal # minimum monthly payment
        payments.append(minP) # build list of monthly payments
        unpaid = bal - minP # unpaid balance
        bal = unpaid + mIR * unpaid # updated balance
        return calc_balance(bal, minPR, mIR, month, payments) # update balance recursively

def pay_off_dept(bal, mIR, month, lower, upper):
    '''
    Calculates the minimum fixed monthly payment needed in order to pay off
    a credit card balance within X months using bisection search.
    '''
    
    guess = (lower + upper) / 2 # guess for bisection search
    month -= 1
    if month < 0:
        if round(bal) == 0:
            return round(guess, 2) # base case
        elif bal < 0: # if balance is negative, reduce upper bound for monthly payment
            return pay_off_dept(balance, mIR, months, lower, guess)
                # narrow the guessing range recursively
                # while resetting arguments 'bal' and 'month' to the global variables 'balance' and 'months'
        else: # if balance is positive, change increase lower bound for monthly payment
            return pay_off_dept(balance, mIR, months, guess, upper)
    else:
        unpaid = bal - guess # unpaid balance
        bal = unpaid + mIR * unpaid # updated balance
        return pay_off_dept(bal, mIR, month, lower, upper) # update balance recursively

# variables to be assigned by the user
balance = 100000 # initial balance
months = 12 # duration
aIR = 0.22 # annual interest rate
mPR = 0.05 # monthly payment rate

mIR = aIR / months # monthly interest rate

payments = []
new_balance, payments = calc_balance(balance, mPR, mIR, months, payments) # calculate remaning balance and monthly payments
average_payment = round(sum(payments) / len(payments), 2) # average monthly payment
loss1 = round(abs(balance - new_balance - sum(payments)), 2) # cost of interest

# set lower and upper bounds for guessing fixed monthly payment:
minGuess = balance / 12 # accurate if there was no interest
maxGuess = (balance * (1 + mIR)**months) / months # accurate if entire balance were paid off at the end of the year

payment = pay_off_dept(balance, mIR, months, minGuess, maxGuess) # calculate minimum monthly payment to pay off dept within X months
loss2 = round(abs(balance - 0 - payment*months), 2) # cost of interest

# output for the user:
print('Current Balance:', balance, '€')
print('Duration:', months, 'months')
print('With a monthly payment rate of %.2f:' % mPR)
print('   - You will pay', average_payment, '€ per month on average.')
print('   - Your loss will be', loss1, '€ for that time period.')
print('   - Your remaining balance will be', new_balance, '€.')
print('If you want to pay off your balance within', months, 'months:')
print('   - You will have to pay', payment, '€ per month.')
print('   - Your loss will be', loss2, '€ in total.')
print('   - Your remaining balance will be 0 €.')
