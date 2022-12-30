import os
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
    IDa_priv = 31869297399262301645804724780494485853083453101086351121144159019892931866018394329611078515887304771461389919893961295138923688275628259274514649943947313176187799304661899549772260644651455751571892873377013566249875353470864616832839704070301316886719462236923849939276520795626519490521886811597325358569362709294373113636015347197142679027375533396696131375231696051322471601967990071280031751577902490570966601746867809067463471099079757847396472019294668445325494132962562366850529729529859052374978552685955612335374909160576229160098448321711822119570309999558360102506065448387575221394178761161854196208986
    IDa_pub = pow(g, IDa_priv, p)

    # Generate Alice signed pre key
    # This is the key that should be re-generated every few weeks
    SPKa_priv = 25510878141529576863521498715288875868726641884637455246406122529734194485949018115790745939288220378645237872789375295386950458721205855178835470418777044678137088184349583160106294205204562540286278082667078870991089018873855069535390289569294422841020937795097302221235455032902563629894071850834550413848511104851780422741845950467767495155914855950951814835718044143250672008900244106531976399355539597834514731939716518528362045773249759719663386311007202199090309334003683980144927076744972703815311249339561860713963783549763688382953906408042681720333841215833444459953563100731946790258065940555443950426257
    SPKa_pub = pow(g, SPKa_priv, p)

    hashed_SPKa_pub = hash512(SPKa_pub)

    # For the one-time prekeys, we choose a random number
    OTPKa_priv = 29538058859371078741337886344725332433320110892214302837653580136386851786074000289644484081256453813378801664790764515619642336336628821063415611471137807620104973096649442629502892077247645266994709088453258258868539140886723512814295756191093363690417835330667259510193189862766547541524426443647191912944013321993678940256815382157772295632984589759363253576309717307046486443001574765782334704989500672588005113615795505018677204305689993756717908708606089226895092939692533550566767190069866028777868166954492865721644273308466204473683841667914000819726841018713262982313300971838177933053380098523663894237180
    OTPKa_pub = pow(g, OTPKa_priv, p)

    # For the ephemeral key, we choose a random number
    EKA_priv = 28900725540770713142369068201221291575827950068098793715801588832442229780783957860297001440106704069148752366935188364725998270360195076444504667959749710354948258912256843139622266752775698906161645442682186041714506685800142183831416153089561663111092056598652182062690525722096573484204285869765355445765426045681665130734870662615724047036327353030770566725098923583622754057610052572010842968566841166354080381180287982200035998141873289259607456623680284227888532819375105046503387768809676507064469617740725856392265538696538532849377222525496345378107013351811398538718002402509277826283522112585468556200735
    EKa_pub = pow(g, EKA_priv, p)

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


def start():
    # We create the server and Bob, so we can put the information on the server for the x3dh exchange
    server = Server()
    alice = Alice()
    bob = Bob()

    print(f'You are {alice.name}')
    # We publish the key bundles on the server
    server.set_alice(alice.IDa_pub, alice.SPKa_pub, alice.SPKa_sig, alice.OTPKa_pub, alice.RSAa_pub, alice.RSAa_modulo,  alice.hashed_SPKa_pub, alice.EKa_pub)
    server.set_bob(bob.IDb_pub, bob.SPKb_pub, bob.SPKb_sig, bob.OTPKb_pub, bob.RSAb_pub, bob.RSAb_modulo, bob.hashed_SPKb_pub, bob.EKb_pub)

    # We need to fetch the bundle and check if the signature of Bob SPK is valid

    if rsa_verify(server.SPKb_sig, server.RSAb_pub, server.RSAb_modulo) == server.Hash_SPKb:
        print('The Signature is valid')
        print('We will start the X3DH key exchange')

        if server.X3DH_alice_init(alice) == server.X3DH_bob_not_init(bob):
            print(f'The shared key is {alice.shared_key}')
    else:
        print('Error')
        exit()


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

