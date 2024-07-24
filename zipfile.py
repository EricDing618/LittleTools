import numpy as np
import string,itertools
import os
import zipfile,py7zr,rarfile,tarfile

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


class BaseUnCompress: #改自博客 https://blog.csdn.net/weixin_43796109/article/details/125431009
    def __init__(self, file_path, output_path, password=None):
        self.file_path = file_path                  # 输入文件路径
        self.output_path = output_path              # 输出文件路径
        self.password = password                    # 压缩密码

    # zip解压缩
    def unzip_file(self):
        try:
            with zipfile.ZipFile(file=self.file_path, mode='r') as fp:
                fp.extractall(self.output_path, pwd=self.password.encode('ascii'))
            return True
        except:
            return False

    # 7z解压缩
    def un7z_file(self):
        try:
            with py7zr.SevenZipFile(self.file_path, 'r', password=self.password) as fp:
                fp.extractall(path=self.output_path)
            return True
        except:
            return False

    # RAR解压缩
    def unrar_file(self):
        try:
            with rarfile.RarFile(self.file_path, 'r') as fp:
                fp.extractall(self.output_path, pwd=self.password)
            return True
        except:
            return False

    #TAR解压缩
    def untar_file(self):
        try:
            with tarfile.TarFile(self.file_path,'r') as fp:
                fp.extractall(self.output_path)
            return True
        except:
            return False

    def run(self):
        file_state = False
        if not os.path.exists(self.file_path):
            return file_state
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        # zip解压缩
        if zipfile.is_zipfile(self.file_path):
            file_state = self.unzip_file()

        # 7z解压缩
        if py7zr.is_7zfile(self.file_path):
            file_state = self.un7z_file()

        # RAR解压缩
        if rarfile.is_rarfile(self.file_path):
            file_state = self.unrar_file()

        if tarfile.is_tarfile(self.file_path):
            file_state=self.untar_file()

        return file_state

if __name__=='__main__':
    a=pwdArray(4)
    print(a.getlen())