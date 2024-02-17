# Initialize Environment
import random
from datetime import datetime
import matplotlib.pyplot as plt

testrange = list(range(0,100000))
hashcomp = []

# Create a list of unsorted values using the same seed for repeatability
random.seed(42)
testcase = list(random.sample(range(1, 1000000), 500))

# Define Linear Probe Hash Functions
# https://www.flamingbytes.com/blog/hash-table-implementation-in-python/
def hash_func(key):
    return key % len(hash3)

def insert(key, value):
    hash_key = hash_func(key)
    hash3[hash_key] = value
    while hash3[hash_key]:
        hash_key = (hash_key + 1) % len(hash3)

# Calculations
for i in testrange:
    start = datetime.now()
    hash3 = [None] * 1031
    for key in testcase:
        insert(key, key)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    hashcomp.append(td)

# Plot Results
fig, ax = plt.subplots(figsize=(5,3))
plt.grid(which = 'major', axis = 'both', linestyle = ':', color = '#e9e9e9')
plt.plot(testrange, hashcomp, color = '#2d3047')
xlim = ax.get_xlim()
ax.set_xlabel('Iteration', fontsize = 15, loc =
				'left').set_color('#707070')
ax.set_ylabel('Time\n(ms)', fontsize = 15, rotation =
				'horizontal', loc = 'bottom', labelpad =
				45).set_color('#707070')
ax.set_title('Most Iterations Required 0.2ms to\nInsert 500 Items into Hash Table\nof 1031 Length with Linear Probing', fontsize = 23, pad = 15).set_color('#171819')
for pos in ['right', 'top']:
	plt.gca().spines[pos].set_visible(False)
ax.spines['bottom'].set_color('#A0A0A0')
ax.spines['left'].set_color('#A0A0A0')
# https://stackoverflow.com/a/11250884/13801562
labels = [item.get_text() for item in ax.get_xticklabels()]
labels[2], labels[3], labels[4], labels[5], labels[6] = '20k', '40k', '60k', '80k', '100k'
ax.set_xticklabels(labels);
ax.tick_params(axis='y', which='both', right=False,
				left=False, colors = '#686868')
ax.tick_params(axis='x', which='both', top=False,
				bottom=False, colors = '#686868')
plt.show();