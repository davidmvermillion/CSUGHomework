import random

# Create file
def file_init():
    file = open('CSC507/Module6/file3.txt', 'x')
    file.write(str(int(random.random()*10000)))
    file.close()

file_init()