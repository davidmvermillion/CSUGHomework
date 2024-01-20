# https://www.independent.co.uk/voices/top-10-anagrams-words-trivia-a8285076.html
a, b = "astronomer", "moonstarer"
i = 0
n = 0
if len(a) == len(b):
    # https://www.geeksforgeeks.org/python-string-split/
    # https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
    list_a, list_b = list(a), list(b)
    list_c = []
    # https://stackoverflow.com/questions/49677949/python-while-loop-range-function
    while i in range(0,len(a)):
        if list_a[i] != list_b[n]:
            n += 1
        else:   
            # https://www.w3schools.com/python/python_lists_add.asp
            list_c.append(list_b[n])
            i += 1
            n = 0
    if list_a == list_c:
        print(a, ' is an anagram of ', b)
    else:
        print(a, ' is not an anagram of ', b, ' because no combinations match between them.')
else:
    print(a, ' is not an anagram of ', b, ' because they do not have the same amount of characters.')