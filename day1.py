"""
PART 1
Find two numbers that sum 2020

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
print('Found two numbers')
print('Numbers: ', n1, n2)
print('Product: ', n1*n2)   


"""

PART 2
Find three numbers that sum 2020

"""   

# Create array with labeld numbers (number, even/odd, last digit)  
last_digit = []
for n in numbers:
    last_digit.append(int(str(n)[-1]))     
even_odd = list(np.mod(numbers, 2))
df = {'number':numbers, 'even_odd':even_odd, 'digit':last_digit}
df = pd.DataFrame(df)

# Separate even and odd numbers
even = df[df['even_odd'] == 0]
odd = df[df['even_odd'] == 1]

# Search both possibilities (even, even, even) and (odd, odd, even)
def search_even_even_even():
    for a in even['number']:
        for b in even[ even['number'] < (2020-a) ]['number']:
            c = 2020 - a - b
            if c in even['number'].values:
                print('Found three numbers')
                print('Numbers: ', a, b, c)
                print('Product: ', a*b*c)
                return a, b, c

def search_odd_odd_even():
    for a in odd['number']:
        for b in odd[ odd['number'] < (2020-a) ]['number']:
            c = 2020 - a - b
            if c in even['number'].values:
                print('Found three numbers')
                print('Numbers: ', a, b, c)
                print('Product: ', a*b*c)                
                return a, b, c

search_even_even_even()
search_odd_odd_even()