"""

Find pair of numbers which sum 2020

"""

import pandas as pd
import numpy as np

# Read input
numbers = pd.read_csv('input/day1.txt', header=None)
numbers = list(numbers[0])

# Classify numbers by last digit
# Create empty list
groups = []
for i in range(10):
    groups.append([])

# Classify    
for n in numbers:
    last_digit = int(str(n)[-1])
    groups[last_digit].append(n)

# Calculate possible combinations (last digits sum 10) and search for 2020
def search_2020():
    for i in range(6):
        x = i
        y = (10-x) % 10
        for k in range(len(groups[x])):
            for l in range(len(groups[y])):
                n1 = groups[x][k]
                n2 = groups[y][l]
                sum_xy = n1 + n2
                if sum_xy == 2020:
                    return n1, n2

# Display solution                
n1, n2 = search_2020()
print(n1,' + ',n2,' = ', n1+n2)
print(n1, ' * ', n2, ' = ', n1*n2)                    