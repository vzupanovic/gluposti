import random
class AES:
    sbox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab,0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

    inv_sbox = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb
    ,0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb
    ,0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e
    ,0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25
    ,0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92
    ,0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84
    ,0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06
    ,0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b
    ,0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73
    ,0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e
    ,0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b
    ,0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4
    ,0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f
    ,0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef
    ,0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61
    ,0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]

    Rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8,
    0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
    0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f,
    0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d,
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab,
    0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d,
    0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25,
    0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01,
    0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d,
    0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa,
    0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a,
    0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02,
    0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
    0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef,
    0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94,
    0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
    0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f,
    0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5,
    0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33,
    0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb ]

    keySize = { "AES_128":16, "AES_192":24, "AES_256":32 }

    def getSbox(self, num):
        return self.sbox[num]

    def getInvSbox(self, num):
        return self.inv_sbox[num]

    def getRcon(self, num):
        return self.Rcon[num]

    def rotate(self, word, step): #1d2c3a4f = 2c3a4f1d
        b = word[0]
        for i in range(0, 3):
            word[i*step] = word[(i+1)*step]
        word[3*step] = b
        return word

    def expCore(self, word, iteration): #zamjeni bajtove s onim iz sbox
        word = self.rotate(word, 1)
        for i in range(0, 4):
            word[i] = self.getSbox(word[i])
        word[0] = word[0]^self.getRcon(iteration)
        return word

    def getKeySize(self, size):
        if (self.keySize["AES_128"] == size):
            exp_size = (10 + 1) * 16
        elif (self.keySize["AES_192"] == size):
            exp_size = (12 + 1) * 16
        elif (self.keySize["AES_256"] == size):
            exp_size = (14 + 1) * 16
        return exp_size

    def expKey(self, original_key, size):
        current_size = 0
        current_Rcon = 1 # trenutna rcon iteracija
        exp_size = self.getKeySize(size)
        t = [0]*4
        expandedKey = [0] * exp_size
        for i in range(0,size): #prepisi kljuc stari koliko imas
            expandedKey[i] = original_key[i]
        current_size = current_size + size
        #print current_size, expandedKey
        while (current_size < exp_size):
            for i in range(0,4):
                t[i] = expandedKey[(current_size - 4) + i] #u t zadnju rijec
            if (current_size % size == 0):
                t = self.expCore(t, current_Rcon)
                current_Rcon = current_Rcon + 1 #svakih 16, 24, 32
            #samo za 256!
            if (size == self.keySize["AES_256"] and ((current_size % size) == 16)):
                for i in range(0,4):
                    t[i] = self.getSbox(t[i])
            
            #xor na t i rijec
            for i in range(0, 4):
                expandedKey[current_size] = expandedKey[current_size - size]^t[i]
                current_size = current_size + 1
        return expandedKey

    def createRoundKey(self, exp_key, key_pointer):
        round_key = [0] * 16
        for i in range(0,4):
            for j in range(0,4):
                round_key[i + j*4] = exp_key[key_pointer + i*4 + j] #po stupcima puni pazi
        return round_key

    def xorRoundKey(self, state, subkey):
        for i in range(0,16):
            state[i] = state[i]^subkey[i]
        return state

    def switchBytes(self, state):
        for i in range(0,16):
            state[i] = self.getSbox(state[i])
        return state

    def switchBytesInv(self, state):
        for i in range(0,16):
            state[i] = self.getInvSbox(state[i])
        return state

    def xTimes(self, a, b):
        broj = b
        rez = 0
        #mult_list = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
        not_empty = []
        for i in range(0,8):
            p = broj & 1
            broj = broj >> 1
            if (a > 0xff):
                a = a^0x11b
            #print hex(a), p
            if (p==1):
                not_empty.append(a)
            a = a << 1
        #print not_empty
        rez = 0
        for num in not_empty:
            rez = rez^num
        return rez

    def shiftRow(self, state, state_pointer, num):
        for i in range(0,num):
            temp = state[state_pointer]
            for j in range(0,3):
                state[state_pointer + j] = state[state_pointer + j + 1]
            state[state_pointer + 3] = temp
        return state

    def shiftRowInv(self, state, state_pointer, num):
        for i in range(0,num):
            temp = state[state_pointer + 3]
            for j in range(3,0,-1):
                state[state_pointer + j] = state[state_pointer + j -1]
            state[state_pointer] = temp
        return state

    def shiftRows(self, state):
        for i in range(0,4):
            state = self.shiftRow(state, i*4, i)
        return state

    def shiftRowsInv(self, state):
        for i in range(0,4):
            state = self.shiftRowInv(state, i*4, i)
        return state

    def mixColumns(self, state, inv):
        column = [0]*4
        for i in range(0,4):
            for j in range(0,4):
                column[j] = state[i + j*4] #izvuci van stupac
            column = self.mulColumn(column, inv)
            for k in range(0,4):
                state[i + 4*k] = column[k] #vraca nazad izmnozeni stupac s onom m. u stanj.
        return state

    def mulColumn(self, column, inv):
        matrix = [2, 3, 1, 1,
                  1, 2, 3, 1,
                  1, 1, 2, 3,
                  3, 1, 1, 2]
        copy = [0]*4
        if inv:
            mul = [14,9,13,11]
        else:
            mul = [2,1,1,3]
        copy = column[:]
        column[0]=self.xTimes(copy[0],mul[0])^self.xTimes(copy[3],mul[1])^self.xTimes(copy[2],mul[2])^self.xTimes(copy[1],mul[3])
        column[1]=self.xTimes(copy[1],mul[0])^self.xTimes(copy[0],mul[1])^self.xTimes(copy[3],mul[2])^self.xTimes(copy[2],mul[3])
        column[2]=self.xTimes(copy[2],mul[0])^self.xTimes(copy[1],mul[1])^self.xTimes(copy[0],mul[2])^self.xTimes(copy[3],mul[3])
        column[3]=self.xTimes(copy[3],mul[0])^self.xTimes(copy[2],mul[1])^self.xTimes(copy[1],mul[2])^self.xTimes(copy[0],mul[3])
        return column

    def getRoundNumber(self, size):
        if self.keySize["AES_128"] == size:
            return 10
        elif self.keySize["AES_192"] == size:
            return 12
        else:
            return 14

    def AesRound(self, state, round_key):
        state = self.switchBytes(state)
        state = self.shiftRows(state)
        state = self.mixColumns(state, 0)
        state = self.xorRoundKey(state, round_key)
        return state

    def AesRoundInv(self, state, round_key):
        state = self.shiftRowsInv(state)
        state = self.switchBytesInv(state)
        state = self.xorRoundKey(state, round_key)
        state = self.mixColumns(state, 1)
        return state

    def aesMain(self, state, expanded_key, n_rounds):
        state = self.xorRoundKey(state, self.createRoundKey(expanded_key, 0)) #ona glupost dodaj potkljuc init runda
        for i in range(1, n_rounds):
            state = self.AesRound(state, self.createRoundKey(expanded_key,16*i))
        state = self.switchBytes(state)
        state = self.shiftRows(state)
        state = self.xorRoundKey(state, self.createRoundKey(expanded_key, 16*n_rounds))
        return state

    def aesInvMain(self, state, expanded_key, n_rounds):
        state = self.xorRoundKey(state, self.createRoundKey(expanded_key, 16*n_rounds))
        for i in range(n_rounds-1, 0, -1):
            state = self.AesRoundInv(state, self.createRoundKey(expanded_key, 16*i))
        state = self.shiftRowsInv(state)
        state = self.switchBytesInv(state)
        state = self.xorRoundKey(state,self.createRoundKey(expanded_key,0))
        return state
                                
                                 

    def AesEncript(self, ulaz, size, key):
        output = [0]*16
        num_rounds = self.getRoundNumber(size)
        exp_key_size = self.getKeySize(size)
        block = [0]*16
        for i in range(0,4):
            for j in range(0,4):
                block[i + j*4] = ulaz[i*4 + j]
        expanded_key = self.expKey(key, size)
        block = self.aesMain(block, expanded_key, num_rounds)
        for i in range(0,4):
            for j in range(0,4):
                output[i*4 + j] = block[i + j*4]
        return output

    def AesDecrypt(self, ulaz, size, key):
        output = [0] * 16
        num_rounds = self.getRoundNumber(size)
        exp_key_size = self.getKeySize(size)
        block = [0]*16
        for i in range(0,4):
            for j in range(0,4):
                block[i+j*4] = ulaz[i*4+j]
        expanded_key = self.expKey(key,size)
        block = self.aesInvMain(block, expanded_key, num_rounds)
        for i in range(0,4):
            for j in range(0,4):
                output[i*4+j] = block[i+4*j]
        return output

    def printOut(self, output):
        out = ''
        for i in range(0,len(output)):
            out=out + hex(output[i])
        print out
            

    def FormatOutput(self, output, in_string):
        print in_string
        out = ''
        for i in range(0, len(output)):
            mini = hex(output[i])
            out = out + mini[mini.find('x')+1:]
        print out
        return out
        
