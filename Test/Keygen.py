import Prime
import os
import random

# Generate a 2048-bit prime number : p
# We will store this number in a file, so we don't do it every time

Valid = False
counter = 0

if not (os.path.isfile('prime.txt')):
    print('We will generate a new safe prime number')
    while not Valid:
        print('We try a new prime number')
        counter += 1
        print(f'iter : {counter}')
        # We will try with a library first
        p = Prime.prime()
        # the line below is a known safe prime
        # p = (2**2048) - 1942289
        print(f'p : {p}')
        p_minus = p-1
        # print(p_minus)

        if p_minus % 2 == 0:
            print('We will now see if q = (p-1)/2 is prime')
            q = p_minus//2
            if Prime.isMillerRabinPassed(q):
                print(f'q : {q}')
                print('q is prime')
                Valid = True
            else:
                print('q is not prime')
        else:
            print('p-1 is not equal to 2q')
        file = open("prime.txt", "w")
        file.write(str(p))
        file.close()
else:
    print('We already have a safe prime number generated')

f = open("prime.txt", "r")
p = int(f.read())
print("2048 bit prime p is :", p)
print("p has for bit length : ", p.bit_length())

# Now that we have our safe prime
# We know the only divisor are 1, 2, q and p-1
# We will generate a random number a and see if a**[1, 2, q, p-1] mod p = 1

p_minus = p - 1
q = p_minus // 2
counter = 0

if not (os.path.isfile('generator.txt')):
    print('We will find a generator of our cyclic group')
    while True:
        counter += 1
        print(f'iter : {counter}')
        g = random.randrange(1, p)
        print(f'We are testing : {g}')
        # pour l'utilisation de pow : https://stackoverflow.com/questions/57668289/implement-the-function-fast-modular-exponentiation
        if pow(g, 1, p) != 1 and pow(g, 2, p) != 1 and pow(g, q, p) != 1 and pow(g, p_minus, p) == 1:
            print(f'It is a generator or our cyclic group Zp')
            file = open("generator.txt", "w")
            file.write(str(g))
            file.close()
            break
        else:
            print(f'It is not a generator of our group Zp')
else:
    print('We already have a generator of our cyclic group')

f = open("generator.txt", "r")
g = int(f.read())
print(f'The generator of our cyclic group is : {g}')


print('We now have a prime p of 2048-bit and g, a generator of Zp')
