import socket
import termcolor

def scan(target, ports):
    for p in range(1, ports):
        scan_port(target, p)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f'Port {port} on {ipaddress} opened')
        sock.close()
    except:
        print(f'Port {port} on {ipaddress} closed')
    
targets = input("[*] Enter Targets to Scan(split by ,): ")
ports = int(input("[*] How many ports to Scan? "))

if ',' in targets:
    targetList = targets.split(',')
    for t in targetList:
        print(f'Scanning {t}...')
        scan(t.strip(' '), ports)
else:
    scan(targets.strip(' '), ports)