class Operation:
    def ConvertToHex(self, string):
        block = list(string)
        dec_block = []
        hex_block = []
        for char in block:
            dec_block.append(hex(ord(char)))
        for char in dec_block:
            hex_block.append(int(char,16))
        return hex_block

    def ReturnToChar(self, blocks, usable):
        message = ''
        print "Poslana poruka: "
        blocks[-1]=blocks[-1][0:usable]
        for block in blocks:
            for num in block:
                message = message + chr(num)

        print message
                

    def GetBlocks(self, text_list):
        blocks = []
        last_block = []
        n_blocks = len(text_list) // 16
        #print n_blocks
        for i in range(0,n_blocks):
            block = text_list[16*i:(16*i+16)]
            blocks.append(block)
        last_block_length = len(text_list) % 16
        if (last_block_length > 0):
            padd_with = 16 - last_block_length
            pointer = last_block_length
            last_block = text_list[16*n_blocks:16*n_blocks+pointer] + [padd_with]*(16 - last_block_length)
            blocks.append(last_block)
            #print last_block
        else:
            padd_with = 16
            last_block = [128]*16
            blocks.append(last_block)
            #print last_block
        pointer = last_block_length
        #print "pointer",pointer
        #print "s ovim dopuni", hex(padd_with)
        #print last_block_length
        #print blocks
        #print "OVO SU BLOKOVI", blocks
        return blocks, last_block_length

    def ECBencrypt(self, blocks, key, key_size):
        full_text = ''
        aes = AES()
        encrypt_blocks = []
        print "Prikaz kriptiranja po blokovima:\n"
        for block in blocks:
            state = block
            out = aes.AesEncript(state,key_size,key)
            encrypt_blocks.append(out)
            aes.FormatOutput(state,"Jasni blok: ")
            temp = aes.FormatOutput(out, "Kriptirani blok: ")
            full_text = full_text + temp
        print "-------------------------------------------"
        print "Kriptirana poruka: "
        print full_text
        print "\n"
        return encrypt_blocks

    def ECBdecrypt(self, encrypt_blocks, key, key_size, remove):
        full_text = ''
        aes = AES()
        decrypted_blocks = []
        for block in encrypt_blocks:
            state = block
            out = aes.AesDecrypt(state, key_size, key)
            decrypted_blocks.append(out)
        return decrypted_blocks

    def XOR(self, output, plain_tekst):
        temp = []
        for i in range(0, len(output)):
            new_value = output[i] ^ plain_tekst[i]
            temp.append(new_value)
        return temp

    def StringToHex(self,output):
        print in_string
        out = ''
        for i in range(0, len(output)):
            mini = hex(output[i])
            out = out + mini[mini.find('x')+1:]
        #print out
        return out

    def ListToNumber(self, list_num):
        string = ''
        for char in list_num:
            string = string + hex(char)
        a = self.StringToHex(string)
        return int(a,16)

    def IncCounter(self, num, counter):
        block_modify = 15 - num // 256
        counter[block_modify] = counter[block_modify] + 1
        return counter

    def CTRencrypt(self, blocks, key, key_size):
        IV = [0]*16
        aes = AES()
        counter = IV[:]
        full_text = ''
        encrypted_blocks = []
        for i in range(0,len(blocks)):
            state = aes.AesEncript(counter,key_size,key)
            enc_block = []
            enc_block = self.XOR(state, blocks[i])
            encrypted_blocks.append(enc_block)
            counter = self.IncCounter(i,counter)
            aes.FormatOutput(blocks[i],"Jasni blok: ")
            temp = aes.FormatOutput(enc_block, "Kriptirani blok: ")
            full_text = full_text + temp
        print "-------------------------------------------"
        print "Kriptirana poruka: "
        print full_text
        print "\n"
        return encrypted_blocks

    def CTRdecrypt(self, encrypt_blocks, key, key_size, remove):
        IV = [0]*16
        aes = AES()
        counter = IV[:]
        full_text = ''
        decrypted_blocks = []
        for i in range(0,len(blocks)):
            state = aes.AesEncript(counter,key_size,key)
            enc_block = []
            enc_block = self.XOR(state, encrypt_blocks[i])
            decrypted_blocks.append(enc_block)
            counter = self.IncCounter(i,counter)
            #full_text = full_text + temp
        return decrypted_blocks

    def GetKey(self, size):
        #array_len = size // 8
        key = []
        for i in range(0, size):
            num = random.randrange(0,255)
            key.append(num)

        return key
            

        
