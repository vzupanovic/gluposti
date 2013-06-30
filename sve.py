import wx
import gui
from math import *
from Crypto.Hash import SHA
from Crypto.Cipher import AES
from Crypto import Random
import KSI
import pickle
import os
import base64
import random
from Crypto.PublicKey import RSA
import binascii

class SHA1_my:
    def generate_hash(self, in_dat, out_dat):
        f = open(in_dat)
        sadrzaj = f.read()
        f.close()
        m = SHA.new()
        m.update(sadrzaj)
        sazetak = m.hexdigest()
        f = open(out_dat, "w")
        f.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('Description','Hash',None,f)
        KSI.put_data_s('Method','SHA-1',None,f)
        KSI.put_data_s('Hash data',sazetak, None, f)
        f.write('---END OS2 CRYPTO DATA---\n')
        f.close()
        print "[AP] sazetak generiran!"
        return sazetak

class AES_my:
    def get_data(self, in_dat, out_dat, key_data):
        f = open(key_data,'r')
        data = KSI.load(f)
        f.close()
        #print data
        key = ''.join(data['Secret key'])
        self.key = key

    def generate_key(self, key_dat, key_size):
        key = ''
        key_len = key_size // 8
        #print key_len
        for i in range(0, key_len):
            num = random.randint(0,15)
            key = key + hex(num)[2:]
        #print len(key)
        f = open(key_dat, 'w')
        f.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('Method','AES',None,f)
        KSI.put_data_s('Key length',hex(key_size),None,f)
        KSI.put_data_s('Secret key',key,None,f)
        f.write('---END OS2 CRYPTO DATA---\n')
        print "[AP] kljuc generiran!"
        f.close()

    def encrypt(self, in_dat, out_dat, key_dat):
        f = open(key_dat, 'r')
        data = KSI.load(f)
        f.close()
        kljuc = data["Secret key"][0]
        print "[AP] tajni kljuc: ",kljuc
        obj = AES.new(kljuc, AES.MODE_CFB,"This is an IV456")
        f = open(in_dat, "r")
        poruka = f.read()
        sifrirana = obj.encrypt(poruka)
        sifr = base64.b64encode(sifrirana)
        #print sifr
        f = open(out_dat, 'w')
        f.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('Description','Crypted file',None,f)
        KSI.put_data_s('Method','AES',None,f)
        KSI.put_data('Data',sifr,f)
        self.enc_data = sifrirana
        self.kljuc = kljuc
        f.write('---END OS2 CRYPTO DATA---\n')
        f.close()
        print "[AP] podaci kriptirani!"

    def decrypt(self):
        obj = AES.new(self.kljuc, AES.MODE_CFB,"This is an IV456")
        poruka = obj.decrypt(self.enc_data)
        print "[AP] dekriprirana poruka:\n", poruka
        return poruka


