leftlist = []
rightlist = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
def assignlist():
    for numbers in lines:
        numbers_seperated = str(numbers).split("   ")
        leftlist.append(numbers_seperated[0])
        rightlist.append(numbers_seperated[1])

def occurances():
    sim_score = 0
    for lnumber in leftlist:
        occ = 0
        for rnumber in rightlist:
            if int(lnumber) == int(rnumber):
                occ += 1
        sim_score += int(lnumber) * occ
    return sim_score


if __name__ == '__main__':
    assignlist()
    print(occurances())