if __name__ == "__main__":
    message = raw_input("Unesite poruku: ")
    print "--------------------------------"
    print "1 -> ECB nacin kriptiranja"
    print "2 -> CTR nacin kriptiranja"
    print "--------------------------------"
    choice = input("?:")
    key_size = input("Velicina kljuca [16, 24, 32]?:")
    if choice == 1:
        #key_size = 32
        #key = [0x60,0x3d,0xeb,0x10,0x15,0xca,0x71,0xbe,0x2b,0x73,0xae,0xf0,0x85,0x7d,0x77,0x81,0x1f,0x35,0x2c,0x07,0x3b,0x61,0x08,0xd7,0x2d,0x98,0x10,0xa3,0x09,0x14,0xdf,0xf4]
        #key = [0x2b,0x7e,0x15,0x16,0x28,0xae,0xd2,0xa6,0xab,0xf7,0x15,0x88,0x09,0xcf,0x4f,0x3c]
        op = Operation()
        key = op.GetKey(key_size)
        tekst_hex = op.ConvertToHex(message)
        blocks = []
        e_blocks = []
        d_blocks = []
        blocks, lbl = op.GetBlocks(tekst_hex)
        e_blocks = op.ECBencrypt(blocks, key, key_size)
        d_blocks = op.ECBdecrypt(e_blocks,key,key_size,lbl)
        op.ReturnToChar(d_blocks,lbl)
    else:
        #key_size = 32
        #key = [0x60,0x3d,0xeb,0x10,0x15,0xca,0x71,0xbe,0x2b,0x73,0xae,0xf0,0x85,0x7d,0x77,0x81,0x1f,0x35,0x2c,0x07,0x3b,0x61,0x08,0xd7,0x2d,0x98,0x10,0xa3,0x09,0x14,0xdf,0xf4]
        op = Operation()
        key = op.GetKey(key_size)
        tekst_hex = op.ConvertToHex(message)
        blocks = []
        e_blocks = []
        d_blocks = []
        blocks, lbl = op.GetBlocks(tekst_hex)
        e_blocks = op.CTRencrypt(blocks, key, key_size)
        d_blocks = op.CTRdecrypt(e_blocks,key,key_size,lbl)
        op.ReturnToChar(d_blocks,lbl)
    
    
