import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

def say_greeting():
    print("How are you?")

print("program started!")

decorated_function = delay_decorator(say_greeting)
decorated_function()

# a decorator is simply a function which wraps another function and gives it some addition functionality or modifies the functionality