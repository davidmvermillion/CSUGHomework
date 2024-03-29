# David M Vermillion
# 01/24/2024
# CSC506: Comparing Binary and Sequential Search Algorithms
# Original copied from textbook

def linear_search(numbers, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0
   
    for i in range(len(numbers)):
        comparisons = comparisons + 1
        if (numbers[i] == key):
           return i, comparisons
    return -1, comparisons # not found
 
def binary_search(numbers, key):
    # Added variable to hold total number of comparisons.
    comparisons = 0

    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts at whole range
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
   
    # Loop until "low" passes "high"
    while (high >= low):
        # Calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        comparisons = comparisons + 1
        if (numbers[mid] < key):
            low = mid + 1
      
        elif (numbers[mid] > key):
            high = mid - 1
      
        else:
            return mid, comparisons
  
    return -1, comparisons # not found


# Main program to test both search functions 
numbers = [40,	57,	66,	70,	77,	81,	92,	96,	115,	124,	134,	137,	138,	141,	142,	159,
           	182,	198,	212,	222,	268,	274,	276,	285,	290,	299,	321,	331,
            339,	355,	390,	391]
print('NUMBERS:', numbers)
     
key = int(input('Enter an integer key to search for: '))
print()
 
# Test linear search
key_index, comparisons = linear_search(numbers, key)      
if (key_index == -1):
    print('Linear search: %d was not found with %d comparisons.' % (key, comparisons))
else:
    print('Linear search: Found %d at index %d with %d comparisons.' % (key, key_index, comparisons))
 
# Test binary search
key_index, comparisons = binary_search(numbers, key)
if (key_index == -1):
    print('Binary search: %d was not found with %d comparisons.' % (key, comparisons))
else:
    print('Binary search: Found %d at index %d with %d comparisons.' % (key, key_index, comparisons))