

class Server:
    # Pour alice
    IDa = 0
    SPKa = 0 # It will consist of the hashed value of Alice SPKa_pub
    SPKa_sig = 0
    OTPKa = 0
    RSAa_pub = 0
    RSAa_modulo = 0


    # Pour Bob
    IDb = 0
    SPKb = 0 # It will consist of the hashed value of Bob SPKb_pub
    SPKb_sig = 0
    OTPKb = 0
    RSAb_pub = 0
    RSAb_modulo = 0

    def set_bob(self, value1, value2, value3, value4, value5, value6):
        self.IDb = value1
        self.SPKb = value2
        self.SPKb_sig = value3
        self.OTPKb = value4
        self.RSAb_pub = value5
        self.RSAb_modulo = value6

    def set_alice(self, value1, value2, value3, value4, value5, value6):
        self.IDa = value1
        self.SPKa = value2
        self.SPKa_sig = value3
        self.OTPKa = value4
        self.RSAa_pub = value5
        self.RSAa_modulo = value6
