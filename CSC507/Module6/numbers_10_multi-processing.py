# Setup
from datetime import datetime
import multiprocessing
import numpy as np
import re
# https://www.reddit.com/r/learnpython/comments/7bnaf1/comment/dpjiupw/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
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

# https://www.geeksforgeeks.org/multiprocessing-python-set-1/
# Multiprocessing write loop
if __name__ == "__main__": 
    # Create processes 
    p1 = multiprocessing.Process(target=loop(length1), args=(10, )) 
    p2 = multiprocessing.Process(target=loop(length2), args=(10, )) 
    p3 = multiprocessing.Process(target=loop(length3), args=(10, )) 
    p4 = multiprocessing.Process(target=loop(length4), args=(10, )) 
    p5 = multiprocessing.Process(target=loop(length5), args=(10, )) 
    p6 = multiprocessing.Process(target=loop(length6), args=(10, )) 
    p7 = multiprocessing.Process(target=loop(length7), args=(10, )) 
    p8 = multiprocessing.Process(target=loop(length8), args=(10, )) 
    p9 = multiprocessing.Process(target=loop(length9), args=(10, )) 
    p10 = multiprocessing.Process(target=loop(length10), args=(10, )) 
  
    # Start processes 
    p1.start() 
    p2.start()
    p3.start() 
    p4.start() 
    p5.start() 
    p6.start()
    p7.start() 
    p8.start()
    p9.start() 
    p10.start()  
  
    # Wait until processes are finished 
    p1.join() 
    p2.join()
    p3.join() 
    p4.join()  
    p5.join() 
    p6.join()
    p7.join() 
    p8.join()
    p9.join() 
    p10.join() 
  
    # Processes finished 
    print("Done!") 

# Final runtime
end = datetime.now()
print((end - start).total_seconds())