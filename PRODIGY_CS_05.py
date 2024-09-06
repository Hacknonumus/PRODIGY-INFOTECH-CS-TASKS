#!/usr/bin/python3.12
import pyshark

''' Packet analyzer using pyshark module'''
def packet_sniffer(packet):
    if 'IP' in packet:
        source_ip = packet.ip.src
        destination_ip = packet.ip.dst
        protocol = packet.transport_layer if hasattr(packet, 'transport_layer') else 'Unknown'
        print(f"Source IP: {source_ip}  Destination IP: {destination_ip}  Protocol: {protocol}")

        # Check if the packet is ICMP
        if 'ICMP' in packet:
            icmp_type = packet.icmp.type
            icmp_code = packet.icmp.code
            print(f"ICMP Packet: Type={icmp_type}, Code={icmp_code}")

        # Additional analysis for suspicious patterns (malicious behavior)
        if int(packet.ip.ttl) < 64:  # Example: Detecting low TTL values (could be a sign of network scanning)
            print(f"Suspicious Packet: Low TTL detected from {source_ip} (TTL={packet.ip.ttl})")

        # Check for large data packets (potentially malicious)
        if hasattr(packet, 'length') and int(packet.length) > 1500:
            print(f"Warning: Large packet detected from {source_ip} (Length={packet.length})")

        # Raw payload analysis
        if hasattr(packet, 'raw'):
            payload = packet.raw
            print(f"Payload: {payload}")

def main(interface):
    capture = pyshark.LiveCapture(interface=interface)
    for packet in capture.sniff_continuously(packet_count=10):  # Adjust packet_count as needed
        packet_sniffer(packet)

if __name__ == "__main__":
    interface = input("Enter the interface to sniff (e.g., eth0): ")
    main(interface)
