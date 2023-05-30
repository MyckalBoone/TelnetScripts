import getpass
import telnetlib

HOST = "Host IP"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

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
