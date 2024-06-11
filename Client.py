import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Client")
        self.master.geometry("400x450")
        
        self.top_frame = tk.Frame(master)
        self.top_frame.pack(pady=10)
        
        self.username_label = tk.Label(self.top_frame, text="Username:")
        self.username_label.pack(side=tk.LEFT)
        
        self.username_entry = tk.Entry(self.top_frame)
        self.username_entry.pack(side=tk.LEFT, padx=5)
        
        self.ip_label = tk.Label(self.top_frame, text="IP Address:")
        self.ip_label.pack(side=tk.LEFT)
        
        self.ip_entry = tk.Entry(self.top_frame)
        self.ip_entry.pack(side=tk.LEFT, padx=5)
        
        self.port_label = tk.Label(self.top_frame, text="Port:")
        self.port_label.pack(side=tk.LEFT)
        
        self.port_entry = tk.Entry(self.top_frame)
        self.port_entry.pack(side=tk.LEFT, padx=5)
        
        self.connect_button = tk.Button(self.top_frame, text="Connect", command=self.connect_to_server)
        self.connect_button.pack(side=tk.LEFT, padx=5)
        
        self.text_area = scrolledtext.ScrolledText(master, state='disabled')
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack(pady=10)
        
        self.msg_entry = tk.Entry(self.bottom_frame, width=40)
        self.msg_entry.pack(side=tk.LEFT, padx=5)
        
        self.send_button = tk.Button(self.bottom_frame, text="Send", command=self.send_message, state=tk.DISABLED)
        self.send_button.pack(side=tk.LEFT)
        
        self.client = None
        self.running = False

    def connect_to_server(self):
        ip = self.ip_entry.get()
        port = int(self.port_entry.get())
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))
        self.username = self.username_entry.get()
        
        self.running = True
        threading.Thread(target=self.receive_messages).start()
        
        self.connect_button.config(state=tk.DISABLED)
        self.send_button.config(state=tk.NORMAL)
        self.display_message(f"Connected as {self.username}")

    def receive_messages(self):
        while self.running:
            try:
                msg = self.client.recv(1024).decode('utf-8')
                if msg:
                    self.display_message(msg)
            except:
                self.running = False
                self.client.close()
                break

    def send_message(self):
        msg = f"{self.username}: {self.msg_entry.get()}"
        self.display_message(msg)  # Display message locally
        self.client.send(msg.encode('utf-8'))
        self.msg_entry.delete(0, tk.END)

    def display_message(self, msg):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, msg + '\n')
        self.text_area.yview(tk.END)
        self.text_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()
