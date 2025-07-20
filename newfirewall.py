import tkinter as tk
from netfilterqueue import NetfilterQueue
from scapy.all import IP
import threading
import os
import subprocess

# Global blacklist
blacklist = []

# Firewall logic
def process_packet(packet):
    pkt = IP(packet.get_payload())
    if pkt.src in blacklist:
        log(f"[BLOCKED] {pkt.src}")
        packet.drop()
    else:
        log(f"[ALLOWED] {pkt.src}")
        packet.accept()

def start_firewall():
    log("[*] Starting firewall...")
    subprocess.call(["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "1"])
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, process_packet)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        nfqueue.unbind()

def run_firewall_thread():
    threading.Thread(target=start_firewall, daemon=True).start()

def stop_firewall():
    log("[*] Stopping firewall...")
    subprocess.call(["sudo", "iptables", "-F"])

def add_ip():
    ip = ip_entry.get()
    if ip and ip not in blacklist:
        blacklist.append(ip)
        update_blacklist()
        ip_entry.delete(0, tk.END)

def update_blacklist():
    blacklist_text.delete(1.0, tk.END)
    for ip in blacklist:
        blacklist_text.insert(tk.END, f"{ip}\n")

def log(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)

# GUI
root = tk.Tk()
root.title("Python Firewall GUI")
root.geometry("500x400")

tk.Label(root, text="Enter IP to Block:").pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

tk.Button(root, text="Add to Blacklist", command=add_ip).pack()
tk.Button(root, text="Start Firewall", command=run_firewall_thread).pack()
tk.Button(root, text="Stop Firewall", command=stop_firewall).pack()

tk.Label(root, text="Blacklisted IPs:").pack()
blacklist_text = tk.Text(root, height=5)
blacklist_text.pack()

tk.Label(root, text="Logs:").pack()
log_text = tk.Text(root, height=10)
log_text.pack()

root.mainloop()