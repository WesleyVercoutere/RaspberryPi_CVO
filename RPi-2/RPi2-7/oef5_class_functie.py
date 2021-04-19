class Test:
    teller = 200

    def test_say_hello():
        print("hello from Test")


t1 = Test()

test_say_hello()

Test.test_say_hello()

t1.test_say_hello()




