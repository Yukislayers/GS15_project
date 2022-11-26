import Primal

#Generate a key of 2048 bits for the X3DH.

#This function gives us all the generator of n
def generator(n):
    size = set(range(1, n))
    results = []
    for a in size:
        g = set()
        for x in size:
            g.add((a**x)%n)
            if g == size:
                results.append(a)
    return results

#Generate a 2048 bit prime number
p = Primal.primal()
print("2048 bit prime p is :",p)
print("p has for bit length : ", p.bit_length())

#gen = generator(p)
#print(f"Z_p has generators {gen}")