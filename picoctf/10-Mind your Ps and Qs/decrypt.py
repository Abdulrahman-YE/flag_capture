import math
from Crypto.Util.number import long_to_bytes


"""
Function to if a number is a perfect square
(A perfect square is a positive integer that is obatined by multiplying an integer by itself)
@params:
    positive_int : The number to check if it perfect square
@return
    True : if positive_int is a perfect square
    False : otherwise
"""
def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2

c= 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n= 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e= 65537
# Using factor db
p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003

phi = (p-1) * (q - 1)

d = pow(e, -1, phi)

m = pow(c, d, n)
print(long_to_bytes(m))
