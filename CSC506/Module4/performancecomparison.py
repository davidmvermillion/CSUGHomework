# Design and implement an experiment that will compare the performance of the Python list based
# stack and queue with the linked list implementation.
# https://www.geeksforgeeks.org/stack-in-python/

# Initialize Environment
from queue import LifoQueue
import linkedstack
from datetime import datetime
import numpy as np
testcase = list(range(0,100000))
qsperf = [] # Queue-based stack performance comparison
lsperf = [] # List stack performance comparison
llsperf = [] # Linked-list stack comparison

# Queue-based stack
# Create queue-based stack
staq = LifoQueue(maxsize = 100001)

# Insert
for i in testcase:
    start = datetime.now()
    staq.put(i)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    qsperf.append(td)

# Pop
for i in testcase:
    start = datetime.now()
    staq.get()
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    qsperf.append(td)    

qsav = np.average(qsperf) # Queue-based stack performance average
qsmax = np.max(qsav) # Maximum runtime in test
print(f"Queue-based stack insertion and popping of 9999 objects executed in an average of: {qsav:.03f}ms")

# Using a list as a stack
# Create list-based stack
stack = []

# Insert
for i in testcase:
    start = datetime.now()
    stack.append(i)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    lsperf.append(td)

# Pop
for i in testcase:
    start = datetime.now()
    stack.pop()
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    lsperf.append(td)    

lsav = np.average(lsperf) # Queue-based stack performance average
lsmax = np.max(lsav) # Maximum runtime in test
print(f"List-based stack insertion and popping of 9999 objects executed in an average of: {lsav:.03f}ms")


# Linked-List Stack

# Create list-based stack
stackll = linkedstack.Stack()

# Insert
for i in testcase:
    start = datetime.now()
    stackll.push(i)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    llsperf.append(td)

# Pop
for i in testcase:
    start = datetime.now()
    stackll.pop()
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    llsperf.append(td)    

llsav = np.average(llsperf) # Queue-based stack performance average
llsmax = np.max(llsperf) # Maximum runtime in test
print(f"Linked-List based stack insertion and popping of 9999 objects executed in an average of: {llsav:.03f}ms")


# Comparisons
print(f"\nLinked-List based stack insertion and popping of 100k objects executed in an average of {llsav:.03f}ms and no more than {llsmax:.03f}ms per operation")
print(f"\nList based stack insertion and popping of 100k objects executed in an average of {lsav:.03f}ms and no more than {lsmax:.03f}ms per operation")
print(f"\nQueue based stack insertion and popping of 100k objects executed in an average of {qsav:.03f}ms and no more than {qsmax:.03f}ms per operation")
