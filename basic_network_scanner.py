#import all methods needed from scapy
from scapy.all import ARP, Ether, srp

#IP address for destination 
target_ip = "23.19.225.248/24"

#create ARP (Address Resolution Protocol packet
#The need for an ARP request arises when a device wants to know the MAC address of the device to which the source wants to communicate with.
arp = ARP(pdst=target_ip)

#create ether broadcast and ff:ff:ff:ff:ff:ff MAC address inidcates broadcasting address
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether/arp

result = srp(packet, timeout=3)[0]

#client list will hold address.
clients=[]

for sent, received in result:
    #for each ip and mac address append (add) it to the clients list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    
#print clients
print("Available devices on the network")
print("IP" + " "*18 +"MAC")

for client in clients:
    print("{:16}   {}".format(client['ip'], client['mac']))
    


