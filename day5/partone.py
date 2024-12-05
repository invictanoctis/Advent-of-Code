import math

instructions = []
updates = []

with open('input.txt', 'r') as file:
    data = file.read().splitlines()
    
def format():
    for line in data:
        if '|' in line:
            instructions.append(line.split('|'))
        elif '' == line:
            continue
        else:
            nline = line.split(',')
            updates.append(nline)

def checkup(update):
    for index, number in enumerate(update):
        for nextindex in range(index, len(update)-1):
            if instructions.count([update[nextindex],number]) > 0:
                return 0
    return update[math.ceil((len(update)/2))-1]
                
def mainloop():
    total = 0
    
    for update in updates:
        total += int(checkup(update))
    
    return total
    

if __name__ == '__main__':
    format()
    print(mainloop())