def extended_gcd(a, b):
  if b == 0:
    return a, 1, 0
  
  gcd, x1, y1 = extended_gcd(b, a % b)

  # BACKTRAKCING
  x = y1
  y = x1 - (a // b) * y1

  return gcd, x, y


# GCD OF 35 AND 15
a, b = 35, 15
    gcd, x, y = extended_gcd(a, b)
    
    print(f"Extended GCD of {a} and {b}:")
    print(f"GCD = {gcd}")
    print(f"Coefficients: x = {x}, y = {y}")
    print(f"Verification: {a}*({x}) + {b}*({y}) = {a*x + b*y}")
    print()

# MODUALR MULTIPLICATIVE INVERSE OF 3 MOD 11 
a, m = 3, 11
gcd, x, y = extended_gcd(a, m)

if gcd == 1:
  # x is modular inverse of a
  inv = x % m
  print(f"Multiplicative inverse of {a} mod {m} is: {inv}")
  print(f"Verification: ({a} * {inv}) mod {m} = {(a * inv) % m}")
else:
  print(f"No multiplicative inverse (GCD = {gcd})")
