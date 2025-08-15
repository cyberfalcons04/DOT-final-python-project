import socket
import ipaddress
from scapy.all import ARP, Ether, srp

def getting_ip():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #Class
    s.connect(("8.8.8.8",80)) #method to connect to a public 
    ip= s.getsockname()[0] #method to get the local IP address
    s.close() #close the socket
    return ip
def getting_host():
    host_name= socket.gethostname() 
    return host_name

def domain():
    ip=getting_ip()
    try:
        domain_name = socket.gethostbyaddr(ip)[0]  
    except socket.herror:
        domain_name = "Domain not found"
    return domain_name
def scan_network():
    local_ip = getting_ip()
    network = ipaddress.ip_network(local_ip + "/24", strict=False)
    print("\n[+] Scanning network range:", network)
    for ip in network.hosts():
        print(ip)    
    arp = ARP(pdst=str(network))
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    answered, _ = srp(packet, timeout=2, verbose=False)

    devices = []
    for sent, recv in answered:
        devices.append({'ip': recv.psrc, 'mac': recv.hwsrc})

    
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

    return devices    
def arp_scan():
    local_ip = getting_ip()
    network = ipaddress.ip_network(local_ip + "/24", strict=False)
    print(f"\n Scanning network: {network}\n")
    
    
    arp = ARP(pdst=str(network))
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    answered, _ = srp(packet, timeout=2, verbose=False)

    devices = []
    for sent, recv in answered:
        devices.append({'ip': recv.psrc, 'mac': recv.hwsrc})

    
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

    return devices

    

print(f'Local IP: {getting_ip()}')
print(f'Host Name: {getting_host()}')
print(f'Domain Name: {domain()}')

arp_scan()