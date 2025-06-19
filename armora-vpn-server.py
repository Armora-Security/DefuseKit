#!/usr/bin/env python3
import socket
import threading
import os
import logging
from pytun import TunTapDevice, IFF_TUN, IFF_TAP, IFF_NO_PI
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Setup logging
logging.basicConfig(
    filename='logs/server.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

KEY = os.urandom(32)
IV_SIZE = 16
PORT = 12345
CLIENT_IP = "10.0.0.2"
SERVER_IP = "10.0.0.1"

clients = {}

def decrypt_data(key, iv, data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()

def encrypt_data(key, iv, data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def setup_tun_device():
    tun = TunTapDevice(name="tun0", flags=IFF_TUN | IFF_NO_PI)
    tun.addr = SERVER_IP
    tun.netmask = "255.255.255.0"
    tun.up()
    os.system("ip link set tun0 up")
    os.system("ip addr add 10.0.0.1/24 dev tun0")
    os.system("ip route add 10.0.0.0/24 dev tun0")
    return tun

def handle_client(conn, addr, tun):
    try:
        conn.send(SERVER_IP.encode())
        iv = conn.recv(IV_SIZE)
        while True:
            encrypted = conn.recv(4096)
            if not encrypted:
                break
            decrypted = decrypt_data(KEY, iv, encrypted)
            tun.write(decrypted)
            logging.info(f"[PACKET IN] From {addr}: {decrypted[:50]}...")
    except Exception as e:
        logging.error(f"Error handling client {addr}: {e}")
    finally:
        conn.close()
        del clients[addr]
        logging.info(f"Client {addr} disconnected.")

def start_server():
    tun = setup_tun_device()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", PORT))
        s.listen(5)
        print(f"[*] Armora™ VPN Server running on port {PORT}...")

        while True:
            conn, addr = s.accept()
            clients[addr] = conn
            threading.Thread(target=handle_client, args=(conn, addr, tun)).start()

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    start_server()
