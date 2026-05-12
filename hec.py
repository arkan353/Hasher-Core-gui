import hashlib;import sys;import random

#hec = hashlib.md5(b"1950")
#print(hec.hexdigest())
END = '\033[0m'

__author__ = "k1rpit"
__version__ = "1.0"

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

salts =[
    '05c2f2','039b9d','0305d53','0b9d99','0535d0cf4fc'
    ,'0c9190dd4','0b2441','0xp39i','0244448','0bcbf115a',
    '04448cb343aa688f5d3efd','0234346767G37467','0e580ac0bcbf115aeca9e8dc114',
    '04f93b6c9190dd46e009919','00040b24411','0257b7efad6ef9','0QWNnwihcsd3fd'
]


def start():
    print(f'''{GREEN}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
███████████████████████████████████████████████████████████████ by->k1rpit
█─█─██▀▄─██─▄▄▄▄█─█─█▄─▄▄─█▄─▄▄▀█▀▀▀▀▀██─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄─█
█─▄─██─▀─██▄▄▄▄─█─▄─██─▄█▀██─▄─▄████████─███▀█─██─██─▄─▄██─▄█▀█
▀▄▀▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  {END}  ''')
def help():
    print(f'''{BLUE}
    [1]--MD5-classic        [0]-exit
    [2]--SHA-1-legacy       
    [3]--SHA2_256-standart
    [4]--SHA2_512-big
    [5]-salt
   {END} ''')
start()
help()

def sl(s):
    sa = random.choice(salts)
    s = s+sa
    print(f'{BLUE}[+]salt->{sa}\n[+]hash_salt->{s}')

def hech_md5(ppw):
    q1=hashlib.md5(ppw.encode()).hexdigest()
    print(f'{GREEN}[+]pw->{ppw}\n[+]hash->md5\n[+]hash_pw->{q1}{END}')

def hech_SHA1(ppw1):
    q1 = hashlib.sha1(ppw1.encode()).hexdigest()
    print(f'{GREEN}[+]pw->{ppw1}\n[+]hash->sha1\n[+]hash_pw->{q1}{END}')


def hech_SHA2(ppw2):
    q1 = hashlib.sha256(ppw2.encode()).hexdigest()
    print(f'{GREEN}[+]pw->{ppw2}\n[+]hash->sha2_256\n[+]hash_pw->{q1}{END}')

def hech_SHA4(ppw4):
    q1 = hashlib.sha512(ppw4.encode()).hexdigest()
    print(f'{GREEN}[+]pw->{ppw4}\n[+]hash->sha2_512\n[+]hash_pw->{q1}{END}')
try:
    while True:
        A = input('[?]>>>')
        if A == '1':
            ppw = input('[1]>>>')
            hech_md5(ppw)
        elif A == '2':
            ppw1 = input('[2]>>>')
            hech_SHA1(ppw1)
        elif A == '3':
            ppw2 = input('[3]>>>')
            hech_SHA2(ppw2)
        elif A == '4':
            ppw4 = input('[4]>>>')
            hech_SHA4(ppw4)
        elif A == '0':
            sys.exit()
        elif A == '5':
            s = input('[5]>>>')
            sl(s)

except KeyboardInterrupt:
    print(f"{PURPLE}пока!{END}")