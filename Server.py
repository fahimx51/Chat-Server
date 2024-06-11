import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class ChatServer:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Server")
        self.master.geometry("400x300")
        
        self.start_button = tk.Button(master, text="Start", command=self.start_server)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_server, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.text_area = scrolledtext.ScrolledText(master, state='disabled')
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.server_label = tk.Label(master, text="Server IP: N/A\nPort: N/A")
        self.server_label.pack(pady=10)
        
        self.server = None
        self.clients = []
        self.running = False

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', 12345))
        self.server.listen(5)
        
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        threading.Thread(target=self.accept_clients).start()
        
        host_ip = socket.gethostbyname(socket.gethostname())
        self.server_label.config(text=f"Server IP: {host_ip}\nPort: 12345")
        self.display_message("Server started on port 12345")

    def stop_server(self):
        self.running = False
        for client in self.clients:
            client.close()
        if self.server:
            self.server.close()
        
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.server_label.config(text="Server IP: N/A\nPort: N/A")
        self.display_message("Server stopped")

    def accept_clients(self):
        while self.running:
            client, addr = self.server.accept()
            self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client,)).start()
            self.display_message(f"Client connected: {addr}")

    def handle_client(self, client):
        while self.running:
            try:
                msg = client.recv(1024).decode('utf-8')
                if msg:
                    self.broadcast(msg, client)
                    self.display_message(msg)
            except:
                self.clients.remove(client)
                client.close()
                break

    def broadcast(self, msg, client):
        for c in self.clients:
            if c != client:
                try:
                    c.send(msg.encode('utf-8'))
                except:
                    self.clients.remove(c)
                    c.close()

    def display_message(self, msg):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, msg + '\n')
        self.text_area.yview(tk.END)
        self.text_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatServer(root)
    root.mainloop()
