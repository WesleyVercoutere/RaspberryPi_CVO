'''
import mijn_module2

print("global scope=",dir())

print()

print("scope mijn_module2=",dir(mijn_module2))

print()

print("leeftijd=", mijn_module2.leeftijd)

mijn_module2.check_leeftijd()

'''

# of
'''

from mijn_module2 import check_leeftijd, leeftijd

print(dir())

print()

#print(dir(mijn_module2))  error waarom?


print("leeftijd=", leeftijd)

check_leeftijd()

'''

# of
'''

from mijn_module2 import *

print(dir())

print()

#print(dir(mijn_module2))  error waarom?


print("leeftijd=", leeftijd)

check_leeftijd()

'''



