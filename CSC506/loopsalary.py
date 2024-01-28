# Initializing variables
starting_pay = 0.01 # dollars
day_pay = starting_pay
increase_rate = 2
pay_period = 30 # days

for i in range(1,pay_period + 1):
    print(
        'Day', i, 'pays $', day_pay
    )
    day_pay = day_pay * increase_rate