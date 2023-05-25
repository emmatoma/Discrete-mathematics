#!/usr/bin/env python
# coding: utf-8

# In[21]:


###euclidian algoythm
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
        print(x,y)
    return x


# In[22]:


648*2


# In[23]:


gcd(533,377)


# In[6]:


234/24


# In[8]:


24*9


# In[9]:


234-216


# In[24]:


#extended euclidian algorythm
def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    
    x = y1 - (b//a) * x1
    
    y = x1
    print(y1,"-",b,"div",a,"=",(b//a),"*",x1)
    print(gcd, "=",x,",",y) 
    return gcd,x,y
     
 
# Driver code
a, b = 533,377
g, x, y = gcdExtended(a, b)
print("gcd(", a , "," , b, ") = ", g)


# In[3]:


from math import *

def euclid_algo(x, y, verbose=True):
	if x < y: #  x >= y
		return euclid_algo(y, x, verbose)
	print()
	while y != 0:
		if verbose: print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
		(x, y) = (y, x % y)
	
	if verbose: print('MCD is %s' % x) 
	return x


euclid_algo(1111 , 111111)



# In[21]:


euclid_algo(15,8)

gcdExtended(15,8)


# In[23]:


euclid_algo(123,10)

gcdExtended(123,10)


# In[34]:


12*3


# In[35]:


euclid_algo(888,54)

gcdExtended(888,54)


# In[41]:


p = 13
q = 19
e = 11
C =207

# Calculamos n y phi(n)
n = p*q
phi_n = (p-1) * (q-1)

# Encontramos el inverso multiplicativo de e módulo phi(n)
# utilizando el algoritmo extendido de Euclides
r0, r1 = phi_n, e
s0, s1 = 1, 0
t0, t1 = 0, 1

while r1 != 0:
    q = r0 // r1
    r = r0 % r1
    s = s0 - q * s1
    t = t0 - q * t1
    print(f"q: {q}, r: {r}, s: {s}, t: {t}")
    r0, r1 = r1, r
    s0, s1 = s1, s
    t0, t1 = t1, t

d = s0 % phi_n

# Desciframos el mensaje
M = pow(C, d, n)

# Imprimimos el resultado
print("El mensaje original es:", M)


# In[5]:


def decrypt_message(c, e, n):
    # Calculate the value of d
    d = pow(e, -1, n-1)
    # Decrypt the message
    m = pow(c, d, n)
    return m
c =   # the encrypted message
e = 7  # the public exponent
n = 221  # the modulus
m = decrypt_message(c, e, n)
print("The decrypted message is:", m)


# In[4]:


dividend = -111
divisor = 589

inverse = pow(dividend, -1, divisor)

print(f"The multiplicative inverse of {dividend} modulo {divisor} is: {inverse}")


# In[11]:


dividend = -110
divisor = 327

# Step 1: Calculate the remainder
remainder = dividend % divisor

# Step 2: Find the multiplicative inverse of the remainder modulo 589
multiplicative_inverse = None
for x in range(1, divisor):
    if (remainder * x) % divisor == 1:
        multiplicative_inverse = x
        break

# Step 3: Check if the multiplicative inverse exists and print the result
if multiplicative_inverse is not None:
    print(f"The multiplicative inverse of {dividend} modulo {divisor} is: {multiplicative_inverse}")
else:
    print(f"The multiplicative inverse of {dividend} modulo {divisor} does not exist.")


# In[18]:


###this is a good checker to see if you find the multiplicative inverse (works with negatives)
result = -110 * 217 % 327

print(result)


# In[9]:


def is_mersenne_prime(p):
    if p == 2:
        return True

    mersenne_number = 2 ** p - 1
    s = 4

    for _ in range(p - 2):
        s = (s ** 2 - 2) % mersenne_number

    return s == 0

# Example usage
number = 8191
is_prime = is_mersenne_prime(number)

if is_prime:
    print(f"{number} is a Mersenne prime.")
else:
    print(f"{number} is not a Mersenne prime.")


# In[13]:


def find_multiplicative_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

modulus = 1231
number = 511

multiplicative_inverse = find_multiplicative_inverse(number, modulus)

if multiplicative_inverse is not None:
    print(f"The multiplicative inverse of {number} modulo {modulus} is {multiplicative_inverse}.")
    result = (number * multiplicative_inverse) % modulus
    print(f"Verifying: ({number} * {multiplicative_inverse}) % {modulus} = {result}")
else:
    print(f"The multiplicative inverse of {number} modulo {modulus} does not exist.")


# In[27]:


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        print(f"{x} * {a} + {y} * {b}")
        return gcd, y, x - (a // b) * y

num1 = 377
num2 = 533

gcd, coeff1, coeff2 = extended_gcd(num1, num2)

print("GCD:", gcd)
print("Linear Combination:", coeff1, "*", num1, "+", coeff2, "*", num2)


# In[30]:


def discrete_log(base, target, modulo):
    result = 1
    for x in range(modulo):
        result = (result * base) % modulo
        if result == target:
            return x
    return None

base = 5
target = 9
modulo = 23

logarithm = discrete_log(base, target, modulo)

if logarithm is not None:
    print("El logaritmo discreto de", target, "base", base, "módulo", modulo, "es", logarithm)
else:
    print("No se encontró un logaritmo discreto para", target, "base", base, "módulo", modulo)


# In[39]:


###calcular logaritmo discreto
dividend = 3 **10
divisor = 29

remainder = dividend % divisor

print("Remainder:", remainder)


# In[ ]:




