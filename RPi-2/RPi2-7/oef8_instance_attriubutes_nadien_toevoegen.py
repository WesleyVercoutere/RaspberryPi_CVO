class Test:
    teller = 200

    def test_say_hello(self):
        print("hello from Test, p=", self)


t1 = Test()

t1.name = "Wim"
t1.lastname = "Verlinden"

print("1", dir(t1))
print("2", t1.__dict__)