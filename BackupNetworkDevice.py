import getpass
import telnetlib

HOST = "Host IP"
user = input("Enter your telnet username: ")
password = getpass.getpass()

# Get IP Addresses of the switch from the file
f = open('IP Address file')

for IP in f:
    IP=IP.strip()
    print("Get running config from Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n") #To show all of the show run cmd below
    tn.write(b"show run\n")
    tn.write(b'exit\n')

    readoutput = tn.read_all()
    saveoutput = open("switch" + HOST, "w") # open file "switch"+(HOST) as write
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close

    print(tn.read_all().decode('ascii')) #print outcome OPTIONAL
