p = 29
ints = [14, 6, 9]

for a in  range(1, p):
	if a**2 % p in ints:
		print(a**2 % p)

# 6 is a quadratic residue mod 29 because 8^2 = 64 and 64 % 29 = 6
# root of 6 mod 29 is 8
