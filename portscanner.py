import socket

from termcolor import colored

def scan(target, ports):
    for p in range(1, ports):
        scan_port(target, p)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(colored(f'[+] Port {port} on {ipaddress} open', 'green'))
        sock.close()
    except:
        pass
    
targets = input("[*] Enter Targets to Scan(split by ,): ")
ports = int(input("[*] How many ports to Scan? "))

if ',' in targets:
    targetList = targets.split(',')
    for t in targetList:
        print(colored(f'Scanning {t}...', 'red'))
        scan(t.strip(' '), ports)
else:
    scan(targets.strip(' '), ports)

