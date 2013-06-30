#-*- coding: cp1250 -*-

## Python version 2.5

def load(fp):
    ## Loads the data from the input file in a dictionary.
    data = []
    while True:
        line = fp.readline()
        if line == '':
            break
        line = line.strip()
        if line != '':
            data.append(line)
    keywords = ['Description', 'File name', 'Method', 'Key length', 
                'Secret key', 'Modulus', 'Private exponent', 'Public exponent', 
                'Signature', 'Data', 'Envelope data', 'Envelope crypt key']
    beginning = '---BEGIN OS2 CRYPTO DATA---'
    ending = '---END OS2 CRYPTO DATA---'
    while data[0] != beginning:
        data.pop(0)
    while data[len(data)-1] != ending:
        data.pop()
    items = {}
    i = 0
    while True:
        if data[i] == ending:
            break
        elif data[i] == beginning:
            i += 1
            continue
        elif data[i][len(data[i])-1] == ':' and data[i][0:len(data[i])-1] in keywords:
            activeKeyword = data[i][0:len(data[i])-1]          
            items[activeKeyword] = []
            i += 1
        else:
            items[activeKeyword].append(data[i])
            i += 1
    return items

def dump(keydata):
    for i in keydata:
        print i
        for j in keydata[i]:
            print '  ' + j

def get_items(name, keydata):
    ### Returns the data associated with the given key (or name). 
    if name in keydata:
        return keydata[name]    
    else:
        return None
    
def get_n_value(name, No, keydata):
    ## Used for retrieving key lengths. Returns the length in the decimal base 
    ## of either the first or the second key, depending on No.
    if name not in keydata:
        return None
    from string import atoi
    hval = keydata[name][No]
    return atoi(hval, 16)

def get_hexc_value(name, keydata):
    ## Used for retrieving various data. Returns all of the data associated 
    ## with the key (or name), but merged in a single string.
    if name not in keydata:
        return None
    return ''.join(keydata[name])

def get_hex8_value(name, keydata):
    ## Used for retriving various data that represents hexadecimal numbers. 
    ## Returns a list of positive decimal numbers that correspond to 2-digit 
    ## hexadecimal numbers.
    if name not in keydata:
        return None
    data = get_hexc_value(name, keydata)
    length = len(data)
    if length % 2 != 0:
        data = data.zfill(length + 1)
    position = 0
    bit8 = []
    from string import atoi
    while position < len(data):
        bit8.append(atoi(data[position:position+2], 16))
        position += 2
    return bit8

def get_hex16_value(name, keydata):
    ## Used for retriving various data that represents hexadecimal numbers. 
    ## Returns a list of positive decimal numbers that correspond to 4-digit 
    ## hexadecimal numbers.
    if name not in keydata:
        return None
    data = get_hexc_value(name, keydata)
    length = len(data)
    if length % 4 != 0:
        data = data.zfill(length + 4 - length % 4)
    position = 0
    bit16 = []
    from string import atoi
    while position < len(data):
        bit16.append(atoi(data[position:position+4], 16))
        position += 4
    return bit16

def get_hex32_value(name, keydata):
    ## Used for retriving various data that represents hexadecimal numbers. 
    ## Returns a list of positive decimal numbers that correspond to 8-digit 
    ## hexadecimal numbers.
    if name not in keydata:
        return None
    data = get_hexc_value(name, keydata)
    length = len(data)
    if length % 8 != 0:
        data = data.zfill(length + 8 - length % 8)
    position = 0
    bit32 = []
    from string import atoi
    while position < len(data):
        bit32.append(atoi(data[position:position+8], 16))
        position += 8
    return bit32

def get_b64_u8_value(name, keydata):
    ## Used for retrieving data written in Base64. Returns a string.
    if name not in keydata:
        return None
    from base64 import b64decode
    return b64decode(get_hexc_value(name, keydata))

def get_b64_u16_value(name, keydata):
    ## Used for retrieving data written in Base64. Returns a list of short
    ## integers.
    if name not in keydata:
        return None
    from base64 import b64decode
    data = b64decode(get_hexc_value(name, keydata))
    length = len(data)
    retval = []

    for i in xrange(0, length, 2):
        retval.append((ord(data[i]) << 8) + ord(data[i+1]))
    
    if length % 2 != 0:
        retval.append(ord(data[i]) << 8)
    return retval
    

