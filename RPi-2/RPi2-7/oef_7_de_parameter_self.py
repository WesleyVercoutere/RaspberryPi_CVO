class Test:
    teller = 200

    def test_say_hello(self):
        print("hello from Test, p=", self)


t1 = Test()

t1.test_say_hello()
Test.test_say_hello()
