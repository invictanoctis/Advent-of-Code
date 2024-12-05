import math

instructions = []
updates = []
incorrect = []

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

def filter():
    for update in updates:
        for index, number in enumerate(update):
            for nextindex in range(index, len(update)-1):
                if instructions.count([update[nextindex],number]) > 0:
                    incorrect.append(update)

def sort(): # manchmal nicht richtiges total?! race condition oder so ne scheisse ohne ueberhaupt async zu haben, naja fick meinen bubble sort gay ahh
    total = 0
    
    for line in incorrect:
        for index in range(len(line)-1):
            for num in range(len(line)-1, index, -1):
                if instructions.count([line[num-1],line[num]]) > 0:
                    line[num], line[num-1] = line[num-1], line[num]
        print(line)
        total += int(line[math.ceil((len(line)/2))-1])
        
    return total
    

if __name__ == '__main__':
    format()
    filter()
    print(sort())
    