import math

def lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b
