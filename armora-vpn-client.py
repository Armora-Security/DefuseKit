#!/usr/bin/env python3
import socket
import os
import threading
import logging
from pytun import TunTapDevice, IFF_TUN, IFF_TAP, IFF_NO_PI
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Setup logging
logging.basicConfig(
    filename='logs/client.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

SERVER_IP = input("Enter server IP: ")
PORT = 12345
KEY = os.urandom(32)
IV_SIZE = 16

def encrypt_data(key, iv, data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    pad_len = 16 - (len(data) % 16)
    data += b'\x00' * pad_len
    return encryptor.update(data) + encryptor.finalize()

def setup_tun_device():
    tun = TunTapDevice(name="tun0", flags=IFF_TUN | IFF_NO_PI)
    tun.addr = "10.0.0.2"
    tun.netmask = "255.255.255.0"
    tun.up()
    os.system("ip link set tun0 up")
    os.system("ip addr add 10.0.0.2/24 dev tun0")
    os.system("ip route add 10.0.0.0/24 dev tun0")
    return tun

def read_from_tunnel(tun, sock):
    while True:
        packet = tun.read(2048)
        iv = os.urandom(IV_SIZE)
        encrypted = encrypt_data(KEY, iv, packet)
        sock.send(iv + encrypted)
        logging.info(f"[SENT] Encrypted packet to server.")

def start_client():
    tun = setup_tun_device()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((SERVER_IP, PORT))
        client_ip = sock.recv(16).decode()
        print(f"[*] You are assigned IP: {client_ip}")

        threading.Thread(target=read_from_tunnel, args=(tun, sock)).start()

        while True:
            pass  # Keep tunnel open

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    start_client()
