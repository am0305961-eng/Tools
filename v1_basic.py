# Port Scanner v1.0
# Author: DrFox
import socket

Target_ip = input("Enter The Ip You Want To Scan: ")

print("Scanning...")
for i in range (1 , 1025):
    s = socket.socket()
    s.settimeout(0.1)
    call = s.connect_ex((Target_ip , i))
    s.close()
    if call == 0:
        print(f"Port {i} Is Open")

    

