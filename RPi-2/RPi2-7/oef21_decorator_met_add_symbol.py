import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_greeting():
    print("How are you?")

print("program with @ decorator started!")

say_greeting()  # say_greeting = delay_decorator(say_greeting)  is wat er eigenlijk gebeurt ...

# a decorator is simply a function which wraps another function and gives it some addition functionality or modifies the functionality