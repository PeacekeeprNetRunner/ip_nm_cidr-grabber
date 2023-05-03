  GNU nano 5.4                                                                               ownip.py                                                                                         
        for octet in octets:
                binary_str += bin(int(octet))[2:].zfill(8)

        cidr = 0
        for bit in binary_str:
                if bit == "1":
                        cidr += 1

        return cidr

ip = socket.gethostbyname(socket.gethostname())
print("Loopback IP: ", ip)

interfaces = netifaces.interfaces()

wlan_interface = None
for iface in interfaces:
        if "wlan" in iface:
                wlan_interface = iface
                break

if wlan_interface:
        addrs = netifaces.ifaddresses(wlan_interface)
        w_ip = addrs[netifaces.AF_INET][0]["addr"]
        iface_addrs = addrs[netifaces.AF_INET]
        iface_dict = iface_addrs[0]
        netmask = iface_dict.get('netmask')
        print("Netmask: ", netmask)
        cidr = subnet_mask_to_cidr(netmask)
        print("CIDR:", cidr)
        print("Wlan IP: ", w_ip)
else:
        print("No WLAN Interface to pull from.")

octets = w_ip.split(".")

octets[-1] = "0"

w_ip = ".".join(octets)

print("Lowest: ", w_ip)

target = (str(w_ip) + "/" + str(cidr))
print("Current Target:", target)
