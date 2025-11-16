from github import *
import tkinter as t
import socket
import os
import json
import netaddr as net
import requests


#Classes
class User:
    def __init__(self, name, room,ip,code):
        self.room = room
        self.name = name
        self.ip = ip
        self.code = code
        
    def state(self):
        print(f"{self.name}: {self.room}: {self.ip}: {self.code}")

class Item(t.Frame):
    def __init__(self, parent, name, price):
        super().__init__(parent, relief=t.RAISED, borderwidth=1, padx=5, pady=5)

        t.Label(self, text=name, font=("Arial", 12, "bold")).pack()
        t.Label(self, text=f"${price}").pack()

#Var
with open("goonected.txt", "r") as v:
    rah = v.read()
Key = Github(str(rah)) #dont steal please and dont hurt  my repos :beg emoji:
Repo = Key.get_repo('Epuos/GetYgoCodeQuick')
CurrentAccount = User(None,"main.json",None,None)
entry = "temp"
try:
    CurrentAccount.ip = requests.get('https://api.ipify.org').text
    print(f"Your public IP address is: {CurrentAccount.ip}")
except requests.RequestException as e:
    print(f"Error retrieving public IP address: {e}")



#func
def git_update(text='x', repodirct= CurrentAccount.room):    
    try:
        file = Repo.get_contents(CurrentAccount.room)
        old = file.decoded_content.decode("utf-8")
        new = old + text + "\n"
        Repo.update_file(repodirct, "skibidi text!", new, file.sha)
    except Exception as e:
        print("GitE:", e)    

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def create(path = f"{get_local_ip()}.json"):
    info = {
    "name":f"{CurrentAccount.name}",
    "ip":f"{CurrentAccount.ip}",
    "code":f"{CurrentAccount.code}",
    }
    with open(path, "w") as acc:  
        json.dump(info, acc, indent=4)
    with open(path, "r") as acc:
        uploaddeez = acc.read()
    Repo.create_file(path, "committing files", uploaddeez)
    os.remove(path)





def handle_placeholder(event):
    if event.type == '9':  # FocusIn
        if entry.get() == 'Enter text here...':
            entry.delete(0, t.END)
            entry.config(fg='black')
    else:  # FocusOut
        if entry.get() == '':
            entry.insert(0, 'Enter text here...')
            entry.config(fg='grey')



def One():
    global entry
    root = t.Tk()
    root.configure(background='#586BA4')
    root.title("Get Ygo Code")
    root.geometry("150x100")
    
    # Name entry with placeholder
    Name = t.Entry(root, fg='grey')
    Name.insert(0, 'Enter name...')
    Name.pack()
    
    # Code entry with placeholder
    Code = t.Entry(root, fg='grey')
    Code.insert(0, 'Enter Room Code...')
    Code.pack()
    
    def handle_placeholder(event):
        widget = event.widget
        placeholder = 'Enter name...' if widget == Name else 'Enter Room Code...'
        
        if event.type == '9':  # FocusIn
            if widget.get() == placeholder:
                widget.delete(0, t.END)
                widget.config(fg='white')
        else:  # FocusOut
            if widget.get() == '':
                widget.insert(0, placeholder)
                widget.config(fg='grey')
    
    Name.bind('<FocusIn>', handle_placeholder)
    Name.bind('<FocusOut>', handle_placeholder)
    Code.bind('<FocusIn>', handle_placeholder)
    Code.bind('<FocusOut>', handle_placeholder)
    
    def GetAll():
        CurrentAccount.name = Name.get()
        CurrentAccount.code = Code.get()
        git_update(
f"""
    "{get_local_ip()}":{{
    "name":"{CurrentAccount.name}"
    "ip":"{CurrentAccount.ip}",
    "code":"{CurrentAccount.code}",
    }}
    }}
""")
        root.destroy()
    
    t.Button(root, text="Submit", command=lambda: GetAll()).pack()
    root.mainloop()

def Two():
    root = t.Tk
    root.geometry("150x100")
    Item(root, "", 999).pack(fill=t.X, padx=10, pady=5)
    Item(root, "Mouse", 29).pack(fill=t.X, padx=10, pady=5)
    Item(root, "Keyboard", 149).pack(fill=t.X, padx=10, pady=5)
    

#main
if __name__ == "__main__":
    One()
