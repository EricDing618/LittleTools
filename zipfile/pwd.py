import numpy as np
import string,itertools

class pwdArray:
    def __init__(self, max_len=4):
        self.max_len = max_len
        self.chars = string.digits+string.ascii_letters
        self.charlen=len(self.chars)
        self.pwd = []
        for i in range(self.max_len):
            self.pwd+=itertools.product(self.chars,repeat=i+1)

    def getpwd(self):
        return tuple(self.pwd)
    
    def getlen(self)->int:
        '''非占内存预估长度'''
        a=0 
        for i in range(self.max_len):
            a+=self.charlen**(i+1)
        return a

if __name__=='__main__':
    a=pwdArray(4)
    print(a.getlen())