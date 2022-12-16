import os
import random
from Bob import *
from Server import *
from Signature import *

# This will be the class of the first person to talk


class Alice:
    if not (os.path.isfile('prime.txt')):
        print('You need to first generate a prime number')
        exit()

    f = open("prime.txt", "r")
    p = int(f.read())
    f.close()

    f = open("generator.txt", "r")
    g = int(f.read())
    f.close()

    if not (os.path.isfile('generator.txt')):
        print('You need to first find a generator of our cyclic group')
        exit()

    name = 'Alice'

    # Generate Alice IDa key pair
    IDa_priv = 10
    IDa_pub = pow(g, IDa_priv, p)

    # Generate Alice signed pre key
    # This is the key that should be re-generated every few weeks
    SPKa_priv = 20
    SPKa_pub = pow(g, SPKa_priv, p)

    hashed_SPKa_pub = hash512(SPKa_pub)

    # For the one-time prekeys, we choose a random number
    OTPKa_priv = 30
    OTPKa_pub = pow(g, OTPKa_priv, p)

    # For the ephemeral key, we choose a random number
    a = random.randrange(1, p)
    EKa = pow(g, a, p)

    # RSA key pair
    # Generated with Signature.py file
    RSAa_priv = 63876487815647514170700786872553424646175147520844601190629520777528041708949271733982563022011514046110456874591233238339729417809653304250544327388299640003938824871044884116899846502784646702713714181735365476192281617455187058709555993374723415560395650650786850995919145344427812499768792164403114630723
    RSAa_pub = 49642280304406183040258777691786381609976842941924843955894888172173866054911266338384387534442339754504928584434007720798371076432289079844504941330337431425268407193578589113655357700654293155871491683216102084271545027619893411277578483250481467401481272788070102835208564793517478208516895305276888967251
    RSAa_modulo = 88068270365962917055293150267727212750764582867753083804320845015734418624122471647835983161864625889411666451395391812186761964722418458626397745627220556728433375773380250064084468195371558487955547812763052847977496208757699627312896586214402523963412052854997794847952017238886309046262885749831661071021

    # We create the prekey signature by signing the signed pre key with Alice private key
    # We will use the rsa signature
    SPKa_sig = rsa_signature(hashed_SPKa_pub, RSAa_priv, RSAa_modulo)

    # The shared key will be updated later
    shared_key = 0


# We create the server and Bob, so we can put the information on the server for the x3dh exchange
server = Server()
alice = Alice()
bob = Bob()

# We publish the key bundles on the server
server.set_alice(alice.IDa_pub, alice.hashed_SPKa_pub, alice.SPKa_sig, alice.OTPKa_pub, alice.RSAa_pub, alice.RSAa_modulo)
server.set_bob(bob.IDb_pub, bob.hashed_SPKb_pub, bob.SPKb_sig, bob.OTPKb_pub, bob.RSAb_pub, bob.RSAb_modulo)

# We need to fetch the bundle and check if the signature of Bob SPK is valid

if rsa_verify(server.SPKb_sig, server.RSAb_pub, server.RSAb_modulo) == server.SPKb:
    print('Valid signature')
    print('Do X3DH')
else:
    print('Error')


'''
# Communication method for the moment
print('You are : ' + Alice.name)

friend = input("Please enter the name of the person you want to talk to : ")

print('You are going to talk to : ' + friend)

file = Alice.name + '_' + friend + '.txt'
revfile = friend + '_' + Alice.name + '.txt'

#Verify if a text file between the two already exists
if not (os.path.isfile(file)) and not (os.path.isfile(revfile)):
    f = open(file, "w")
    print('File between ' + Alice.name + ' and ' + friend + ' is created !')
    f.write("start of the conversation between " + Alice.name + " and " + friend)
    f.close()
else:
    print('File between ' + Alice.name + ' and ' + friend + ' already exists !')

mydir = Alice.name + '_dir'
friend_dir = friend + '_dir'

#Create folder to share files 
if not (os.path.isdir(mydir)):
    os.mkdir(mydir)
    print(mydir + ' folder is created')
else:
    print(friend_dir + ' folder is already created')

if not (os.path.isdir(friend_dir)):
    os.mkdir(friend_dir)
    print(friend_dir + ' folder is created')
else:
    print(friend_dir + ' folder is already created')

#Make sure that whatever the order of the name, we will still write in the same file
#if the two people that communicate have the right names
if (os.path.isfile(file)):
    file = file
else:
    file = revfile

print('\n-------------------------------------------')
print('Start of the communication \n')

talking = True

print('If you want to stop, type : STOP')

#We need to create something to share the files
while talking == True:
    f = open(file, "a")
    new_input = input(Alice.name + ' : ')
    if new_input.lower() == 'stop':
        talking = False
        f.close()
        break
    f.write('\n' + Alice.name + ' : ' + new_input)
    f.close()
'''
