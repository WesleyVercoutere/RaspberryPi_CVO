class Test:
    teller = 200

    def test_say_hello(p=None):
        print("hello from Test, p=", p)


t1 = Test()
t2 = Test()

t1.test_say_hello()
t2.test_say_hello()