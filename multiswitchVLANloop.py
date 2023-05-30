import getpass
import telnetlib

HOST = "Host IP"
user = input("Enter your telnet username: ")
password = getpass.getpass()

# Get IP Addresses of the switches from the file
f = open('IP Address file')

# For each IP address in the file -> login -> conf t -> add vlans
for IP in f:
    IP=IP.strip()
    print("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    for n in range (2,101)
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(password\n)
    tn.write(b"conf t")
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN 2\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN 3\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name Python_VLAN 4\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
