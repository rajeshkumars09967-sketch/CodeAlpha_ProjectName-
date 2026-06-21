# 🔍 Basic Network Sniffer — CodeAlpha Cybersecurity Internship

## 📌 Task 1 — Network Sniffer

A Python-based network packet sniffer built as part of the
CodeAlpha Cybersecurity Internship Program.

---

## 🎯 Objective

- Capture live network traffic packets
- Analyze packet structure and content
- Understand how data flows through a network
- Learn basics of TCP, UDP, and ICMP protocols

---

## 🛠️ Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Programming Language |
| Scapy | Packet Capturing Library |
| Npcap | Windows Packet Capture Driver |
| VS Code | Code Editor |

---

## ⚙️ Features

- ✅ Captures live network packets in real time
- ✅ Detects TCP, UDP, ICMP protocols
- ✅ Displays Source & Destination IP addresses
- ✅ Shows Source & Destination Port numbers
- ✅ Displays TTL (Time To Live) values
- ✅ Shows packet payload (first 80 bytes)
- ✅ Timestamps every captured packet
- ✅ Packet counter

---

## 📋 Requirements

- Python 3.10 or higher
- Scapy library
- Npcap (Windows only)
- Administrator/Root privileges

---

## 🚀 Installation & Setup

### Step 1 — Install Python
Download from: https://python.org/downloads

### Step 2 — Install Scapy
```bash
pip install scapy
```

### Step 3 — Install Npcap (Windows Only)
Download from: https://npcap.com
- During install check "WinPcap API-compatible Mode"

### Step 4 — Run the Sniffer
```bash
# Windows (Run CMD as Administrator)
python sniffer.py

# Linux / Mac
sudo python3 sniffer.py
```

---

## 📊 Sample Output
