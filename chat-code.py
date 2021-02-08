import socket
import threading
import os
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system("tput setaf 012")
ip=input("\n\t\tEnter Your ID : ")
port=1234

s.bind((ip,port))

sip=input("\n\t\tEnter Friend's ID : ")
sport=1234

print()
os.system('clear')
os.system('tput setaf 22')
os.system('figlet -f script Friend Zone')
print("\n\t\t")
print('\n\t\t>>'+os.system('date +"%d-%m-%y"')+'<<')

def send():
    while True:
        os.system('tput setaf 55')
        msg=input('\n').encode()
        s.sendto(msg,(sip,sport))
        if msg.decode() == "exit":
            os.system('tput setaf 7')
            os._exit(1)


def recv():
    while True:
        os.system('tput setaf 33')
        print('')
        msg=s.recvfrom(1024)
        if msg[0].decode()=="exit":
            os._exit(1)
        print('\n\t\t\t\t  msg from @' + sip + ': '  + msg[0].decode())
        os.system('tput setaf 28')
        print('\n\t\t\t <Time: ' + os.system('date +%T%p') + '>')

t1=threading.Thread(target=send)
t2=threading.Thread(target=recv)

t1.start()
t2.start()

