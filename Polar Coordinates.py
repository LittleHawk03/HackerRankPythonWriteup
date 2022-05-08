

from cmath import phase
import cmath


num = complex(input())
z = complex(num)

print(cmath.polar(z)[0])
print(phase(z))