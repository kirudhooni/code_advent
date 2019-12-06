
from itertools import groupby


init = 284639
final = 748759
current = init
combinations=0
trueCounter1=0
trueCounter2=0
allCom = []
# print (number[0])
while current != final :
    number = str(current)
    for i in range(len(number)-1):
        if int(number[i+1]) - int(number[i]) >= 0:
            trueCounter1 = trueCounter1 +1
        
        if int(number[i+1]) == int(number[i]):
            trueCounter2 = trueCounter2 +1
            

    if trueCounter1 == 5 and trueCounter2:
        combinations = combinations+1
        allCom.append(current)
    trueCounter1 = 0
    trueCounter2 = 0
    current = current +1
    
print(combinations)

# trueCounter2=0
# #part two
newCombinations=0
for i in range(len(allCom)):
    number = str(allCom[i])
    recordRepeat = []
    for j in range(len(number)-1):
        if int(number[j+1]) == int(number[j]):
            recordRepeat.append(int(number[j+1]))
    test= [len(list(group)) for key, group in groupby(recordRepeat)]
    even_set =0
    for k in range(len(test)):
        if (test[k]+1) == 2:
            even_set =1
    if even_set == 1:
        newCombinations +=1

print(newCombinations)