def get_b64_u32_value(name, keydata):
    ## Used for retrieving data written in Base64. Returns a list of integers.
    if name not in keydata:
        return None
    from base64 import b64decode
    data = b64decode(get_hexc_value(name, keydata))
    length = len(data)
    retval = []

    for i in xrange(0, length, 4):
        retval.append((ord(data[i]) << 24) + (ord(data[i+1]) << 16) + (ord(data[i+2]) << 8) + ord(data[i+3]))
    
    maximum = max(xrange(0, length, 4))
    dif = length - maximum
    
    if dif == 1:
        retval.append(ord(data[length-1]) << 24)
    elif dif == 2:
        retval.append((ord(data[length-2]) << 24) + ord(data[length-1]) << 16)
    elif dif == 3:
        retval.append((ord(data[length-3]) << 24) + ord(data[length-2]) << 16 + ord(data[length-1]) << 8)
    
    return retval

def put_header(mesg, fp):
    ## Writes a message (comment) and the file header in the output file.
    try:
        fp.writelines(mesg+'\n')
        fp.write('---BEGIN OS2 CRYPTO DATA---\n')
        return 1
    except:
        return 0
    
def put_footer(mesg, fp):
    ## Writes the file footer and a message(comment) in the output file.
    try:
        fp.write('---END OS2 CRYPTO DATA---\n')
        fp.writelines(mesg+'\n')
        return 1
    except:
        return 0
    
def put_data_d(name, value1, value2, fp):
    ## Used for writing keys in the output file.
    try:
        fp.write(name+':')
        value = str(hex(value1))[2:]
        if value[len(value)-1] == 'L':
            value = value[:len(value)-1]
        if len(value) % 2 != 0:
            value = value.zfill(len(value)+1)
        for i in range(0,len(value)):
            if i%60 == 0:
                fp.write('\n    ' + value[i])
            else:
                fp.write(value[i])
        fp.write('\n')
        #fp.write('    ' + value + '\n')
        if value2 != -1:
            value = str(hex(value2))[2:]
            if value[len(value)-1] == 'L':
                value = value[:len(value)-1]
            if len(value) % 2 != 0:
                value = value.zfill(len(value)+1)
            fp.write('    ' + value + '\n')
        fp.write('\n')
        return 1
    except:
        return 0
    
def put_data_s(name, value1, value2, fp):
    ## Used for writing simple, textual data.    
    try:
        fp.write(name + ':\n')
        fp.write('    ' + value1 + '\n')
        if value2 != None:
            fp.write('    ' + value2 + '\n')
        fp.write('\n')
        return 1
    except:
        return 0

def put_data(name, value, fp):
    fp.write(name+':')
    for i in range(0,len(value)):
        if (i%60 == 0):
            fp.write('\n    '+value[i])
        else:
            fp.write(value[i])
    fp.write('\n\n')
        
    
def put_data_hexu8(name, value, length, fp):
    ## Used for writing various hexadecimal data (stored in a string).
    try:
        fp.write(name + ':\n')
        if length % 2 != 0:
            value = str(value).zfill(length+1)
            length += 1
        position = 0
        while position < length:
            if position + 60 < length:
                fp.write('    ' + value[position:position+60] + '\n')
            else:
                fp.write('    ' + value[position:length] + '\n')
            position += 60
        fp.write('\n')
        return 1
    except:
        return 0

def put_data_hexu16(name, value, length, fp):
    ## Used for writing various hexadecimal data (stored in a list of short
    ## integers).
    s = ''
    for i in value:
        s += chr(i >> 8 & 255)
        s += chr(i & 255)
    return put_data_hexu8(name, s, len(s), fp)


def put_data_hexu32(name, value, length, fp):
    ## Used for writing various hexadecimal data (stored in a list of 
    ## integers).
    s = ''
    for i in value:
        s += chr(i >> 24)
        s += chr(i >> 16 & 255) 
        s += chr(i >> 8 & 255)
        s += chr(i & 255)
    return put_data_hexu8(name, s, len(s), fp)
    
def put_data_b64u8(name, value, length, fp):
    ## Used for writing data (stored in a string) in Base64 encoding.
    try:
        fp.write(name + ':\n')
        from base64 import b64encode
        data = b64encode(value)
        position = 0
        while position < len(data):
            if position + 60 < len(data):
                fp.write('    ' + data[position:position+60] + '\n')
            else:
                fp.write('    ' + data[position:len(data)] + '\n')
            position += 60
        fp.write('\n')
        return 1
    except:
        return 0
    
def put_data_b64u16(name, value, length, fp):
    ## Used for writing data (stored in a list of short integers) in Base64 
    ## encoding.
    s = ''
    for i in value:
        s += chr(i >> 8 & 255)
        s += chr(i & 255)
    return put_data_b64u16(name, s, len(s), fp)

def put_data_b64u32(name, value, length, fp):
    ## Used for writing data (stored in a list of integers) in Base64 encoding.
    s = ''
    for i in value:
        s += chr(i >> 24)
        s += chr(i >> 16 & 255) 
        s += chr(i >> 8 & 255)
        s += chr(i & 255)
    return put_data_b64u8(name, s, len(s), fp)
