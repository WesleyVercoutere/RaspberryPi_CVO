class Test:
    teller = 100  # teller is een class attribute


t1 = Test()

print("0", t1.teller)  # het object t1 kan de class variabele teller lezen

print("1", dir())
print("2", dir(Test))

print("3", dir(t1))
print("4", t1.__dict__)
print("5", Test.__dict__)

t1.teller = 200

print("6", t1.teller)  # het object t1 kan de class variabele teller lezen

print("7", dir())
print("8", dir(Test))

print("9", dir(t1))
print("10", t1.__dict__)
print("11", Test.__dict__)
