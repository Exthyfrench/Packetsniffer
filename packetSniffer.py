import socket
import struct

# Create a raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# Set the socket to promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# Receive packets indefinitely
while True:
  # Receive a packet
  packet = s.recv(65565)
  
  # Unpack the packet header
  ip_header = packet[:20]
  ip_header = struct.unpack("!BBHHHBBH4s4s", ip_header)
  
  # Get the source and destination IP addresses
  source_ip = socket.inet_ntoa(ip_header[8])
  dest_ip = socket.inet_ntoa(ip_header[9])
  
  # Print the packet header
  print(f"Source IP: {source_ip} Destination IP: {dest_ip}")

# Disable promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
