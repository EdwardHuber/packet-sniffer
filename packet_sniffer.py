from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("[*] Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)
