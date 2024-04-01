import random

file = open('CSC507/Module2/file2.txt', 'x')
file.write(str(int(random.random()*1000)))
file.close()

length = list(range(1,1000))
file = open('CSC507/Module2/file2.txt', 'a')

for i in length:
    file.write('\n')
    file.write(str(int(random.random()*1000)))

file.close()