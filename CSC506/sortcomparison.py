import insertionsort as IS
import quicksort as QS
# https://www.geeksforgeeks.org/how-to-check-the-execution-time-of-python-script/
from datetime import datetime

# Create a list of unsorted values using the same seed for repeatability
# https://www.geeksforgeeks.org/generating-random-number-list-in-python/
# https://www.w3schools.com/python/ref_random_seed.asp
import random
random.seed(42)
numbers = list(random.sample(range(1, 50), 25))
numbers2 = numbers

# Print unsorted list
# print('UNSORTED:', numbers)

# Show Insertion Sort Performance
start = datetime.now()
IS.insertion_sort(numbers)
end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"Insertion Sort executed in : {td:.03f}ms")
print('SORTED:', numbers)

# Show Quick Sort Performance
start = datetime.now()
QS.quicksort(numbers2, 0, len(numbers2)-1)
end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"Insertion Sort executed in : {td:.03f}ms")
print('SORTED:', numbers2)