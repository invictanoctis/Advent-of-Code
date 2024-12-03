with open('input.txt', 'r') as file:
    data = file.read()

def findmul(start):
    return data.find('mul(', start)

def testmul(loc, res):
    end = data.find(r')', loc)
    
    if end - loc <= 8:
        print(f'mul an {loc} gefunden')
        
        interval = data[loc+1:end]
        print(interval)

        if interval.count(',') == 1:
            values = interval.split(',')
            if values[0].isnumeric() and values[1].isnumeric():
                res += int(values[0]) * int(values[1])
                print('added')

    return res            

def mainloop():
    start, res = 0, 0
    
    while True:
        new = findmul(start)
        start = new+3
        
        if new != -1:
            res = testmul(start, res)
            
        else:
            print("Ende erreicht")
            break
    return res
    
    
if __name__ == '__main__':
    print(mainloop())