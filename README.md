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

# 🎣 Phishing Awareness Training — CodeAlpha Cybersecurity Internship

## 📌 Task 2 — Phishing Awareness Training

A phishing awareness training module created as part of
the CodeAlpha Cybersecurity Internship Program.

---

## 👤 Author

- **Name:** Rajesh Kumar S
- **Internship:** CodeAlpha Cybersecurity Internship
- **Task:** Task 2 — Phishing Awareness Training

---

## 🎯 Objective

- Educate users about phishing attacks and how they work
- Explain how to recognize phishing emails and fake websites
- Explain social engineering tactics used by attackers
- Provide best practices to avoid falling victim to phishing

---

## 📊 Presentation Slides Overview

| Slide | Topic |
|-------|-------|
| Slide 1 | Title — Phishing Awareness Training |
| Slide 2 | What is Phishing? |
| Slide 3 | Types of Phishing |
| Slide 4 | How to Recognize a Phishing Email |
| Slide 5 | Real Example: "Urgent Security Alert" |
| Slide 6 | How to Spot Fake Websites |
| Slide 7 | Social Engineering Tactics |
| Slide 8 | Best Practices to Stay Safe |
| Slide 9 | Key Habits Diagram |
| Slide 10 | Stay Vigilant — Summary |

---

## 🔍 Topics Covered

### What is Phishing?
Phishing is a fraudulent attempt to steal sensitive data by
posing as a trusted entity. Attackers seek usernames,
passwords, financial details, or access tokens. It is often
the first step in larger breaches leading to unauthorized
system access, data loss, and identity theft.

### Types of Phishing
- 📧 **Deceptive Phishing** — mass emails impersonating banks or services
- 🎯 **Spear Phishing** — highly targeted, personalized based on research
- 🐳 **Whaling** — executive-targeted attacks for high-value access
- 📞 **Vishing & Smishing** — voice calls and SMS messages used to deceive

### How to Recognize a Phishing Email
- **The Sender Trap** — domain misspellings, odd subdomains, display-name spoofing
- **Urgent Language** — threats of suspension push victims to act before verifying
- **Suspicious Links & Attachments** — hover to preview URLs, avoid unexpected attachments

### Real World Example — "Urgent Security Alert"
- Mismatched sender and reply-to domains
- Generic greeting and inconsistent branding
- Shortened or obfuscated URL leading to credential-harvesting page
- Outcome: Users led to a cloned login page; harvested credentials
  enabled lateral movement into internal systems

### How to Spot Fake Websites
- Verify the URL and confirm exact domain spelling
- Watch for certificate warnings or expired certs
- Look for inconsistent branding or low-quality images
- Beware of requests for unusual data (PINs, full SSNs)
- Use a second device to verify a suspected site

### Social Engineering Tactics
- 👔 **Authority** — scammers pose as IT, HR, or government officials
- ⏰ **Scarcity & Urgency** — limited-time threats pressure fast action
- 😨 **Emotional Manipulation** — fear, curiosity, or excitement trigger mistakes

### Best Practices to Stay Safe
- ✅ Use Multi-Factor Authentication (MFA) on all critical accounts
- ✅ Verify before you click — hover links and check sender domains
- ✅ Report suspicious activity immediately to IT/security
- ✅ Keep software and browsers updated

### Key Daily Habits
- 🔍 Verify Source
- ⏸️ Pause & Confirm
- 🖱️ Think Before Click
- 🔐 Use MFA

---

## 📁 Project Structure
