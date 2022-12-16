import random
import hashlib
import Prime

# We will use this class to implement the RSA signature
# To do GCD division and extended GCD for the RSA division

# Funtion to find the GCD of two numbers
def GCD(m, n):
    if n == 0:
        return m
    else:
        r = m % n
        return GCD(n, r)

# Function to find an inverse
def exteuclid(a, b):

    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t

    if t1 < 0:
        t1 = t1 % a

    return r1, t1


def rsa_signature(Message, Private_key, n):
    # Then we will sign it
    Signed_message = pow(Message, Private_key, n)
    # print(Signed_message)
    return Signed_message


def rsa_verify(Signed_Message, public_key, n):
    M1 = pow(Signed_Message, public_key, n)
    # print(M1)
    return M1


def hash512(Message):
    # We need to put our Message as a string to use Hashlib library
    string = str(Message)
    hashed_message = int(hashlib.sha512(string.encode()).hexdigest(), 16)
    return hashed_message


# We will use this function to create RSA key for our user
# Once it is done, we will store them in a variable for each user
def gen_RSA_key():
    # Parameter for RSA public and private key
    p = Prime.prime(512)
    # print(p.bit_length())
    q = Prime.prime(512)
    # print(q.bit_length())
    n = p * q
    Pn = (p-1)*(q-1)

    # print(Pn)

    # Generate encryption key in range 1 < e < Pn
    # e must be an odd number

    while True:
        print('Trying new encryption key')
        e = random.randrange(1, Pn)
        if e%2 == 1:
            print(e)

            # Obtain inverse of e in Z_Pn
            r, d = exteuclid(Pn, e)
            if r == 1:
                d = d
                print(f'Decryption key is {d}')
                break
            else:
                print('Multiplicative inverse for the encryption key does not exist')
        else:
            print(f'{e} is not an odd number')

    # At this point
    # d is the private key
    # (n, e) make the public key

    # Now we want to sign

    print(f'The private key d is equal to {d}')
    print(f'The public key e is equal to {e}')
    print(f'n is equal to {n}')


    Message = 149
    print(f'Initial message is : {Message}')

    # We sign the message with a private key
    Signed_Message = rsa_signature(Message, d, n)
    print(f'The signed message is : {Signed_Message}')

    # We verify with the public key if the hash of the message are similar
    Verify_Message = rsa_verify(Signed_Message, e, n)
    print(f'After verification of the signed message, we get : {Verify_Message}')


    if Message== Verify_Message :
        print('Valid')
        print('Bob can accept Alice Signature')
    else:
        print('Error')


