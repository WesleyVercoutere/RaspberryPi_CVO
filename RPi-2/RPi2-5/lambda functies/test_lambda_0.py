# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

# vb 1 
x = lambda a : a + 10
print(x(5))

# vb 2
x = lambda a, b : a * b
print(x(5, 6))

# vb 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# vb 3
#x = lambda a, b, c : "hallo"
#print(x(5, 6, 2))

# vb 4
x = lambda a="nothing", b="nothing", c="nothing" : a+b+c+"hallo"
print(x())
