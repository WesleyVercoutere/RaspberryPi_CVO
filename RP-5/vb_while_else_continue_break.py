#meeste gebruikte vorm
teller=3
while teller < 5:
    print("teller=",teller)
    teller+=1
    
# andere mogelijkheden

teller=3
while teller < 5:
    print("teller=",teller)
    teller+=1
else:
    print("nu in else...")
    print("teller=",teller)
print(":-)")

teller=0
while teller < 10:
    teller+=1
    if teller%2==0:
        continue
    print("teller=",teller)
else:
    print("while else1")
print("finished1")


teller=0
while teller < 10:
    teller+=1
    if teller%2==0:
        break
    print("teller=",teller)
else:
    print("while else2")
print("finished2")

