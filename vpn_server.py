#!/usr/bin/env python3
import socket
import threading
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import random

KEY = os.urandom(32)  # AES-256 key
PORT = 12345
CLIENT_IP_POOL = ["10.0.0." + str(i) for i in range(2, 20)]

clients = {}

def decrypt_data(key, iv, data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()

def encrypt_data(key, iv, data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def handle_client(conn, addr):
    print(f"[+] Client connected from {addr}")
    try:
        client_ip = random.choice(CLIENT_IP_POOL)
        CLIENT_IP_POOL.remove(client_ip)
        conn.send(client_ip.encode())
        print(f"[*] Assigned IP: {client_ip}")

        iv = conn.recv(16)
        while True:
            encrypted = conn.recv(4096)
            if not encrypted:
                break
            decrypted = decrypt_data(KEY, iv, encrypted)
            print(f"[>] From {client_ip}: {decrypted.decode('utf-8', errors='ignore')}")
    except Exception as e:
        print(f"[!] Error handling client {addr}: {e}")
    finally:
        conn.close()
        if client_ip in clients.values():
            del clients[addr]
        CLIENT_IP_POOL.append(client_ip)
        print(f"[-] Client {addr} disconnected.")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", PORT))
        s.listen(5)
        print(f"[*] Armora™ VPN Server running on port {PORT}...")

        while True:
            conn, addr = s.accept()
            clients[addr] = conn
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
