# Setup
import random
from datetime import datetime
import multiprocessing
# import time 
import numpy as np
import re
import os
import sys
os.chdir( os.path.dirname( sys.argv[0] ) )

# Datetime counter start
start = datetime.now()

# Loop Length
length1 = list(range(1,250000))
length2 = list(range(250000,500000))
length3 = list(range(500000,750000))
length4 = list(range(750000,1000000))
length5 = list(range(750000,1000000))
length6 = list(range(750000,1000000))
length7 = list(range(750000,1000000))
length8 = list(range(750000,1000000))
length9 = list(range(750000,1000000))
length10 = list(range(750000,1000000))

# length = list(range(9))
# length[0] = list(range(1,250000))
# length[1] = list(range(250000,500000))
# length[2] = list(range(500000,750000))
# length[3] = list(range(750000,1000000))
# length[4] = list(range(750000,1000000))
# length[5] = list(range(750000,1000000))
# length[6] = list(range(750000,1000000))
# length[7] = list(range(750000,1000000))
# length[8] = list(range(750000,1000000))
# length[9] = list(range(750000,1000000))

# Splits
n = 10
file = np.loadtxt('file3.txt', dtype = int)
lbl = np.split(file, n)

# Create functions

# https://www.geeksforgeeks.org/get-variable-name-as-string-in-python/
def get_var_name(var):
    for name, value in globals().items():
        if value is var:
            return name

# https://stackoverflow.com/a/40771263/13801562
def get_numbers(string):
    result = [int(num) for num in re.findall(r"\d+", string)]
    return result[0]

def loop(length):
    # file = open('CSC507/Module6/file3.txt', 'a')
    split10p = open("newfile10p_" + str(get_var_name(length)) + ".txt", 'w')
    x = get_numbers(get_var_name(length)) - 1
    for i in length:
        split10p.write(str((lbl[x][i])*2) + '\n')
    split10p.close()



# https://www.geeksforgeeks.org/parallel-processing-in-python/
# Parallel processing write loop
if __name__ == '__main__': 
    pool = multiprocessing.Pool() 
    pool = multiprocessing.Pool(processes = 10) 
    # inputs = [length[0], length[1], length[2], length[3], length[4], length[5], length[6], length[7], length[8], length[9]] 
    inputs = [length1, length2, length3, length4, length5, length6, length7, length8, length9, length10] 
    outputs = pool.map(loop, inputs) 

# Final runtime
end = datetime.now()
print((end - start).total_seconds())