# Setup
import random
from datetime import datetime
import multiprocessing

# Datetime counter start
start = datetime.now()

# Loop Length
length1 = list(range(1,250000))
length2 = list(range(250000,500000))
length3 = list(range(500000,750000))
length4 = list(range(750000,1000000))

# Create function
def loop(length):
    file = open('CSC507/Module3/file2.txt', 'a')
    for i in length:
        file.write('\n')
        file.write(str(int(random.random()*1000)))
    file.close()

# https://www.geeksforgeeks.org/multiprocessing-python-set-1/
# Multiprocessing write loop
if __name__ == "__main__": 
    # Create processes 
    p1 = multiprocessing.Process(target=loop(length1), args=(10, )) 
    p2 = multiprocessing.Process(target=loop(length2), args=(10, )) 
    p3 = multiprocessing.Process(target=loop(length3), args=(10, )) 
    p4 = multiprocessing.Process(target=loop(length4), args=(10, )) 
  
    # Start processes 
    p1.start() 
    p2.start()
    p3.start() 
    p4.start() 
  
    # Wait until processes are finished 
    p1.join() 
    p2.join()
    p3.join() 
    p4.join()  
  
    # Processes finished 
    print("Done!") 

# file.close()

# Final runtime
end = datetime.now()
print((end - start).total_seconds())