# Setup workspace
import insertionsort as IS
import quicksort as QS
from datetime import datetime
import random
import numpy as np
insertionperformance = []
quickperformance = []

# Create a list of unsorted values using the same seed for repeatability
random.seed(42)
numbers = list(random.sample(range(1, 1000000), 500))
numbers2 = numbers

# Calculate Insertion Sort Performance over 1k samples
for i in range(1,1000):
    start = datetime.now()
    IS.insertion_sort(numbers)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    insertionperformance.append(td)

# Calculate Quick Sort Performance over 1k samples
for i in range(1,1000):
    start = datetime.now()
    QS.quicksort(numbers2, 0, len(numbers2)-1)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    quickperformance.append(td)

# Display Findings
ipav = np.average(insertionperformance) # Insertion Sort Performance Average
print(f"Insertion Sort executed in an average of: {ipav:.03f}ms")
qpav = np.average(quickperformance) # Quick Sort Performance Average
print(f"Quick Sort executed in an average of: {qpav:.03f}ms")
diff = qpav - ipav
mdiff = qpav / ipav
print(f"\nInsertion Sort was {diff:.03f}ms or {mdiff:.0f}x faster than Quick Sort \n")