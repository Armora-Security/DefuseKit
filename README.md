# DefuseKit: ArmoraVPN™ – Custom Tunneling Framework (Proprietary)

---

## 🔒 ArmoraVPN™ – Securing Your Network with Experimental Technology

Welcome to **DefuseKit**, home of **ArmoraVPN™** – a custom tunneling framework built with a philosophy of "security through obscurity" and hardcore performance. ArmoraVPN™ isn't just another VPN; it's an ambitious experiment in creating secure, flexible network tunnels supported by unique functionalities, giving you complete control over your privacy and connection.

Developed by **Armora Security**, this project represents our endeavor to craft a VPN solution that goes beyond merely securing data—it redefines how you interact with networks, focusing on robust encryption and adaptive capabilities.

---

## 🔥 ArmoraVPN™'s "Crazy Cool" Features

ArmoraVPN™ comes with a set of powerful core features, alongside planned developments that will truly make it "crazy":

* **Full Network Tunneling using TUN Devices (Kernel-Level Integration):**
    This is at the heart of ArmoraVPN™'s ingenuity. By leveraging **TUN devices** at the operating system's kernel level, ArmoraVPN™ can create a virtual network interface that captures and routes **all your network traffic**.
    This means not just your browser or specific applications, but **every piece of network activity** from your device will traverse this secure tunnel, providing comprehensive privacy and security coverage at the OS level. It offers superior isolation and prevents traffic leaks outside the tunnel.

* **AES-256 Encryption for Secure Communication (Military-Grade Standard):**
    Security is our paramount concern. All data passing through the ArmoraVPN™ tunnel is encrypted using the **AES-256** standard. This is a military-grade encryption algorithm renowned for its robust security, ensuring the confidentiality and integrity of your data against eavesdropping or unauthorized modification. Every data packet is protected from end-to-end.

* **Multi-Client Support (Experimental Scalability):**
    The ArmoraVPN™ server is designed to support **multiple concurrent clients**. This allows a single server instance to serve various devices or users, laying the groundwork for deployments in broader environments. It's ideal for experimenting with different client configurations or providing encrypted access for a small group of users.

* **Activity Logging (Transparency & Debugging):**
    ArmoraVPN™ servers come equipped with **activity logging capabilities**. Every connection, data transfer, and significant event will be recorded. This is crucial for **debugging**, monitoring server health, identifying potential anomalies, and providing basic transparency regarding VPN usage.

* **Simple Chat GUI (Internal Encrypted Communication):**
    Uniquely, ArmoraVPN™ includes a **simple chat GUI**. This isn't for general communication, but rather an **internal encrypted chat channel** between clients and the server, or among clients connected to the same server. This functionality can be used for system notifications, internal coordination, or even simple command-and-control within a secure experimental environment.

* **Auto-Disconnect Timeout (To Be Added - Upcoming Security Feature):**
    As part of continuous development, an **auto-disconnect timeout** feature will be added. This will automatically terminate client connections after a period of inactivity. This is vital for security, preventing unattended sessions from remaining open and reducing potential risks if a client device is inactive or lost.

### 🚀 Planned "Insane" Features for the Future

We're not stopping here. ArmoraVPN™ will continue to evolve with even more groundbreaking features:

* **Dynamic Port Hopping & Obfuscation:** Dynamically changing communication ports and disguising VPN traffic to appear as regular web traffic (e.g., HTTPS), to evade detection and blocking by advanced firewalls.
* **Stealth Mode / Traffic Cloaking:** Advanced techniques to make VPN traffic indistinguishable from other normal internet traffic, enhancing resilience against DPI (Deep Packet Inspection).
* **Basic Firewall Integration (Server-Side):** Fundamental integration with the OS firewall (e.g., `iptables` on Linux) on the server side to secure the VPN endpoint itself and control inbound/outbound traffic.
* **Multi-Server Load Balancing:** The capability to distribute client load across multiple VPN servers, boosting scalability and uptime.
* **Enhanced User Management:** A more sophisticated user management system to handle credentials, permissions, and usage statistics for each client individually.
* **Cross-Platform Clients:** Development of clients for platforms beyond Python, such as Android, iOS, Windows, or macOS, for wider and easier access.
* **One-Time Pad (OTP) Key Exchange (Experimental):** Exploration of more advanced key exchange methods, such as OTP, for theoretically perfect security (with significant implementation challenges).

