from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def main():
    print("Starting Packet Sniffer...")
    sniff(prn=packet_callback, count=10)  # Capture 10 packets for demonstration

if __name__ == "__main__":
    main()
