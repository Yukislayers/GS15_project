import os
from Alice import *
from Server import *
from Signature import *
from Test.SymmRatchet import SymmRatchet
# This will be the class of the second person to talk


def pad(msg):
    # pkcs7 padding
    num = 16 - (len(msg) % 16)
    return msg + bytes([num] * num)

def unpad(msg):
    # remove pkcs7 padding
    return msg[:-msg[-1]]

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

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
    IDb_priv = 17177758807324845692857368693377283569917000253711757948276657124373021674370888039262011854095683245856550177330748719217582943929659175533515996172744102803519750499798908547990001632992233932395913831775215383821614113936391861772530934230336453164268743083199682697033834366406975361666116961025136007946791011572750667327044635674282751231969871692911622163309943831870069828335208169679334373285775448463956379942945586690304138107899115228213921677252949168055652170164844799655949842947089993618674947738890047631176672561216795692674325069024030733424792011537968208691097234776785939783641278916001509201309
    IDb_pub = pow(g, IDb_priv, p)

    # Generate Alice signed pre key
    # This is the key that should be re-generated every few weeks
    SPKb_priv = 29481355251797690541460288458135166075606261765334726598143710463430881323931459567281033139363812333774769997448920740617170569969987288276831608864663749372638984723049635442004689704086969304602647971316990663400212114318662466595118391458315687056664178500535475352746938016152807452632808294558053793134281590748034748463294036790536299818050928536353221340592249518272724617816717626171634209349779478180271023721765804188249183757152918492676207974712216940848899527533764101664499115391053384222836979422292138402928357094086734700498813458930932765226856267779411696147344411422222083747019540430560453168553
    SPKb_pub = pow(g, SPKb_priv, p)

    hashed_SPKb_pub = hash512(SPKb_pub)

    # For the one-time prekeys, we choose a random number
    OTPKb_priv = 21168411617692412495262355659114213455484933268005729583841322490303255808017152961908500772736051490664908477611675744211135897888703797518257515200958279257135888636693038757429625417268628009296411710756212102428447513784166581475416298186052446279220739015444033555849464587768308444743209626252641433572162281307329233326998007474056313947448000050542640378817206471348251662942821324622083327383083417799138202788228766417892670237318342709484716795206563360836456891993933941748434620406487027517706755243560600074483941990261221585151494912746809346478466770969329660739006349887655520423116400687262857162122
    OTPKb_pub = pow(g, OTPKb_priv, p)

    # For the ephemeral key, we choose a random number
    EKb_priv = 21094546904479834322785065407742363982409865787747711471431407417626669123593718673826946060389581302573884462989955004299599044631756338179465536770937671563274130090274792214367534590934623059000139354604832446544261059571421215001787497839888476565275388125056250025101687416842695568512244037299224334430702375807692786169013021893212992517916833787544641722475674595791752690837349898250629773464456575588539173273222622214660477622904785274540089775849780244946046916679814757772487344910609012305818078477798833671635827952228835497949359752431559782120847773335969391710267581307290507963048722482815111841392
    EKb_pub = pow(g, EKb_priv, p)

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

    DHb_ratchet_priv = 31520537626859489247612700576792915348323752089764165996541678560726231871780642343138326665460612962415575073291631928968576159222847986088984902728798193256299951357852364441641154325095964156580211151143915814378849330277236664506152037699756794135322390778829075170992518216371780283753132919638030205952713458018821685533039963948951717105597717157584558241631842719681521258879027542697959964694098829309351861554144057381353137711116961155179400663782427687085244309861983009731915100846211694611983307546890532388992085158949259113104736134619652204858657771730892004246998329188649448624305427122183979762480
    DHb_ratchet_pub = pow(g, DHb_ratchet_priv, p)

    def bob_init_ratchet(self):
        # initialise the root chain with the shared key
        self.root_ratchet = SymmRatchet(self.shared_key)
        # initialise the sending and recving chains
        self.send_ratchet = SymmRatchet(self.root_ratchet.next()[0])
        self.recv_ratchet = SymmRatchet(self.root_ratchet.next()[0])

    def dh_ratchet(self, alice_public):
        # perform a DH ratchet rotation using Alice's public key
        dh_recv = Keygen.dh(self.p, self.DHb_ratchet_priv, alice_public)
        shared_recv = self.root_ratchet.next(dh_recv)[0]
        # use Alice's public and our old private key
        # to get a new recv ratchet
        self.recv_ratchet = SymmRatchet(shared_recv)
        print('[Bob]\tRecv ratchet seed:', shared_recv)
        # generate a new key pair and send ratchet
        # our new public key will be sent with the next message to Alice
        self.DHratchet = Prime.nBitRandom(2048)
        dh_send = Keygen.dh(self.p, self.DHratchet, alice_public)
        shared_send = self.root_ratchet.next(dh_send)[0]
        self.send_ratchet = SymmRatchet(shared_send)
        print('[Bob]\tSend ratchet seed:', shared_send)

    def send(self, bob, msg):
        key, iv = self.send_ratchet.next()
        iv = bytes(iv.encode('UTF-8'))
        cipher1 = byte_xor(iv, msg)
        print(cipher1)
        key = bytes(key.encode('UTF-8'))
        cipher2 = byte_xor(key, cipher1)
        print(cipher2)

        print('[Alice]\tSending ciphertext to Bob:', cipher2)

        bob.recv(cipher2, self.DHb_ratchet_pub)

    def recv(self, cipher, alice_public_key):

        self.dh_ratchet(alice_public_key)
        key, iv = self.recv_ratchet.next()
        iv = bytes(iv.encode('UTF-8'))
        key = bytes(key.encode('UTF-8'))
        pt2 = byte_xor(cipher, key)
        print(pt2)
        pt1 = byte_xor(iv, pt2)
        print(pt1)
        print('[Alice]\tDecrypted message:', pt1)


def start():
    # We create the server and Bob, so we can put the information on the server for the x3dh exchange
    server = Server()
    bob = Bob()
    alice = Alice()

    print(f'You are {bob.name}')

    # We publish the key bundles on the server
    server.set_alice(alice.IDa_pub, alice.SPKa_pub, alice.SPKa_sig, alice.OTPKa_pub, alice.RSAa_pub, alice.RSAa_modulo,  alice.hashed_SPKa_pub, alice.EKa_pub)
    server.set_bob(bob.IDb_pub, bob.SPKb_pub, bob.SPKb_sig, bob.OTPKb_pub, bob.RSAb_pub, bob.RSAb_modulo, bob.hashed_SPKb_pub, bob.EKb_pub)

    # We need to fetch the bundle and check if the signature of Bob SPK is valid

    if rsa_verify(server.SPKa_sig, server.RSAa_pub, server.RSAa_modulo) == server.Hash_SPKa:
        print('The Signature is valid')
        print('We will start the X3DH key exchange')

        if server.X3DH_bob_init(bob) == server.X3DH_alice_not_init(alice):
            print(f'The shared key is {bob.shared_key}')


        else:
            print('Error')
            exit()
    else:
        print('Error')
        exit()

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

