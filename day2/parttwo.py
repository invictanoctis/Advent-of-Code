formatted_input = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

def formatlist():
    for line in lines:
        line.replace('/n','')
        formatted_input.append(line.split(' '))

def safetycheck():
    safe_reports = 0
    asc, desc, tol = False, False, False
    
    for report in formatted_input:
        for index in range(len(report)-1):
            dif = int(report[index]) - int(report[index+1])
            
            if int(report[index]) < int(report[index+1]) and desc is False:
                asc = True
                if abs(dif) < 1 or abs(dif) > 3:
                    if tol is False:
                        tol = True
                    else:
                        break
                if index == len(report)-2:
                    safe_reports += 1

            elif int(report[index]) > int(report[index+1]) and asc is False:
                desc = True
                if abs(dif) < 1 or abs(dif) > 3:
                    if tol is False:
                        tol = True
                    else:
                        break
                if index == len(report)-2:
                    safe_reports += 1

            else:
                if tol is False:
                    tol = True
                    
                    if index == len(report)-2:
                        safe_reports += 1
                else:
                    break

        asc = False
        desc = False
        tol = False
        
    return safe_reports


if __name__ == '__main__':
    formatlist()
    print(f'There are: {safetycheck()}')