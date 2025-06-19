#!/usr/bin/env python3
import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

SERVER_IP = input("Enter server IP: ")
PORT = 12345
KEY = os.urandom(32)  # Harus sama dengan server

def encrypt_data(key, iv, data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def send_data(sock, data):
    iv = os.urandom(16)
    padded_data = data + b' ' * ((16 - len(data) % 16) % 16)
    encrypted = encrypt_data(KEY, iv, padded_data)
    sock.send(iv)
    sock.send(encrypted)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, PORT))
    client_ip = s.recv(16).decode()
    print(f"[*] You are assigned IP: {client_ip}")

    while True:
        msg = input("Send to server: ").strip()
        if msg.lower() in ['exit', 'quit']:
            break
        send_data(s, msg.encode())
