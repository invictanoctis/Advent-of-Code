with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

def checkx(num, index):
    chval = 0
    
    # boundaries
    if (
        num + 1 <= len(lines)-1 and
        num - 1 >= 0 and
        index + 1 <= len(lines[num])-1 and
        index - 1 >= 0
    ):
        # top
        if (
            lines[num + 1][index - 1] == 'S' and
            lines[num + 1][index + 1] == 'S' and
            lines[num - 1][index + 1] == 'M' and
            lines[num - 1][index - 1] == 'M'
        ):
            chval += 1
        
        # right
        if (
            lines[num + 1][index - 1] == 'S' and
            lines[num + 1][index + 1] == 'M' and
            lines[num - 1][index + 1] == 'M' and
            lines[num - 1][index - 1] == 'S'
        ):
            chval += 1
        
        # bottom
        if (
            lines[num + 1][index - 1] == 'M' and
            lines[num + 1][index + 1] == 'M' and
            lines[num - 1][index + 1] == 'S' and
            lines[num - 1][index - 1] == 'S'
        ):
            chval += 1
        
        # left
        if (
            lines[num + 1][index - 1] == 'M' and
            lines[num + 1][index + 1] == 'S' and
            lines[num - 1][index + 1] == 'S' and
            lines[num - 1][index - 1] == 'M'
        ):
            chval += 1
            
    return chval
        
def mainloop():
    total = 0
    
    for num in range(len(lines)):
        for index in range(len(lines[num])):
            if lines[num][index] == 'A':
                total += checkx(num, index)
    
    return total


if __name__ == '__main__':
    print(mainloop())