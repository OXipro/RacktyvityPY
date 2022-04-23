import telnetlib
from time import sleep

user = "admin"  # login de base
password = "1234"  # mdp d-e base


def prise(status, prise):
    tn = telnetlib.Telnet(host="192.168.111.19", port=23)
    sleep(0.1)
    print(tn.read_until(b"Login:").decode('ascii'))
    tn.write(b"admin" + b"\r\n")
    sleep(0.1)
    print(tn.read_until(b"Password:").decode('ascii'))
    tn.write(b"1234" + b"\r\n")
    sleep(0.1)
    print(tn.read_until(b">").decode('ascii'))
    tn.write(b"set p1 portstat " + format(prise).encode() + format(" ").encode() + format(status).encode() + b"\r\n")
    print(tn.read_until(b".").decode('ascii'))
    tn.close()
