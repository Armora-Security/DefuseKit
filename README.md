# DefuseKit
VPN Server by Armora Security

# 🔒 ArmoraVPN™ – Python-based Custom Tunneling Framework

## Features
- Full network tunneling using TUN devices
- AES-256 encryption for secure communication
- Multi-client support
- Activity logging
- Simple chat GUI
- Auto-disconnect timeout (to be added)

## Requirements
```bash
pip install pytun cryptography tk

Usage

Run Server

```bash



sudo python3 armora-vpn-server.py
 Run Client

bash


1
sudo python3 armora-vpn-client.py
 Run Chat GUI

bash


1
python3 gui/client_gui.py
 Note: Requires root access due to TUN device usage. 
