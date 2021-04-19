class Test:
    teller = 100  # teller is een class attribute


t1 = Test()

print("0", t1.teller)  # het object t1 kan de class variabele teller lezen

print("1", dir())
print("2", dir(Test))

print("3", dir(t1))
print("4", t1.__dict__)
