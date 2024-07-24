# Network Packet Analyzer
This repository contains a Network Packet Analyzer tool implemented in Python. The tool is designed to capture, analyze, and display network packets, providing insights into network traffic and protocols. It is a useful tool for network administrators, security professionals, and enthusiasts who want to understand and monitor network activity.

# Features
-->Packet Capture: Uses Python libraries to capture network packets in real-time from a specified network interface.


-->Packet Analysis: Parses and decodes packet data to extract useful information such as source and destination IP addresses, port numbers, and protocol types.


-->Detailed Reporting: Provides detailed output of the packet information, including headers and payload, to help diagnose network issues and analyze traffic patterns.


-->Protocol Support: Supports common network protocols including TCP, UDP, and ICMP, with the ability to expand to other protocols.

#  Usage

Install Dependencies: Ensure you have the necessary Python libraries installed. You can use pip to install them.

pip install scapy
Run the Analyzer: Execute the script to start capturing and analyzing packets.

python network_packet_analyzer.py
View Results: The tool will display captured packet information in the console.

Example Output
yaml
Copy code
Packet 1:
Source IP: 192.168.1.1
Destination IP: 192.168.1.2
Protocol: TCP
Source Port: 80
Destination Port: 443
Payload: [Data Content]

Packet 2:
Source IP: 192.168.1.2
Destination IP: 192.168.1.1
Protocol: UDP
Source Port: 12345
Destination Port: 80
Payload: [Data Content]
Installation
To get started, clone the repository and install the required dependencies:

git clone https://github.com/raghavmishra1//network-packet-analyzer.git
cd network-packet-analyzer
pip install -r requirements.txt

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

