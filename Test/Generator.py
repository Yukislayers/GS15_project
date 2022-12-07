from Crypto.Util import number

#Only for test, not used

#https://crypto.stackexchange.com/questions/9006/how-to-find-generator-g-in-a-cyclic-group

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
                #return results               
        #print(f"iter {a} has g {g}") 
    return results

for i in range(30):
    gens = generator(i)
    if gens:
        print(f"Z_{i} has generators {gens}")
