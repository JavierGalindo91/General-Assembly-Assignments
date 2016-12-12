
# Integers are Immutable
type(3)
type(int)
dir(int)
a = int()
int.__subclasses__()

a = True
type(a)
type(bool)
dir(a)
a.bit_length()
10.bit_length() # ERROR

(10).bit_length()

a.conjugate()
a.denominator

dir(int) == dir(bool)

a = 3.1415
type(a)
type(float)
dir(a)


type(10*2**40)
type(10*2**400)
import sys
sys.maxint
type(sys.maxint)
type(sys.maxint+1)

# Long Integers have unlimited precision
1000000**10000
# floats do not
2**1000.000000000000000000000000000000001 == float(2**1000)

# floats have a max size
float(100000**1000)

complex()
complex(3, 4)
type(4j)
j # error
3j

# STRINGS
a = 'hello world'
print a




# BINARY OPERATIONS
bin(10)
bin(11)
bin(10 ^ 11)

# WHY USE THIS?


type([])
type(list)
