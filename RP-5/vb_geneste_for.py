x= int(input("aantal rijen="))
a=0
for y in range(1, x+1):
    #a=a+y
    for z in range(y):
        a=a+1
        print(a," ", end="")
    print()