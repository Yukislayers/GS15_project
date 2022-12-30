from Test.Keygen import hkdf


class SymmRatchet(object):
    def __init__(self, key):
        self.state = key

    def next(self, inp=b''):
        # turn the ratchet, changing the state and yielding a new key and IV
        output = hkdf(self.state, 80)
        str_output = str(output)
        self.state = str_output[:32]
        outkey, iv = str_output[32:64], str_output[64:]
        return outkey, iv