class RSA_my:
    def compose_keys(self, in_dat1, in_dat2):
        n,d,e = self.get_data(in_dat1,in_dat2)
        key = RSA.construct((n, long(e), d))
        print "[AP] kljuc generiran!"
        return key

    def generate_random_keys(self, privatni_dat, javni_dat, key_len):
        random_num = Random.new().read
        key = RSA.generate(key_len)
        self.key = key
        print "[AP] modulus:", key.n
        f1 = open(privatni_dat,'w')
        f1.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('Description','Private key',None,f1)
        KSI.put_data_s('Method','RSA',None,f1)
        KSI.put_data_s('Key length',hex(key_len),None,f1)
        KSI.put_data_d('Modulus',key.n,-1,f1)
        KSI.put_data_d('Private exponent',key.d,-1,f1)
        f1.write('---END OS2 CRYPTO DATA---\n')
        f1.close()
        f1 = open(javni_dat,'w')
        f1.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('Description','Public key',None,f1)
        KSI.put_data_s('Method','RSA',None,f1)
        KSI.put_data_s('Key length',hex(key_len),None,f1)
        KSI.put_data_d('Modulus',key.n,-1,f1)
        KSI.put_data_d('Public exponent',key.e,-1,f1)
        f1.write('---END OS2 CRYPTO DATA---\n')
        f1.close()
        
        return key
         
    def get_data(self,in_dat_private, in_dat_public):
        f = open(in_dat_private,'r')
        data_private = KSI.load(f)
        f.close()
        modulus = int(''.join(data_private['Modulus']),16)
        private_exponent = int(''.join(data_private['Private exponent']),16)
        #print "modulus:",modulus
        #print "private:", private_exponent
        f = open(in_dat_public)
        data_public = KSI.load(f)
        f.close()
        public_exponent = int(''.join(data_public['Public exponent']),16)
        #print "public", public_exponent
        return modulus, private_exponent, public_exponent

    def encrypt(self, in_dat_private, in_dat_public, in_dat, out_dat):
        key = self.compose_keys(in_dat_private, in_dat_public)
        self.key = key
        public_key = key.publickey()
        f = open(in_dat)
        data = f.read()
        f.close()
        enc_data =  public_key.encrypt(data, 32)
        #print "AAAAAAAA", pickle.dumps(enc_data[0])
        f = open(out_dat,'w')
        f.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('Description','Crypted file',None,f)
        KSI.put_data_s('Method','RSA',None,f)
        KSI.put_data('Data',base64.b64encode(enc_data[0]),f)
        self.enc_data = enc_data
        f.write('---END OS2 CRYPTO DATA---\n')
        f.close()
        print "[AP] kriptiranje zavrsilo!"
        

    def decrypt(self):
        dec_data = self.key.decrypt(self.enc_data)
        print "[AP] dekriptirani podaci: ",dec_data
        return dec_data


class Omotnica:
    def compose_keys(self, in_dat1, in_dat2):
        n,d,e, key_len = self.get_data(in_dat1,in_dat2)
        key = RSA.construct((n, long(e), d))
        #print pickle.dumps(key)
        return key, key_len

    def get_data(self,in_dat_private, in_dat_public):
        f = open(in_dat_private,'r')
        data_private = KSI.load(f)
        f.close()
        modulus = int(''.join(data_private['Modulus']),16)
        private_exponent = int(''.join(data_private['Private exponent']),16)
        #print "modulus:",modulus
        #print "private:", private_exponent
        f = open(in_dat_public)
        data_public = KSI.load(f)
        f.close()
        public_exponent = int(''.join(data_public['Public exponent']),16)
        #print "public", public_exponent
        key_len = data_private['Key length'][0]
        #print "wwww", key_len
        return modulus, private_exponent, public_exponent, key_len

    def stvori_omotnicu(self, in_dat, privatni_dat, javni_dat, out_dat, aes_key_len):
        f = open(in_dat)
        data = f.read()
        f.close()
        kl = aes_key_len // 8
        #print kl
        tajni_kljuc = ''
        for i in range(0, kl):
            tajni_kljuc = tajni_kljuc + '1'
        #tajni_kljuc = '1111111111111111'
        obj = AES.new(tajni_kljuc,AES.MODE_CFB,"This is an IV456")
        sifrirana = obj.encrypt(data)
        sifr = base64.b64encode(sifrirana)
        key, key_len = self.compose_keys(privatni_dat, javni_dat)
        self.key = key
        self.tajni_kljuc = tajni_kljuc
        public_key = key.publickey()
        sifrirani_tajni = public_key.encrypt(tajni_kljuc, 32)
        #print sifrirani_tajni
        sifr_tajni = binascii.hexlify(sifrirani_tajni[0])
        #print sifr_tajni
        f = open(out_dat, 'w')
        f.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('File name',out_dat,None,f)
        KSI.put_data_s('Method','AES\n    RSA',None,f)
        KSI.put_data_s('Key length',key_len+'\n    '+hex(len(tajni_kljuc)*8),None,f)
        KSI.put_data('Envelope data', sifr, f)
        KSI.put_data('Envelope crypt key',sifr_tajni,f)
        f.write('---END OS2 CRYPTO DATA---\n')
        f.close()
        self.poruka = [sifrirana,sifrirani_tajni]
        print "[AP] omotnica generirana!"

    def otvori_omotnicu(self, otvorena_dat):
        kriptirani_tekst = self.poruka[0]
        kriptirani_kljuc = self.poruka[1]
        tajni_kljuc = self.key.decrypt(kriptirani_kljuc)
        #print tajni_kljuc
        obj = AES.new(tajni_kljuc, AES.MODE_CFB,"This is an IV456")
        tekst = obj.decrypt(kriptirani_tekst)
        print "[AP] otvoreni tekst: \n",tekst
        f = open(otvorena_dat, 'w')
        f.write(tekst)
        f.close()
        
