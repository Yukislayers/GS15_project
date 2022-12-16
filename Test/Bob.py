import os
from Server import *
from Signature import *

# This will be the class of the second person to talk


class Bob:
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

    name = 'Bob'

    # Generate Alice IDa key pair
    IDb_priv = 10
    IDb_pub = pow(g, IDb_priv, p)

    # Generate Alice signed pre key
    # This is the key that should be re-generated every few weeks
    SPKb_priv = 20
    SPKb_pub = pow(g, SPKb_priv, p)

    hashed_SPKb_pub = hash512(SPKb_pub)

    # For the one-time prekeys, we choose a random number
    OTPKb_priv = 30
    OTPKb_pub = pow(g, OTPKb_priv, p)

    # For the ephemeral key, we choose a random number
    b = random.randrange(1, p)
    EKb = pow(g, b, p)

    # RSA key pair
    # Generated with Signature.py file
    RSAb_priv = 68945648884904663675267175521577444671902605999545536917279248176439396502805884221274794942250444299948482975374038383270805105662978931021514764928325229883767032602852287231302114445905095126494799062310521087393456951326603244793905517822341606438671712590300023108532563308719437607273680193498919565619
    RSAb_pub = 3146185933466387797585391166964192914607318026918893364146639291582861206230682255437216261693800924044619106554712988485684979347192730098733459790305572379662270806066317486382188875920835230240779434647852255577382729790100053459668994906125353157273376776711205492311892905694832360671825326000906497859
    RSAb_modulo = 107062777979160845210480721813063478070407333770184406013025472343065269367423043925027554327858725377844257240552880578785530291231936563356958696911181858068479947703182057751582566421831537837815114076015346519661198501653486368255325991177573962976986233599323527727371891920500124410718022461517308776263

    # We create the prekey signature by signing the signed pre key with Bob private key
    # We will use the rsa signature
    SPKb_sig = rsa_signature(hashed_SPKb_pub, RSAb_priv, RSAb_modulo)

    # The shared key will be updated later
    shared_key = 0


'''
# Communication method for the moment
print('You are : ' + Bob.name)

friend = input("Please enter the name of the person you want to talk to : ")

print('You are going to talk to : ' + friend)

file = Bob.name + '_' + friend + '.txt'
revfile = friend + '_' + Bob.name + '.txt'

#Verify if a text file between the two already exists
if not (os.path.isfile(file)) and not (os.path.isfile(revfile)):
    f = open(file, "w")
    print('File between ' + Bob.name + ' and ' + friend + ' is created !')
    f.write("start of the conversation between " + Bob.name + " and " + friend)
    f.close()
else:
    print('File between ' + Bob.name + ' and ' + friend + ' already exists !')

mydir = Bob.name + '_dir'
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

while talking == True:
    f = open(file, "a")
    new_input = input(Bob.name + ' : ')
    if new_input.lower() == 'stop':
        talking = False
        f.close()
        break
    f.write('\n' + Bob.name + ' : ' + new_input)
    f.close()
'''
