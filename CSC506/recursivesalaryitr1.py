# Initializing variables
starting_pay = 0.01 # dollars
day_pay = starting_pay
increase_rate = 2
pay_period = 30 # days
i = 0

# https://www.geeksforgeeks.org/difference-between-recursion-and-iteration/
def RecursivePay(pay, days, increase):
    day_list = list(range(1, days + 1))
    # i = 0
    if days == 0:
        print('0 days implies no pay')
    elif days == 1:
        print('1 day of pay is: $', pay)
    # https://stackoverflow.com/a/34839438/13801562
    # https://realpython.com/python-recursion/
    else:
        # for index, i in enumerate(day_list):
        #     print('Day ', day_list[i], ' pays: $', increase * )
        # if i < days + 1:
        #     print('Day ', day_list[i], ' pays: $', increase * RecursivePay(pay, day_list[i], increase))
        #     i =+ 1
        # def count_leaf_items(day_list):
        #     """Recursively counts and returns the
        #     number of leaf items in a (potentially
        #     nested) list.
        #     """
        #     count = 0
        #     for item in day_list:
        #         if isinstance(item, list):
        #             count += count_leaf_items(item)
        #             pay += pay * increase
        #             print('Day ', item, ' pays $', pay)
        #         else:
        #             count += 1

        #     return count
        # https://www.geeksforgeeks.org/product-2-numbers-using-recursion/
        # def product( x , y ): 
        #     # if x is less than y swap 
        #     # the numbers 
        #     if x < y: 
        #         return product(y, x) 
            
        #     # iteratively calculate y 
        #     # times sum of x 
        #     elif y != 0: 
        #         return (x + product(x, y - 1)) 
            
        #     # if any of the two numbers is 
        #     # zero return zero 
        #     else: 
        #         return 0
        # product(starting_pay * increase_rate, pay_period)    

RecursivePay(starting_pay, pay_period, increase_rate)


# def factorialUsingRecursion(n):
#     if (n == 0):
#         return 1;
 
#     # recursion call
#     return n * factorialUsingRecursion(n - 1);

# print(factorialUsingRecursion(5))