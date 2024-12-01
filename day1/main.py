leftlist = []
rightlist = []

with open('input.txt', 'r') as file:
    lines = file.readlines() # speichert jede Zeile als object in einer liste


def assignlist():
    for numbers in lines:
        numbers_seperated = str(numbers).split("   ") # macht eine Liste aus jeder Zeile, Trennung an 3 leerzeichen
        leftlist.append(numbers_seperated[0])
        rightlist.append(numbers_seperated[1])

def sortlist(list): # bisschen unnoetig aber who cares
    list = list.sort()

def difference():
    max_dif = 0
    for index in range(len(leftlist)):
        dif = int(leftlist[index]) - int(rightlist[index])
        max_dif += abs(dif) # macht positiv und fuegt zur max dif hinzu
    return max_dif

if __name__ == '__main__':
    assignlist()
    sortlist(leftlist)
    sortlist(rightlist)
    print(difference())

# pythonic ahhhh loesung lol