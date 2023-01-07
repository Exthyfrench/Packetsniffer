# Packetsniffer
This script creates a raw socket and sets it to promiscuous mode, which allows it to receive all packets on the network. It then receives packets indefinitely and unpacks the packet headers to extract the source and destination IP addresses. Finally, it prints the packet header information.

Keep in mind that you may need to run this script with root privileges, as raw sockets require special privileges to be used.

To use this script, save it to a file (e.g. packet_sniffer.py) and run it using Python:

sudo python packetSniffer.py
