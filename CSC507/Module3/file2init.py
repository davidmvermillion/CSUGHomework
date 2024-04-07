import random

# Create file
def file_init():
    file = open('CSC507/Module3/file2.txt', 'x')
    file.write(str(int(random.random()*1000)))
    file.close()

file_init()