class Digitalni_potpis:
    def compose_keys(self, in_dat1, in_dat2):
        n,d,e, key_len = self.get_data(in_dat1,in_dat2)
        key = RSA.construct((n, long(e), d))
        #print pickle.dumps(key)
        return key, key_len

    def get_data(self,in_dat_private, in_dat_public):
        f = open(in_dat_private,'r')
        data_private = KSI.load(f)
        f.close()
        modulus = int(''.join(data_private['Modulus']),16)
        private_exponent = int(''.join(data_private['Private exponent']),16)
        #print "modulus:",modulus
        #print "private:", private_exponent
        f = open(in_dat_public)
        data_public = KSI.load(f)
        f.close()
        public_exponent = int(''.join(data_public['Public exponent']),16)
        #print "public", public_exponent
        key_len = data_private['Key length'][0]
        #print "wwww", key_len
        return modulus, private_exponent, public_exponent, key_len
    
    def generiraj_digitalni_potpis(self, ulaz_dat, privatni_dat, javni_dat, potpis_dat):
        f = open(ulaz_dat)
        data = f.read()
        f.close()
        m = SHA.new()
        m.update(data)
        sazetak = m.hexdigest()
        #print sazetak
        key, key_len = self.compose_keys(privatni_dat, javni_dat)
        potpis = key.sign(sazetak,'')
        potpis_txt = hex(potpis[0])[2:-1]
        #print "ja sam potpis", len(potpis_txt)
        f = open(potpis_dat, 'w')
        f.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('Description','Signature',None,f)
        KSI.put_data_s('File name',potpis_dat,None,f)
        KSI.put_data_s('Method','SHA-1\n    RSA',None,f)
        KSI.put_data_s('Key length','0xa0\n    '+key_len,None,f)
        KSI.put_data('Signature',potpis_txt,f)
        f.write('---END OS2 CRYPTO DATA---\n')
        f.close()
        self.poruka = [data, potpis]
        self.key = key
        print "[AP] potpis generiran!"
        
        

    def provjeri_digitalni_potpis(self,privatni_dat, javni_dat, potpis_dat):
        tekst = self.poruka[0]
        potpis = self.poruka[1]
        #print "ja sam tekst", tekst
        #print "ja sam potpis", potpis
        sazetak = SHA.new(tekst).hexdigest()
        key, key_len = self.compose_keys(privatni_dat, javni_dat)
        public_key = key.publickey()
        if public_key.verify(sazetak, potpis) == True:
            print "[AP] ok"
            return "Datoteka je autenticna!"
        else:
            print "[AP] fail"
            return "Datoteka nije autenticna!"


