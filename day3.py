"""

Find number of encountered trees

"""

# Read input
txt = open('input/day3.txt')
data = txt.readlines()

for i in range(len(data)):
    data[i] = data[i].split('\n')[0]


# Solve
def count_trees(x_step, y_step):
    "Returns number of encountered trees given a slope"
    length = len(data[0])
    n_trees = 0
    loc = 0
    for i in range(0, len(data), y_step):
        char = data[i][loc]
        if char == '#':
            n_trees += 1
        loc = ( loc + x_step ) % length
    
    return n_trees

slopes = [[1,1],
          [3,1],
          [5,1],
          [7,1],
          [1,2]]

trees = 1

for slope in slopes:
    trees *= count_trees(slope[0], slope[1])
    
print(trees)