# Initializing variables
starting_pay = 0.01 # dollars
day_pay = starting_pay
increase_rate = 2
pay_period = 30 # days
i = 0

# https://www.geeksforgeeks.org/difference-between-recursion-and-iteration/
# https://www.geeksforgeeks.org/tail-recursion/
def RecursivePay(pay_period, day_pay):
    # Day list hard-coded. Would require additional thought to work with original input
    day = abs(31-pay_period)
    print('Day', day, 'pays: $', day_pay)
    if pay_period == 1:
        return day_pay
    else:
        return RecursivePay(pay_period - 1, day_pay * 2)

RecursivePay(pay_period, day_pay)