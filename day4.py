"""

Number of valid passports

"""

with open('C:\Principal\Python\Advent of Code\input\day4.txt') as txt:
    data = txt.readlines()


# Organize data by passport and fields
data.append('\n')    
passports = []
x = 0
for i in range(len(data)):
    if data[i] == '\n':
        new_passport = str()
        for item in data[x:i]:
            new_passport = new_passport + ' ' + item
        new_passport = new_passport[1:].split(' ')
        new_passport.sort()
        for k in range(len(new_passport)):
            new_passport[k] = new_passport[k].split(':')
        passports.append(new_passport)
        x = i + 1
    else:
        data[i] = data[i].split('\n')[0]

# Check if passport is valid        
def byr(field):
    field = int(field)
    if field > 1920 and field < 2002:
        return True
    else:
        return False
    
def iyr(field):
    field = int(field)
    if field > 2010 and field < 2020:
        return True
    else:
        return False

def eyr(field):
    field = int(field)
    if field > 2020 and field < 2030:
        return True
    else:
        return False
    
def hgt(field):
    unit = field[-2:]
    field = int(field[:-2])
    if unit == 'cm' and field > 150 and field < 193:
        return True
    if unit == 'in' and field > 59 and field < 76:
        return True
    else:
        return False
    
def hcl(field):
    code = field[1:]
    chars = set(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
    if field[0] == '#' and len(code) == 6 and set(code) <= chars:
        return True
    else:
        return False
    
def ecl(field):
    colours = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    if set([field]) <= colours:
        return True
    else:
        return False
    
def pid(field):
    numbers = set(['0','1','2','3','4','5','6','7','8','9'])
    if len(field) == 9 and set(field) <= numbers:
        return True
    else:
        return False

def is_valid(field_key, field):
    if field_key == 'byr':
        return byr(field)
    if field_key == 'iyr':
        return iyr(field)
    if field_key == 'eyr':
        return eyr(field)
    if field_key == 'hgt':
        return hgt(field)
    if field_key == 'hcl':
        return hcl(field)
    if field_key == 'ecl':
        return ecl(field)
    if field_key == 'pid':
        return pid(field)
        
############################

valid_passports = 0

for passport in passports:
    if len(passport) >= 7:
        for item in passport:
            if item[0] == 'cid' and len(passport) == 7:
                valid = False
                break
            else:
                valid = is_valid(item[0], item[1])
                if valid == False:
                    break
        if valid == True:
            valid_passports += 1
            
        
