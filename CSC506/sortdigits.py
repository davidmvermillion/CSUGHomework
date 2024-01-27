# Initialize test case, range, and functions
test_case = 2149876530
test_value = test_case
valid_min = 123456789
valid_max = 9876543210
least_movable = list(range(3,10))
most_movable = list(range(0,10))
# https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
def swapPositions(lis, pos1, pos2):
    for i, x in enumerate(lis):
        if i == pos1:
            elem1 = x
        if i == pos2:
            elem2 = x
    lis[pos1] = elem2
    lis[pos2] = elem1
    return lis
# Calculation Loop
if test_case < valid_min:
    print("\nTest case is below the 10 digit integer minimum")
elif test_case > valid_max:
    print("\nTest case is larger than the 10 digit integer maximum")
elif test_case == valid_max:
    print("\nTest case has the maximum possible value.\nNo larger number exists within the given parameters")
else:
    while test_value <= test_case:
        # https://stackoverflow.com/a/21270338
        test_list = [int(a) for a in str(test_case)]
        if test_list[0] & test_list[1] > 2:
            for i, x in enumerate(test_list):
                while i in least_movable:
                    if test_value <= test_case:
                        for n in most_movable:
                            swapPositions(test_list, i, n)
                            # https://sparkbyexamples.com/python/python-list-to-integer/
                            test_value = int(''.join(map(str, test_list)))
print('\n', test_value, ' is the next largest valid number after ', test_case)