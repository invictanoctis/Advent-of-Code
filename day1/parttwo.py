leftlist = []
rightlist = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

def assignlist():
    for numbers in lines:
        numbers_seperated = str(numbers).split("   ")
        leftlist.append(numbers_seperated[0])
        rightlist.append(numbers_seperated[1])

def sortlist(list):
    list.sort()

def occurrences():
    sim_score = 0
    prev = None
    last = 0
    for lnumber in leftlist:
        lnumber = int(lnumber)
        if lnumber != prev:
            occ = 0
            for index in range(last, len(rightlist)):
                rnumber = int(rightlist[index])
                if lnumber == rnumber:
                    occ += 1
                elif lnumber != rnumber and occ != 0:
                    last = index
                    break
            sim_score += lnumber * occ
            prev = lnumber
        else:
            sim_score += prev * occ
    return sim_score


if __name__ == '__main__':
    assignlist()
    sortlist(leftlist)
    sortlist(rightlist)
    print(occurrences())