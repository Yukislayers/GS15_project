import Primal
import os

#Generate a 2048 bit prime number : p
#We will store this number in a file so we don't do it every time

if not (os.path.isfile('Test/prime.txt')):
    p = Primal.primal()
    file = open("Test/prime.txt", "w")
    file.write(str(p))
    file.close()

f = open("Test/prime.txt", "r")
p = int(f.read())
print("2048 bit prime p is :",p)
print("p has for bit length : ", p.bit_length())


#Now that we got P
#We want to find a generator element of Zp

#Si j'utilise la fonction, j'ai un probleme de memoire
#Il faut trouver une autre methode que celle en dessous 
#meme si elle fonctionne pour des petits nombres

'''
def generator(n):
    order = n-1
    size = set(range(1, n))
    results = []
    g = set()
    for a in range(10):
        for x in size:
            g.add((a**x)%n)
            # if we have 1 before x = n-1 then the number will not be a generator
            if ((a**x)%n) == 1 & x != order:
                print(f"iter {a}")
                break
            if g >= 10000000000000:
                results.append(a)
                #we can use a return here to get the first generator element we found
                #return results               
        #print(f"iter {a} has g {g}") 
    return results

gen = generator(p)
if gen:
    print(f"Z_p has for a generator {gen}")

'''

#Apres avoir des recherches, il est ecrit que pour faire du DH, il n'est pas necessaire de choisir g avec g un element generateur de notre corps Zp, on peut normalement le choisir 
#au hasard, le seul interet de choisir g avec g un element generateur de notre groupe Zp est d'avoir un groupe assez grand
#Je pense donc qu'on peut choisir 2 et on aura un groupe suffisament grand pour ne pas avoir de probleme

g = 2