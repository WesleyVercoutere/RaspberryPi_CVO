#for loops  met range(start,stop,step)   default start = 0 step = 1
#range genereert een lijst met nummers tss start en stop (begint met start en eindigt op stop-1) met eventueel een sprong van grootte “step” ipv +1

for x in range(10):
    print(x)
    
print("******************************")

for x in range(5,10):
    print(x)
    
print("******************************")

for x in range(2,10,2):
    print(x)
    
print("******************************")

for x in range(20,10,-2):
    print(x)
  print("******************************")
for loops  met range(start,stop,step) en else   
for x in range(2,10,2):
    print(x)
else:
    print("else of for..")

#   syntax is => for var in range(start, stop, step):     # stop not included

for x in range(10):
    print(x)
'''    
0
1
2
3
4
5
6
7
8
9
'''
for x in range(5,10):
    print(x)    
'''
5
6
7
8
9
'''
for x in range(5,10,2):
    print(x)    
'''
5
7
9    
'''    
for x in range(25,10,-2):
    print(x)    
'''
25
23
21
19
17
15
13
11
'''
for x in "Welkom in CVO Focus":
    print(x)
