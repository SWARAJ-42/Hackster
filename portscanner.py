import socket
from IPy import IP
import termcolor

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_single_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(.5)
        sock.connect((target, port))
        try:
            banner = sock.recv(1024).decode().strip("\n").strip("\r")
            print(termcolor.colored((f"[+] Open port at {port} : {banner}"), "green"))
        except:
            print(termcolor.colored((f"[+] Open port at {port}"), "yellow"))
    except:
        print(termcolor.colored((f"[-] Closed port at {port}"), "red"))


def scan_mul_ports(target, port_init, port_range):
    target_mod = check_ip(target)
    print(f"\n[+]Started scanning for target {target}")
    for i in range(port_init, port_init+port_range):
        scan_single_port(target_mod, i)


def scan_mul_targets(targets: str, port_init, port_range):
    for ind_target in targets.split(","):
        scan_mul_ports(ind_target.strip(" "), port_init, port_range)
