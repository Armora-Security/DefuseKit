import tkinter as tk
import socket
import threading

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Armora™ Chat Interface")

        self.chat_log = tk.Text(root)
        self.chat_log.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.bind("<Return>", self.send_message)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("0.0.0.0", 5000))

        threading.Thread(target=self.receive_messages).start()

    def send_message(self, event=None):
        msg = self.entry.get()
        self.chat_log.insert(tk.END, f"You: {msg}\n")
        self.entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            msg, addr = self.sock.recvfrom(4096)
            self.chat_log.insert(tk.END, f"Remote: {msg.decode()}\n")

root = tk.Tk()
app = ChatApp(root)
root.mainloop()
