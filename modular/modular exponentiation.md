**c = b^e (mod m)**

to find the remainder without calculating full massive c^e.


**Manual Method *(Property of Multiplication)*** *("reduce" the number at every single step.)*

(AxB) (mod m) = \[(A (mod m)) x (B (mod m))] (mod m)



eg: 	3^4 (mod 5)

&nbsp;	3^3 mod 5 = (3^2 mod 5 x 3 mod 5 ) mod 5 = (9mod5 x 3mod5) mod5

&nbsp;			    = (4 x 3)mod5 = 12mod5 = 2

&nbsp;	3^4 mod 5 = (3^3 mod 5 x 3 mod 5 ) mod 5

&nbsp;			    = (2mod5 x 3)mod5 = 6mod5 = 1





**Binary Exponentiation *(Square-and-Multiply)***

use the binary representation of the exponent.



eg: 	3^13 (mod 7)

&nbsp;			13 = 2^3+2^2+2^0 = 8 + 4 + 1

&nbsp;			3^13 = 3^8 x 3^4 x 3^1

&nbsp;		3mod7 = 3

&nbsp;		3^2mod7 = 9mod7  = 2

&nbsp;		3^4mod7 = 2^2mod7 = 4

&nbsp;		3^8mod7 = 4^2mod7 = 16mod7 = 2

&nbsp;	3^13mod7 = (3^8mod7 x 3^4mod7 x 3mod7) mod7

&nbsp;		= 2\*4\*3 mod7 = 24 mod 7 = 3





**Fermat's Little Theorem *(prime exponent)***

a^p = a (mod p)    <==>    a^p-1 = 1 (mod p)





**Negative Remainders**

12mod13 = (-1)^2 = 1

