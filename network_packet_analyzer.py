from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def ethical_use_reminder():
    print("Ensure you have permission to capture and analyze network packets.")
    print("This tool is intended for educational purposes only.")

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        if TCP in packet:
            payload = packet[TCP].payload
        elif UDP in packet:
            payload = packet[UDP].payload
        else:
            payload = None

        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {proto}")
        print(f"Payload: {payload}")

ethical_use_reminder()
sniff(prn=packet_callback, count=10)
