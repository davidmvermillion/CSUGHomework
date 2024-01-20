# Write an algorithm in Python that will represent your 
# stepwise refinement approach for the program of your choice.

# Program Choice: Develop a check writer that, 
# given a numeric dollar amount, will print the amount in words 
# normally required on a check.

# Stepwise Refinement Description
print('\nFirst Level Abstraction:\n',
      '\n1. Accept numerical input',
      '\n2. Convert to words',
      '\n3. Display word output\n',
      '\n\nSecond Level Abstraction:',
      '\n1. Ask the user for a numerical only entry without commas',
      '\n2. Split the numerical portion into words that follow the relevant format.',
      '\n3. Calculate the output to see if we need to add character fillers.',
      '\n4. Correctly display the word output.\n',
      '\n\nThird Level Abstraction:',
      '\n1. Ask the user for a numerical only entry without commas.',
      '\n   This requires a format sample to be displayed.',
      '\n2. Split the numerical portion into words that follow the relevant format.',
      '\n   This requires splitting numbers for each factor of ten and separating cents for separate display.',
      '\n3. Calculate the output to see if we need to add character fillers.',
      '\n   This requires an estimate of evenly-spaced character counts for the line.',
      '\n   We\'ll estimate it at 78 characters',
      '\n4. Correctly display the word output.',
      '\n   This follows step 2 and requires each portion to be correctly formatted with hyphens as applicable,',
      '\n   no “and”, and fractional cent displays.\n')

# Program

# https://www.geeksforgeeks.org/python-number-to-words-using-num2words/
# https://pypi.org/project/num2words/
# Setup Environment and variables
from num2words import num2words
import math
import pandas as pd
maxchar = 78
delchar = ' and '
# Entry as float. Will not accept other strings
# https://www.includehelp.com/python/read-input-as-a-float.aspx
entry = float(input('\nPlease input your desired number using only numerals. For example, "1432.34"\n\n'))
# https://www.geeksforgeeks.org/floor-ceil-function-python/
# Split cents from dollars and remove 'and'
entry1 = int(math.floor(entry))
entry2 = str(round(entry - entry1, 2))
entry2 = entry2.replace('0.', ' ')
part1 = num2words(entry1)
if delchar in part1:
#     https://stackoverflow.com/a/23669051
    part1 = part1.replace(delchar, ' ')
else:
    exit
#     https://www.freecodecamp.org/news/append-a-string-in-python-str-appending/
# cents
part2 = str(entry2 + '/100')
# String it all together
part3 = (part1 + ' dollars' + part2)
# Fill extra characters
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.ljust.html#pandas.Series.str.ljust
# https://docs.python.org/3/library/stdtypes.html#str.ljust
part3 = part3.ljust(maxchar, '-')
# Output
print("\nFill the word amount section of your check as follows.",
      "\nDashes indicate a need to place a line in empty spaces.",
      '\n', part3, '\n')