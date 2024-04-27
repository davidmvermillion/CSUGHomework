# Setup
import random
from datetime import datetime

# Datetime counter start
start = datetime.now()

# Length of loop and change file access type
length = list(range(1,10000000))
file = open('CSC507/Module6/file3.txt', 'a')

# Write loop
for i in length:
    file.write('\n')
    file.write(str(int(random.random()*1000)))

file.close()

# Final runtime
end = datetime.now()
print((end - start).total_seconds())