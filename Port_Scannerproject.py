import socket
import re
import tkinter as tk
from tkinter import messagebox

class Portscanner:#super class oop
    def __init__init(self, port, target):
        self.port = port
        self.target = target

    def portscanner(self):
        return 0

class TCP_port(Portscanner):#inheritance
    def __init__(self, port, target):
        super().__init__(port, target)

    def portscanner(self):#override
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target, self.port))
            return f"{self.port} is Open"
        except socket.error:
            return f"{self.port} is Closed"
        finally:
            sock.close()

class UDP_port(Portscanner):
    def __init__(self, port, target):
        super().__init__init(port, target)

    def portscanner(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b'', (self.target, self.port))
            return f"{self.port} is Open"
        except socket.error:
            return f"{self.port} is Closed"
        finally:
            sock.close()
list1 = []# to add ports 
list2 = []#to add service of ports http https etc..
def scan_ports():
    userIP = user_ip_entry.get() #choose 1 TCP or 2 UDP
    target_Ip = target_ip_entry.get()
    from_port = int(from_port_entry.get())#range of PORTS
    to_port = int(to_port_entry.get())

    if not re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.', target_Ip):#NNN.NNN.NNN
        messagebox.showerror("Error", "Invalid IP Address")
        return

    if from_port < 0 or to_port > 65535 or from_port > to_port:
        messagebox.showerror("Error", "Invalid Range of Ports")
        return

    if userIP == "1":  # user chose TCP
        for i in range(from_port, to_port + 1):
            service_name = socket.getservbyport(i)
            list2.append(service_name)
            obj1 = TCP_port(i, target_Ip)
            result = obj1.portscanner()
            list1.append(result)

    elif userIP == "2":  # user chose UDP
        for i in range(from_port, to_port + 1):
            service_name = socket.getservbyport(i)
            list2.append(service_name)
            obj1 = UDP_port(i, target_Ip)
            result = obj1.portscanner()
            list1.append(result)

    result_text.delete(1.0, tk.END)  # Clear previous results
    for result in list1:
        result_text.insert(tk.END, f"{result}\n")
def SERFILE():
    S = input("User, please enter Service:").lower()
    with open("SERVICE.txt", 'w') as F1:
        for i,v in zip(list1, list2):#dicionatry
            if v.lower() == S:
                F1.write(f"Port {i} is associated with the service {v}\n")
    with open('SERVICE.txt', 'r') as file:
      content = file.read()
      print(content)            

    messagebox.showinfo("Scan Complete", "Port scan completed. Results written to SERVICE.txt")

# Create the main window
root = tk.Tk()
root.title("Port Scanner")

# Set background color to beige
root.configure(bg='beige')

# GUI components
user_ip_label = tk.Label(root, text="User IP (1 for TCP, 2 for UDP):", bg='beige')
user_ip_label.grid(row=0, column=0, pady=5)
user_ip_entry = tk.Entry(root)
user_ip_entry.grid(row=0, column=1, pady=5)

target_ip_label = tk.Label(root, text="Target IP:", bg='beige')
target_ip_label.grid(row=1, column=0, pady=5)
target_ip_entry = tk.Entry(root)
target_ip_entry.grid(row=1, column=1, pady=5)

from_port_label = tk.Label(root, text="From Port:", bg='beige')
from_port_label.grid(row=2, column=0, pady=5)
from_port_entry = tk.Entry(root)
from_port_entry.grid(row=2, column=1, pady=5)

to_port_label = tk.Label(root, text="To Port:", bg='beige')
to_port_label.grid(row=3, column=0, pady=5)
to_port_entry = tk.Entry(root)
to_port_entry.grid(row=3, column=1, pady=5)

scan_button = tk.Button(root, text="Scan", command=scan_ports, bg='lightblue')
scan_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

result_text = tk.Text(root, height=10, width=50, wrap=tk.WORD)
result_text.grid(row=5, column=0, columnspan=2, pady=(10, 0))
service_button = tk.Button(root, text="Service", command=SERFILE, bg='lightblue')
service_button.grid(row=9, column=0, columnspan=2, pady=(10, 0))

result_text = tk.Text(root, height=10, width=50, wrap=tk.WORD)
result_text.grid(row=10, column=0, columnspan=2, pady=(10, 0))



root.mainloop()