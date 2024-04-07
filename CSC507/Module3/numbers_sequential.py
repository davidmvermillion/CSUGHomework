# Setup
import random
from datetime import datetime

# Datetime counter start
start = datetime.now()

# Create file
file = open('CSC507/Module3/file2.txt', 'x')
file.write(str(int(random.random()*1000)))
file.close()

# Length of loop and change file access type
length = list(range(1,1000000))
file = open('CSC507/Module3/file2.txt', 'a')

# Write loop
for i in length:
    file.write('\n')
    file.write(str(int(random.random()*1000)))

file.close()

# Final runtime
end = datetime.now()
print((end - start).total_seconds())