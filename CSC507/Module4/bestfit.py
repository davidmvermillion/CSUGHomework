# Program to simulate Best Fit Algorithm Memory Allocation
# Source: https://www.geeksforgeeks.org/program-best-fit-algorithm-memory-management/

# Define Block Sizes
blocks1 = [300, 313, 42, 209, 2019]
blocks2 = [300, 313, 42, 209, 2019]
blocks3 = [300, 400, 500, 350, 2019]

# Define Process Sizes
processes1 = [42, 73, 281, 182, 200]
processes2 = [10, 20, 30, 40, 50]
processes3 = [40, 75, 300, 200, 100]

# Define Best Fit Algorithm
def BestFit(blocks, processes):
    blocksize = len(blocks)
    processsize = len(processes)
    allocation = [-1] * processsize
    
    for i in range(processsize):
        BestFitIndex = -1
        for j in range(blocksize):
            if blocks[j] >= processes[i]:
                if BestFitIndex == -1:
                    BestFitIndex = j
                elif blocks[BestFitIndex] > blocks[j]:
                    BestFitIndex = j
        if BestFitIndex != -1:
            allocation[i] = BestFitIndex
            blocks[BestFitIndex] -= processes[i]

    print('\nGiven process sizes of: ', processes,
          '\nBlock sizes of:         ', blocks,
          '\nAllocations were:       ', allocation)

# Run results for 3 variations
BestFit(blocks1, processes1)
BestFit(blocks2, processes2)
BestFit(blocks3, processes3)