class Digitalni_pecat:
    def compose_keys(self, in_dat1, in_dat2):
        n,d,e, key_len = self.get_data(in_dat1,in_dat2)
        key = RSA.construct((n, long(e), d))
        #print pickle.dumps(key)
        return key, key_len

    def get_data(self,in_dat_private, in_dat_public):
        f = open(in_dat_private,'r')
        data_private = KSI.load(f)
        f.close()
        modulus = int(''.join(data_private['Modulus']),16)
        private_exponent = int(''.join(data_private['Private exponent']),16)
        #print "modulus:",modulus
        #print "private:", private_exponent
        f = open(in_dat_public)
        data_public = KSI.load(f)
        f.close()
        public_exponent = int(''.join(data_public['Public exponent']),16)
        #print "public", public_exponent
        key_len = data_private['Key length'][0]
        #print "wwww", key_len
        return modulus, private_exponent, public_exponent, key_len
    
    def generiraj_digitalni_pecat(self, ulaz_dat, javni_primatelja, tajni_primatelja, tajni_posiljatelja, javni_posiljatelja, omotnica_dat, potpis_dat):
        f = open(ulaz_dat)
        data = f.read()
        f.close()
        tajni_kljuc = '1111111111111111'
        obj = AES.new(tajni_kljuc,AES.MODE_CFB,"This is an IV456")
        sifrirana = obj.encrypt(data)
        C1 = sifrirana
        sifr = base64.b64encode(sifrirana)
        key_primatelj, key_len_primatelj = self.compose_keys(tajni_primatelja, javni_primatelja) #par kljuceva primatelja
        key_posiljatelj, key_len_posiljatelj = self.compose_keys(tajni_posiljatelja, javni_posiljatelja) #par kljuceva posiljatelja
        self.key_primatelj = key_primatelj
        self.key_posiljatelj = key_posiljatelj
        javni_kljuc_primatelja = key_primatelj.publickey()
        self.tajni_kljuc = tajni_kljuc
        sifrirani_tajni = javni_kljuc_primatelja.encrypt(tajni_kljuc, 32)
        C2 = sifrirani_tajni
        #print sifrirani_tajni
        sifr_tajni = binascii.hexlify(sifrirani_tajni[0])
        #print sifr_tajni
        f = open(omotnica_dat, 'w')
        f.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('File name',omotnica_dat,None,f)
        KSI.put_data_s('Method','AES\n    RSA',None,f)
        KSI.put_data_s('Key length',key_len_primatelj+'\n    '+hex(len(tajni_kljuc)*8),None,f)
        KSI.put_data('Envelope data', sifr, f)
        KSI.put_data('Envelope crypt key',sifr_tajni,f)
        f.write('---END OS2 CRYPTO DATA---\n')
        f.close()
        f = open(omotnica_dat)
        data_omotnica = f.read()
        f.close()
        m = SHA.new()
        m.update(data_omotnica)
        sazetak = m.hexdigest()
        #print "JAAAAAA", sazetak
        kriptirani_sazetak = key_posiljatelj.encrypt(sazetak,32)
        C3 = kriptirani_sazetak
        potpis = key_posiljatelj.sign(sazetak, '')
        potpis_txt = hex(potpis[0])[2:-1]
        f = open(potpis_dat, 'w')
        f.write('---BEGIN OS2 CRYPTO DATA---\n')
        KSI.put_data_s('Description','Signature',None,f)
        KSI.put_data_s('File name',potpis_dat,None,f)
        KSI.put_data_s('Method','SHA-1\n    RSA',None,f)
        KSI.put_data_s('Key length','0xa0\n    '+key_len_posiljatelj,None,f)
        KSI.put_data('Signature',potpis_txt,f)
        f.write('---END OS2 CRYPTO DATA---\n')
        f.close()
        self.poruka = [C1, C2, potpis]
        print "[AP] digitalni pecat generiran!"

    def otvori_digitalni_pecat(self, omotnica_dat, izlaz_dat):
        kriptirani_tekst = self.poruka[0]
        kriptirani_tajni_kljuc = self.poruka[1]
        kriptirani_sazetak = self.poruka[2]
        #print kriptirani_tajni_kljuc
        tajni_kljuc = self.key_primatelj.decrypt(kriptirani_tajni_kljuc)
        #print tajni_kljuc
        obj = AES.new(tajni_kljuc, AES.MODE_CFB,"This is an IV456")
        tekst = obj.decrypt(kriptirani_tekst)
        print "[AP] jasni tekst: \n", tekst
        f = open(omotnica_dat)
        data = f.read()
        f.close()
        sazetak = SHA.new(data).hexdigest()
        f = open(izlaz_dat,'w')
        if self.key_posiljatelj.publickey().verify(sazetak, kriptirani_sazetak) == True:
            f.write(tekst)
            f.close()
            return "Autenticnost datoteke zadovoljena!"
        else:
            f.write("Ne mogu otvoriti pecat!")
            f.close()
            return "Autenticnost nije zadovoljena!"          

    
