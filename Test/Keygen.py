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

#Si j'utilise la fonction, j'ai un probleme de memoire
#Il faut trouver une autre methode que celle en dessous 
#meme si elle fonctionne pour des petits nombres

'''
def generator(n):
    order = n-1
    size = set(range(1, n))
    results = []
    for a in size:
        g = set()
        for x in size:
            g.add((a**x)%n)
            # if we have 1 before x = n-1 then the number will not be a generator
            if ((a**x)%n) == 1 & x != order:
                break
            if g == size:
                results.append(a)
                #we can use a return here to get the first generator element we found
                return results               
        #print(f"iter {a} has g {g}") 
    return results

gen = generator(p)
if gen:
    print(f"Z_p has for a generator {gen}")
'''
