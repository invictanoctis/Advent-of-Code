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
    list = list.sort()

def difference():
    max_dif = 0
    for index in range(len(leftlist)):
        dif = int(leftlist[index]) - int(rightlist[index])
        max_dif += abs(dif)
    return max_dif


if __name__ == '__main__':
    assignlist()
    sortlist(leftlist)
    sortlist(rightlist)
    print(difference())