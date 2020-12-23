"""
PARTS 1 and 2
Find number of valid passwords (character frequency and location)

"""

# Read input file
txt = open('input/day2.txt')
data = txt.readlines()

# Main loop
n_valid_1, n_valid_2 = 0, 0

for line in data:
    # Extract variables
    line = line.split('\n')[0]
    policy, password = line.split(': ')
    limits, char = policy.split(' ')
    least, most = int(limits.split('-')[0]), int(limits.split('-')[1])

    # Check if valid
    # Policy version 1
    char_freq = password.count(char)
    if char_freq >= least and char_freq <= most:
        n_valid_1 += 1
    
    # Policy version 2
    if (password[least-1] == char) != (password[most-1] == char):
        n_valid_2 += 1
        
# Display result
print('Number of valid passwords (part 1): ', n_valid_1)
print('Number of valid passwords (part 2): ', n_valid_2)
