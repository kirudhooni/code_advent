import time 

t1 = time.time()

wires = []

with open ('c:/Users/user/Desktop/webDevelopment/Udemy/wires.txt') as f:
    for path in f:
        wires.append(path.strip().split(','))


# print(wires)

store_cart = []
x = 0
y = 0
count =1
cartesian = (0,0)
for wire in wires:
    # print(wire)
    for coordinate in wire:
       #print(coordinate)
        if coordinate[0] == 'R':
            for i in range(int(coordinate[1:])):
               cartesian = (x+i+1, cartesian[1])
               store_cart.append(cartesian)
            x= x+i+1
        if coordinate[0] == 'U':
            for i in range(int(coordinate[1:])):
               cartesian = (cartesian[0], y+i+1)
               store_cart.append(cartesian)
            y = y+i+1
        if coordinate[0] == 'L':
            for i in range(int(coordinate[1:])):
               cartesian = ((x-i-1), cartesian[1])
               store_cart.append(cartesian)
            x= (x-i-1)

        if coordinate[0] == 'D':
            for i in range(int(coordinate[1:])):
               cartesian = (cartesian[0], y-i-1)
               store_cart.append(cartesian)
            y = y-i-1
        
    y=0
    x=0
    cartesian = (0,0)
    if count == 1:
        wire1 = store_cart
        count =0
    
    wire2 = store_cart
    store_cart =[]
# print(wire2)
# print(wire2)

set1 = set(wire1)
set2 = set(wire2)

intersections = set1.intersection(set2)

# print(intersections)
absDist=[]

for intt in intersections:
    absDist.append(abs(intt[0]) + abs(intt[1]))


val = min(absDist)

# print(val)
t2 = time.time()

steps1 = 0
step1Store =[]
steps2 = 0
step2Store =[]
for inter in intersections:
    for cod in wire1:
        steps1 = steps1 + 1
        
        if cod == inter:
            step1Store.append(steps1)
            steps1 =0
            break
    for cod in wire2:
        steps2 = steps2 + 1
        
        if cod == inter:
            step2Store.append(steps2)
            steps2 =0
            break


print(step1Store)
print(step2Store)

final = []
for i in range(len(step1Store)):
    final.append(step1Store[i]+step2Store[i])

print(min(final))




print(t2-t1)
# print(intersections)

# for cod in wire1:
#     for i in range (len(wire2)):
#         if cod == wire2[i]:
#             print (cod)

# print(len(wire1))

# for i in range (len(wire1)):
#     for j in range(len(wire2)):
#         if wire1[i] == wire2[j]:
#             print (wire2[j])
#     print(i)
