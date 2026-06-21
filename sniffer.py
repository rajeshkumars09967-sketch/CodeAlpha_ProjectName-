# ============================================
# CodeAlpha Internship - Task 1
# Basic Network Sniffer
# Author: Your Name
# ============================================

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

# Counter to track packets
packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1

    timestamp = datetime.now().strftime("%H:%M:%S")

    # Only process packets with IP layer
    if IP in packet:
        src_ip  = packet[IP].src
        dst_ip  = packet[IP].dst
        ttl     = packet[IP].ttl

        # --- Identify Protocol ---
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            flags    = packet[TCP].flags
            print(f"\n[{timestamp}] Packet #{packet_count}")
            print(f"  Protocol : {protocol}")
            print(f"  Source   : {src_ip}:{src_port}")
            print(f"  Dest     : {dst_ip}:{dst_port}")
            print(f"  TTL      : {ttl}")
            print(f"  Flags    : {flags}")

        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"\n[{timestamp}] Packet #{packet_count}")
            print(f"  Protocol : {protocol}")
            print(f"  Source   : {src_ip}:{src_port}")
            print(f"  Dest     : {dst_ip}:{dst_port}")
            print(f"  TTL      : {ttl}")

        elif ICMP in packet:
            protocol = "ICMP"
            print(f"\n[{timestamp}] Packet #{packet_count}")
            print(f"  Protocol : {protocol} (Ping)")
            print(f"  Source   : {src_ip}")
            print(f"  Dest     : {dst_ip}")
            print(f"  TTL      : {ttl}")

        else:
            print(f"\n[{timestamp}] Packet #{packet_count}")
            print(f"  Protocol : OTHER")
            print(f"  Source   : {src_ip}")
            print(f"  Dest     : {dst_ip}")

        # --- Show Payload if exists ---
        if Raw in packet:
            payload = packet[Raw].load[:80]  # First 80 bytes only
            print(f"  Payload  : {payload}")

        print("-" * 55)


# ============================================
# MAIN — Start Sniffing
# ============================================
print("=" * 55)
print("   CodeAlpha — Basic Network Sniffer")
print("   Capturing 50 packets... Please wait")
print("   Press Ctrl+C to stop early")
print("=" * 55)

sniff(
    prn=analyze_packet,   # function to call for each packet
    store=False,          # don't store in memory
    count=50              # capture 50 packets then stop
)

print(f"\n✅ Done! Total packets captured: {packet_count}")