class CalcFrame(gui.MainFrame):
    #constructor
    def __init__(self,parent):
        self.rsa = RSA_my()
        self.aes = AES_my()
        self.sha1 = SHA1_my()
        self.omotnica = Omotnica()
        self.digitalni_potpis = Digitalni_potpis()
        self.digitalni_pecat = Digitalni_pecat()
        
        
        #initialize parent class
        gui.MainFrame.__init__(self,parent)
 
    #what to when 'Solve' is clicked
    #wx calls this function with and 'event' object
    def func_generiraj_sazetak(self,event):
        try:
            #sha1 = SHA1_my()
            ulaz_dat = str(self.ulaz_dat.GetPath())
            izlaz_dat = str(self.izlaz_dat.GetPath())
            sazetak = self.sha1.generate_hash(ulaz_dat, izlaz_dat)
            #evaluate the string in 'text' and put the answer back
            self.ispis_sazetak.SetLabel(sazetak)
        except Exception:
            print 'error'

    def func_izlaz(self, event):
        try:
            izlaz_dat = str(self.izlaz_dat.GetPath())
            command = "notepad.exe "+izlaz_dat
            os.system(command)
        except Exception:
            print 'error'

    def func_ulaz(self, event):
        try:
            izlaz_dat = str(self.ulaz_dat.GetPath())
            command = "notepad.exe "+izlaz_dat
            os.system(command)
        except Exception:
            print 'error'

    def func_gen_kljuc_aes(self, event):
        try:
            #self.aes = AES_my()
            key_dat = str(self.kljuc_dat_aes.GetPath())
            #print key_dat
            velicina = self.izbor_aes.GetLabel()
            #print "AAAAAAA",velicina
            self.aes.generate_key(key_dat, int(velicina))
        except Exception:
            print 'error'

    def func_prikazi_aes_kljuc(self, event):
        try:
            kljuc_dat = str(self.kljuc_dat_aes.GetPath())
            command = "notepad.exe "+kljuc_dat
            os.system(command)
        except Exception:
            print 'error'

    def aes_ulaz_dat(self, event):
        try:
            ulaz_dat = str(self.ulaz_dat_aes.GetPath())
            command = "notepad.exe "+ulaz_dat
            os.system(command)
        except Exception:
            print 'error'

    def aes_dat_izlaz(self, event):
        try:
            izlaz_dat = str(self.izlaz_dat_aes.GetPath())
            command = "notepad.exe "+izlaz_dat
            os.system(command)
        except Exception:
            print 'error'

    def func_aes_kriptiraj(self, event):
        try:
            key_dat = str(self.kljuc_dat_aes.GetPath())
            ulaz_dat = str(self.ulaz_dat_aes.GetPath())
            izlaz_dat = str(self.izlaz_dat_aes.GetPath())
            self.aes.encrypt(ulaz_dat, izlaz_dat, key_dat)
        except Exception:
            print 'error'

    def func_aes_dekriptiraj(self, event):
        try:
            self.aes_dec_poruka = self.aes.decrypt()
            f = open("dekriptirano.txt",'w')
            f.write(self.aes_dec_poruka)
            f.close()
        except Exception:
            print 'error'

    def func_prikazi_aes_dec(self, event):
        try:
            command = "notepad.exe dekriptirano.txt"
            os.system(command)
        except Exception:
            print 'error'

    def prikazi_rsa_privatni(self, event):
        try:
            privatni_dat = str(self.privatni_dat_rsa.GetPath())
            command = "notepad.exe "+privatni_dat
            os.system(command)
        except Exception:
            print 'error'


    def prikazi_rsa_javni(self, event):
        try:
            javni_dat = str(self.javni_dat_rsa.GetPath())
            command = "notepad.exe "+javni_dat
            os.system(command)
        except Exception:
            print 'error'


    def prikazi_ulaz_rsa(self, event):
        try:
            ulaz_dat = str(self.ulaz_dat_rsa.GetPath())
            command = "notepad.exe "+ulaz_dat
            os.system(command)
        except Exception:
            print 'error'
        
    def prikazi_izlaz_rsa(self, event):
        try:
            izlaz_dat = str(self.izlaz_dat_rsa.GetPath())
            command = "notepad.exe "+izlaz_dat
            os.system(command)
        except Exception:
            print 'error'


    def func_generiraj_kljuceve(self, event):
        try:
            velicina_kljuca = self.rsa_kljuc_duljina.GetLabel()
            privatni_dat = str(self.privatni_dat_rsa.GetPath())
            javni_dat = str(self.javni_dat_rsa.GetPath())
            #self.rsa = RSA_my()
            self.rsa.generate_random_keys(privatni_dat, javni_dat, int(velicina_kljuca))
        except Exception:
            print 'error'


    def func_rsa_kriptiraj(self, event):
        try:
            #print "tussssssaaaaaaaaaaaaaaaaaaam"
            javni_dat = str(self.javni_dat_rsa.GetPath())
            privatni_dat = str(self.privatni_dat_rsa.GetPath())
            ulaz_dat = str(self.ulaz_dat_rsa.GetPath())
            izlaz_dat = str(self.izlaz_dat_rsa.GetPath())
            self.rsa.encrypt(privatni_dat, javni_dat, ulaz_dat, izlaz_dat)
        except Exception:
            print 'error'

    def func_rsa_dekriptiraj(self, event):
        try:
            izlaz_dat = str(self.izlaz_dat_rsa.GetPath())
            poruka = self.rsa.decrypt()
            f = open(izlaz_dat,'w')
            f.write(poruka)
            f.close()
        except Exception:
            print 'error'

    def prikazi_om_javni(self, event):
        try:
            javni_om = str(self.om_javni_kljuc.GetPath())
            command = "notepad.exe "+javni_om
            os.system(command)
        except Exception:
            print 'error'

    
    def prikazi_om_tajni(self, event):
        try:
            tajni_om = str(self.om_tajni_kljuc.GetPath())
            command = "notepad.exe "+tajni_om
            os.system(command)
        except Exception:
            print 'error'

    def prikazi_om_ulaz(self, event):
        try:
            ulaz_dat = str(self.om_ulaz_dat.GetPath())
            command = "notepad.exe "+ulaz_dat
            os.system(command)
        except Exception:
            print 'error'

    def prikazi_om_izlaz(self, event):
        try:
            izlaz_dat = str(self.om_izlaz_dat.GetPath())
            command = "notepad.exe "+izlaz_dat
            os.system(command)
        except Exception:
            print 'error'


    def prikazi_om(self, event):
        try:
            om_dat = str(self.omotnica_dat.GetPath())
            command = "notepad.exe "+om_dat
            os.system(command)
        except Exception:
            print 'error'

    def func_generiraj_omotnicu(self, event):
        try:
            ulaz_dat = str(self.om_ulaz_dat.GetPath())
            izlaz_dat = str(self.om_izlaz_dat.GetPath())
            javni_dat = str(self.om_javni_kljuc.GetPath())
            tajni_dat = str(self.om_tajni_kljuc.GetPath())
            om_dat = str(self.omotnica_dat.GetPath())
            #self.omotnica = Omotnica()
            self.omotnica.stvori_omotnicu(ulaz_dat, tajni_dat, javni_dat, om_dat, 128)
        except Exception:
            print 'error'


    def func_otvori_omotnicu(self, event):
        try:
            izlaz_dat = str(self.om_izlaz_dat.GetPath())
            self.omotnica.otvori_omotnicu(izlaz_dat)
        except Exception:
            print 'error'

    def prikazi_pt_tajni(self, event):
        try:
            pt_tajni = str(self.pt_tajni_dat.GetPath())
            command = "notepad.exe "+pt_tajni
            os.system(command)
        except Exception:
            print 'error'

    def prikazi_pt_javni(self, event):
        try:
            pt_javni = str(self.pt_javni_dat.GetPath())
            command = "notepad.exe "+pt_javni
            os.system(command)
        except Exception:
            print 'error'
            
    def prikazi_pt_ulaz(self, event):
        try:
            ulaz_dat = str(self.pt_ulaz_dat.GetPath())
            command = "notepad.exe "+ulaz_dat
            os.system(command)
        except Exception:
            print 'error'        

    def prikazi_pt(self, event):
        try:
            izlaz_dat = str(self.pt_izlaz_dat.GetPath())
            command = "notepad.exe "+izlaz_dat
            os.system(command)
        except Exception:
            print 'error'

    def func_generiraj_potpis(self, event):
        try:
            pt_tajni = str(self.pt_tajni_dat.GetPath())
            pt_javni = str(self.pt_javni_dat.GetPath())
            ulaz_dat = str(self.pt_ulaz_dat.GetPath())
            potpis_dat = str(self.pt_izlaz_dat.GetPath())
            #self.digitalni_potpis = Digitalni_potpis()
            self.digitalni_potpis.generiraj_digitalni_potpis(ulaz_dat, pt_tajni, pt_javni, potpis_dat)
        except Exception:
            print 'error'

    def func_provjeri_potpis(self, event):
        try:
            pt_tajni = str(self.pt_tajni_dat.GetPath())
            pt_javni = str(self.pt_javni_dat.GetPath())
            potpis_dat = str(self.pt_izlaz_dat.GetPath())          
            dat_ok = self.digitalni_potpis.provjeri_digitalni_potpis(pt_tajni, pt_javni, potpis_dat)
            self.rez_provjera.SetLabel(dat_ok)
        except Exception:
            print 'error'

    def prikazi_pc_ulaz(self, event):
        try:
            ulaz_dat = str(self.pc_ulaz_dat.GetPath())
            command = "notepad.exe "+ulaz_dat
            os.system(command)
        except Exception:
            print 'error'
            

    def prikazi_pc_javni_primatelja(self, event): #--
        try:
            javni_primatelja = str(self.pc_javni_primatelja_dat.GetPath())
            command = "notepad.exe "+javni_primatelja
            os.system(command)
        except Exception:
            print 'error'


    def prikazi_pc_tajni_posiljatelja(self, event): #oo
        try:
            tajni_posiljatelja = str(self.pc_tajni_posiljatelja_dat.GetPath())
            command = "notepad.exe "+tajni_posiljatelja
            os.system(command)
        except Exception:
            print 'error'

    def prikazi_pc_omotnica(self, event):
        try:
            omotnica_dat = str(self.pc_omotnica_dat.GetPath())
            command = "notepad.exe "+omotnica_dat
            os.system(command)
        except Exception:
            print 'error'


    def prikazi_pc_potpis(self, event):
        try:
            potpis_dat = str(self.pc_potpis_dat.GetPath())
            command = "notepad.exe "+potpis_dat
            os.system(command)
        except Exception:
            print 'error'      


    def prikazi_pc_javni_posiljatelja(self, event): #oo
        try:
            javni_posiljatelja = str(self.pc_javni_posiljatelja.GetPath())
            command = "notepad.exe "+javni_posiljatelja
            os.system(command)
        except Exception:
            print 'error'


    def prikazi_pc_tajni_primatelja(self, event):#--
        try:
            tajni_primatelja = str(self.pc_tajni_primatelja.GetPath())
            command = "notepad.exe "+tajni_primatelja
            os.system(command)
        except Exception:
            print 'error'


    def prikazi_pc_izlaz_dat(self, event):
        try:
            izlaz_dat = str(self.pc_izlaz_dat.GetPath())
            command = "notepad.exe "+izlaz_dat
            os.system(command)
        except Exception:
            print 'error'

    def func_generiraj_pecat(self, event):
        try:
            ulaz_dat = str(self.pc_ulaz_dat.GetPath())
            javni_primatelja = str(self.pc_javni_primatelja_dat.GetPath())
            omotnica_dat = str(self.pc_omotnica_dat.GetPath())
            tajni_primatelja = str(self.pc_tajni_primatelja.GetPath())
            potpis_dat = str(self.pc_potpis_dat.GetPath())
            javni_posiljatelja = str(self.pc_javni_posiljatelja.GetPath())
            tajni_posiljatelja = str(self.pc_tajni_posiljatelja_dat.GetPath())
            izlaz_dat = str(self.pc_izlaz_dat.GetPath())
            #self.digitalni_pecat = Digitalni_pecat()
            self.digitalni_pecat.generiraj_digitalni_pecat(ulaz_dat, javni_primatelja, tajni_primatelja, tajni_posiljatelja, javni_posiljatelja, omotnica_dat, potpis_dat)
            

        except Exception:
            print 'error'


    def func_otvori_pecat(self, event):
        try:
            izlaz_dat = str(self.pc_izlaz_dat.GetPath())
            omotnica_dat = str(self.pc_omotnica_dat.GetPath())
            rez = self.digitalni_pecat.otvori_digitalni_pecat(omotnica_dat, izlaz_dat)
            self.rez_otvaranja.SetLabel(rez)
        except Exception:
            print 'error'
            
            
            
            

 
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = CalcFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
