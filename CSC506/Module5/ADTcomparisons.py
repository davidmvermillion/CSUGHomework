# Starting Information
from datetime import datetime
import matplotlib.pyplot as plt
from hashchain import HashTable

# Key Values
keys = [12345, 67890, 54321, 98765, 24680, 
        13579, 11223, 44556, 99999, 77777]

# Name Values
names = ["John Smith", "Jane Doe", "Alice Johnson", "Bob Williams", "Eve Brown", 
         "Charlie Davis", "Grace Wilson", "David Lee", "Olivia Martinez","Sophia Anderson"]

# Length of key list
listrange = list(range(0, len(keys)))

# Comparison Starters
testcase = list(range(0,100000))
hashcomp = []
dictcomp = []

# https://www.geeksforgeeks.org/implementation-of-hash-table-in-python-using-separate-chaining/
for i in testcase:
    # Create Hash Table with length next largest prime after key length
    start = datetime.now()
    hash = HashTable(13)
    for i in listrange:
        hash.insert(keys[i], names[i])

    # Remove items in table
    for key in keys:
        hash.remove(key)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    hashcomp.append(td)

# https://www.freecodecamp.org/news/add-to-dict-in-python/
for i in testcase:
    # Create Dictionary
    start = datetime.now()
    dictionary = {}
    for i in listrange:
        dictionary[keys[i]] = names[i]

    # Remove items in dictionary
    for key in keys:
        dictionary.pop(key)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    dictcomp.append(td)

# Generate Boxplot
comparisons = [hashcomp, dictcomp]
labels = ['Hash Table', 'Dictionary']
fig, ax = plt.subplots()
ax.boxplot(comparisons, 0, '', labels = labels)
ax.set_title('100k Run Performance\nComparisons (ms)', fontsize = 23, pad = 15).set_color('#171819')
for pos in ['right', 'top']:
	plt.gca().spines[pos].set_visible(False)
ax.spines['bottom'].set_color('#A0A0A0')
ax.spines['left'].set_color('#A0A0A0')
ax.tick_params(axis = 'x', colors = '#282828', labelsize = 15)
ax.tick_params(axis = 'y', which = 'both', right = False,
				left = False, colors = '#101010')
plt.show()