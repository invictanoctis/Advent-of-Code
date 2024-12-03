with open('input.txt', 'r') as file:
    data = file.read()

def findmul(start):
    return data.find('mul(', start)

def findinstruction(start, prev, allowed):
    do = data.find('do()', prev, start)
    dont = data.find("don't()", prev, start)
    
    if do > dont:
        allowed = True
    if dont > do:
        allowed = False
    
    return allowed
    
def testmul(start, res):
    end = data.find(r')', start)
    
    if end - start <= 8:
        print(f'mul an {start} gefunden')
        
        interval = data[start+1:end]
        print(interval)

        if interval.count(',') == 1:
            values = interval.split(',')
            if values[0].isnumeric() and values[1].isnumeric():
                res += int(values[0]) * int(values[1])
                print('added')

    return res            

def mainloop():
    start, prev, res, allowed = 0, 0, 0, True
    
    while True:
        new = findmul(start)
        start = new+3
        
        if new != -1:
            allowed = findinstruction(start, prev, allowed)    
            if allowed is True:
                res = testmul(start, res)
            prev = start
            
        else:
            print("Ende erreicht")
            break
    
    return res
    
    
if __name__ == '__main__':
    print(mainloop())