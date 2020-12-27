"""

Boarding pass

"""
from operator import sub


with open('input/day5.txt') as txt:
    data = txt.readlines()

def row(code):
    row_number = 0
    interval = 128
    for char in code:
        if char == 'B':
            row_number += interval/2
        interval /= 2
    return int(row_number)

def col(code):
    col_number = 0
    interval = 8
    for char in code:
        if char == 'R':
            col_number += interval/2
        interval /= 2
    return int(col_number)

def row_col(boarding_pass):
    row_code = boarding_pass[0:7]
    col_code = boarding_pass[7:10]
    return row(row_code), col(col_code)

def missing_seat(seat_ids):
    seat_ids.sort()
    first_seat = seat_ids[0]
    seats = len(seat_ids)
    compare = list(range(first_seat, first_seat + seats))
    compare = list(map(sub, seat_ids, compare))
    missing_seat_id = seat_ids[compare.index(1)] - 1
    return missing_seat_id
    

seat_ids = []    
for i in range(len(data)):
    data[i] = row_col(data[i])
    id = 8*data[i][0] + data[i][1]
    seat_ids.append(id)
 
max_id = max(seat_ids)
print(max_id)

print(missing_seat(seat_ids))