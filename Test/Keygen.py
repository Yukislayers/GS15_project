import Primal

#Generate a 2048 bit prime number : p
p = Primal.primal()
print("2048 bit prime p is :",p)
print("p has for bit length : ", p.bit_length())

#Now that we got P
#We want to find a generator element of Zp
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

#print(f"Z_p has generators {gen}")