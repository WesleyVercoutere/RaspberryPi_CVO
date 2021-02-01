'''
print(help)

geeft

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''

print("default end parameter is newline...")

print("aanpassen regeleinde naar 2 sterretjes!", end="**")

print("waar komt dit en waarom", end="\n\n")

print("Deze lijn?")

print("Verschillende items", "default gescheiden door" , "een spatie")

print("Verschillende items", "default gescheiden door" , "een spatie", "maar andere opties via sep parameter", sep="@$@$")



