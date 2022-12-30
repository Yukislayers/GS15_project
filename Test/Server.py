import Keygen

class Server:
    # Pour alice
    IDa = 0
    SPKa = 0
    SPKa_sig = 0
    OTPKa = 0
    RSAa_pub = 0
    RSAa_modulo = 0
    Hash_SPKa = 0
    EKa = 0

    # Pour Bob
    IDb = 0
    SPKb = 0
    SPKb_sig = 0
    OTPKb = 0
    RSAb_pub = 0
    RSAb_modulo = 0
    Hash_SPKb = 0
    EKb = 0

    def set_bob(self, value1, value2, value3, value4, value5, value6, value7, value8):
        self.IDb = value1
        self.SPKb = value2
        self.SPKb_sig = value3
        self.OTPKb = value4
        self.RSAb_pub = value5
        self.RSAb_modulo = value6
        self.Hash_SPKb = value7
        self.EKb = value8

    def set_alice(self, value1, value2, value3, value4, value5, value6, value7, value8):
        self.IDa = value1
        self.SPKa = value2
        self.SPKa_sig = value3
        self.OTPKa = value4
        self.RSAa_pub = value5
        self.RSAa_modulo = value6
        self.Hash_SPKa = value7
        self.EKa = value8

    def X3DH_alice_init(self, alice):
        dh1 = Keygen.dh(alice.p, alice.IDa_priv, self.SPKb)
        dh2 = Keygen.dh(alice.p, alice.EKA_priv, self.IDb)
        dh3 = Keygen.dh(alice.p, alice.EKA_priv, self.SPKb)
        dh4 = Keygen.dh(alice.p, alice.EKA_priv, self.OTPKb)

        alice.shared_key = Keygen.hkdf(dh1 + dh2 + dh3 + dh4, 32)

    def X3DH_bob_init(self, bob):
        dh1 = Keygen.dh(bob.p, bob.IDb_priv, self.SPKa)
        dh2 = Keygen.dh(bob.p, bob.EKb_priv, self.IDa)
        dh3 = Keygen.dh(bob.p, bob.EKb_priv, self.SPKa)
        dh4 = Keygen.dh(bob.p, bob.EKb_priv, self.OTPKa)

        bob.shared_key = Keygen.hkdf(dh1 + dh2 + dh3 + dh4, 32)

    def X3DH_bob_not_init(self, bob):
        dh1 = Keygen.dh(bob.p, bob.SPKb_priv, self.IDa)
        dh2 = Keygen.dh(bob.p, bob.IDb_priv, self.EKa)
        dh3 = Keygen.dh(bob.p, bob.SPKb_priv, self.EKa)
        dh4 = Keygen.dh(bob.p, bob.OTPKb_priv, self.EKa)

        bob.shared_key = Keygen.hkdf(dh1 + dh2 + dh3 + dh4, 32)

    def X3DH_alice_not_init(self, alice):
        dh1 = Keygen.dh(alice.p, alice.SPKa_priv, self.IDb)
        dh2 = Keygen.dh(alice.p, alice.IDa_priv, self.EKb)
        dh3 = Keygen.dh(alice.p, alice.SPKa_priv, self.EKb)
        dh4 = Keygen.dh(alice.p, alice.OTPKa_priv, self.EKb)

        alice.shared_key = Keygen.hkdf(dh1 + dh2 + dh3 + dh4, 32)
