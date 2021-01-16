"""
Find sum of answered questions by groups

"""

# Read input
with open('input/day6.txt') as txt:
    data = txt.readlines()

# Parse by group answers    
group = []
group_list = []
for k in range(len(data)):
    if data[k] == '\n':
        group_list.append(set(group))
        group = []
    else:
        answer = data[k].split('\n')[0]
        group.append(answer)
group_list.append(group)

# Select each group union and intersection
unions = []
union = set()
intersections = []
intersection = set()

for i in range(len(group_list)):
    k = 0
    for j in group_list[i]:
        union.update(set(j))
        if k == 0:
            intersection = set(j)
        else: 
            intersection.intersection_update(set(j))
        k += 1
        
    unions.append(len(union))
    union = set()
    intersections.append(len(intersection))
    intersection = set()
 
# Show answers 
print(sum(unions), sum(intersections))