#!/usr/bin/python3.12
import pyshark

''' simple package analyzer using pyshark module'''
def packet_sniffer(packet):
    if 'IP' in packet:
        source_ip = packet.ip.src
        destination_ip = packet.ip.dst
        protocol = packet.ip.proto

        print(f"Source IP: {source_ip}  Destination IP: {destination_ip}  Protocol: {protocol}")

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
