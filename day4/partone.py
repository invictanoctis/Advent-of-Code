with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

def vertical(num, index):
    chval = 0
    
    if index + 3 <= len(lines[num])-1: # boundaries
        if lines[num][index + 1:index + 4] == 'MAS':
            chval += 1

    if index - 3 >= 0: # boundaries
        if lines[num][index - 3: index] == 'SAM':
            chval += 1
    
    return chval
            
def horizontal(num, index):
    chval = 0
    
    if num + 3 <= len(lines)-1: # boundaries
        if (
            lines[num + 1][index] == 'M' and
            lines[num + 2][index] == 'A' and
            lines[num + 3][index] == 'S'
        ):
            chval += 1
    
    if num - 3 >= 0: # boundaries
        if ( 
            lines[num - 1][index] == 'M' and
            lines[num - 2][index] == 'A' and
            lines[num - 3][index] == 'S'
        ):
            chval += 1
        
    return chval

def diagonal(num, index):
    chval = 0
    
    # top to bottom right
    if index + 3 <= len(lines[num])-1 and num + 3 <= len(lines)-1: # boundaries
        if (
            lines[num + 1][index + 1] == 'M' and
            lines[num + 2][index + 2] == 'A' and
            lines[num + 3][index + 3] == 'S'
        ):
            chval += 1
    
    # top to bottom left
    if index - 3 >= 0 and num + 3 <= len(lines)-1: # boundaries
        if (
            lines[num + 1][index - 1] == 'M' and
            lines[num + 2][index - 2] == 'A' and
            lines[num + 3][index - 3] == 'S'
        ):
            chval += 1
    
    # bottom to top right
    if index + 3 <= len(lines[num])-1 and num - 3 >= 0: # boundaries
        if (
            lines[num - 1][index + 1] == 'M' and
            lines[num - 2][index + 2] == 'A' and
            lines[num - 3][index + 3] == 'S'
        ):
            chval += 1
    
    # bottom to top left
    if index - 3 >= 0 and num - 3 >= 0: # boundaries
        if (
            lines[num - 1][index - 1] == 'M' and
            lines[num - 2][index - 2] == 'A' and
            lines[num - 3][index - 3] == 'S'
        ):
            chval += 1
    
    return chval

def mainloop():
    total = 0
    
    for num in range(len(lines)):
        for index in range(len(lines[num])):
            if lines[num][index] == 'X': # nur wenn x fuer runtime und complexitaet
                total += (
                    vertical(num, index) + 
                    horizontal(num, index) +
                    diagonal(num, index)
                )
    
    return total


if __name__ == '__main__':
    print(mainloop())