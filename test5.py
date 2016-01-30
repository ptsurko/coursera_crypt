import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def is_prime(a):
    index = 2
    while index < math.sqrt(a):
        if a % index == 0:
            return False
        index += 1
    return True

def gcde(a, b):
    if a == 0:
        return (b, 0, 1)
    g, x1, y1 = gcde(b % a, a)
    x = y1 - b / a * x1
    y = x1
    return (g, x, y)

def inv(a, b):
    g, x, _ = gcde(a, b)
    return x if g == 1 else None

def exp_ferm(a, b, m):
    if is_prime(m):
        return a ** (b % (m - 1))
    raise Exception('Module %d is not prime number' % m)

def exp_bin(a, b, m):
    power = 1
    result = 1
    temp = a % m
    
    while power <= b:
        if b & power == power:
            result = result * temp % m
        
        temp = temp ** 2 % m    
        power = power << 1
        
    return result

def order(b, m):
    for i in range(1, m):
        if exp_bin(b, i, m) == 1:
            return i
    
def sqrt(a, b, m):   
    for i in range(1, m):
        if exp_bin(i, b, m) == a:
            return i
    return None

assert gcd(5, 35) == 5
assert gcd(6, 35) == 1
assert gcd(7, 23) == 1

assert gcde(7, 23) == (1, 10, -3)

assert inv(7, 23) == 10

assert exp_ferm(2, 10001, 11) == 2

assert is_prime(10) == False
assert is_prime(11) == True
assert is_prime(125) == False
assert is_prime(127) == True

assert exp_bin(2, 10001, 11) == 2

assert sqrt(7, 3, 11) == 6
assert sqrt(3, 2, 11) == 5
assert sqrt(1, 3, 11) == 1
assert sqrt(2, 2, 11) == None

assert order(2, 35) == 12

print len([i for i in range(35) if gcd(i, 35) == 1])