---

## 🛠️ "Hardcore" System Requirements

To run this "crazy" ArmoraVPN™, you'll need the right environment:

* **Python 3.x:** Python version 3.6 or higher is highly recommended.
* **Operating System:** **Linux (Ubuntu/Debian/CentOS)** is the recommended platform due to optimal **TUN device** utilization and the required root access. Compatibility with other OS (macOS, Windows) is very limited or requires complex configurations for TUN devices.
* **Root / Sudo Access:** Running both the server and client **requires root access (`sudo`)** due to low-level operations on TUN devices. Ensure you understand the security implications of executing scripts with elevated privileges.

### Python Dependencies:

Ensure you have all necessary Python libraries. We **highly recommend** using a **virtual environment** to manage dependencies.

* `pytun`: A Python library for interacting with TUN/TAP devices. This is core to our tunneling capabilities.
* `cryptography`: A robust Python cryptography library, used for the secure AES-256 encryption implementation.
* `tk`: Python's standard library for creating simple Graphical User Interfaces (GUI), utilized for the chat GUI.

---

## 🚀 Installation & "Launch" Preparation

Follow these steps to set up ArmoraVPN™:

### 1. Clone the "DefuseKit" Repository

Start by cloning the entire DefuseKit project from GitHub:

```bash
git clone https://github.com/Armora-Security/DefuseKit.git
cd DefuseKit
```

### 2. Set Up a Virtual Environment (Highly Recommended!)

It's crucial to isolate this project's dependencies from your system's Python installation:

```bash
python3 -m venv venv
source venv/bin/activate
```

*(To exit the virtual environment, type `deactivate`)*

### 3. Install Python Dependencies

After activating your virtual environment, install all required libraries:

```bash
pip install pytun cryptography tk
```

---

## 🎯 ArmoraVPN™ "Mission" Usage

ArmoraVPN™ is divided into server and client components. Ensure you run each part on the appropriate machine.

### 1. Running the ArmoraVPN™ Server

The server should be run on the machine that will act as your VPN exit node (e.g., a VPS or a machine with a public IP).

**Important:** Ensure the port used by the server is not blocked by your external firewall or router.

```bash
sudo python3 armora-vpn-server.py
```

*Once executed, the server will await connections from clients.*

### 2. Running the ArmoraVPN™ Client

The client should be run on the device whose traffic you wish to secure.

```bash
sudo python3 armora-vpn-client.py
```

*The client will attempt to connect to the VPN server. Ensure you have correctly configured the server's IP in the client code (if no dynamic configuration is present).*

### 3. Running the Chat GUI (Optional)

The simple chat GUI can be run separately from the main client. It enables basic chat interaction within the VPN tunnel.

```bash
python3 gui/client_gui.py
```

*Note: This GUI requires a desktop environment with Tkinter support.*

---

## ⚙️ Configuration (Initial Setup)

For now, configurations (such as server IP, port, and encryption keys) might need to be adjusted directly within the `armora-vpn-server.py` and `armora-vpn-client.py` files.

* **Server Address:** Ensure `armora-vpn-client.py` is configured with the public IP address or domain name of your `armora-vpn-server.py`.
* **Port:** Ensure the port used by both the server and client matches.
* **Encryption Keys:** The AES-256 key used **must be identical** on the server and all clients to ensure successful encrypted communication. **DO NOT use default keys for any serious deployment.**

---

## ⚠️ Security Warnings & Limitations (Extremely Important!)

* **Experimental Project:** ArmoraVPN™ is an experimental framework and is **NOT recommended for production use** requiring critical security or high reliability. It is a tool for learning and exploration.
* **Root Access:** Executing these scripts with `sudo` grants full root access to your system. Understand every line of code before running it.
* **Security Audit:** The code has not been professionally audited for all potential vulnerabilities.
* **Proprietary:** Again, remember that this is a proprietary project. Any use, modification, or distribution beyond personal review/experimentation requires explicit permission.

---

## 🤝 Contributions & Future Development

We welcome contributions and ideas that can make ArmoraVPN™ even more "crazy" and innovative. If you have suggestions or wish to contribute to future features, please reach out to the Armora Security team.

---

**Armora Security**
*Beyond the Boundaries of Security.*
