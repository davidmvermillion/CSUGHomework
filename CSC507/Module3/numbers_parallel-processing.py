# Setup
import random
from datetime import datetime
import multiprocessing
import time 

# Datetime counter start
start = datetime.now()

# Loop Length
length1 = list(range(1,250000))
length2 = list(range(250000,500000))
length3 = list(range(500000,750000))
length4 = list(range(750000,1000000))

# Create function
def loop(length):
    for i in length:
        file.write('\n')
        file.write(str(int(random.random()*1000)))

# Create file
file = open('CSC507/Module3/file2.txt', 'x')
file.write(str(int(random.random()*1000)))
file.close()

# Change file access type
file = open('CSC507/Module3/file2.txt', 'a')

# https://www.geeksforgeeks.org/multiprocessing-python-set-1/
# Parallel processing write loop
if __name__ == '__main__': 
	pool = multiprocessing.Pool() 
	pool = multiprocessing.Pool(processes=4) 
	inputs = [length1, length2, length3, length4] 
	outputs = pool.map(loop, inputs) 

file.close()

# Final runtime
end = datetime.now()
print((end - start).total_seconds())