import Primal
import os

#Generate a 2048 bit prime number : p
#We will store this number in a file so we don't do it every time

if not (os.path.isfile('Test/primal.txt')):
    p = Primal.primal()
    file = open("Test/primal.txt", "w")
    file.write(str(p))
    file.close()

f = open("Test/primal.txt", "r")
p = int(f.read())
print("2048 bit prime p is :",p)
print("p has for bit length : ", p.bit_length())

#Now that we got P
#We want to find a generator element of Zp


#This function gives us all the generator of n

#Si j'utilise la fonction, j'ai un probleme de memoire
#Il faut trouver une autre methode que celle en dessous 
#meme si elle fonctionne pour des petits nombres

# https://medium.com/asecuritysite-when-bob-met-alice/the-cyclic-group-g-of-order-p-f9688dc9cc27
# a essayer

#Dans le corps Zm de taille m avec m premier, il existe au moins un element a d'ordre w=m-1
'''
def generator(p):
    size = set(range(1, n))
    results = []
    for a in size:
        g = set()
        for x in size:
            g.add((a**x)%n)
            if g == size:
                results.append(a)
    return results
'''

#print(f"Z_p has generators {gen}")