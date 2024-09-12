import pyshark
#Define the path to the pcap file
pcap_file = '/home/analyst/Sample_network_traffic.pcapng'
#Create a packet capture object
cap = pyshark.FileCapture(pcap_file)
#initialize counters
total_packets = 0
source_ips = set()
destination_ips = set()
#Iterate through packets in the pcap file
for packet in cap:
	total_packets += 1
	try:
		source_ip = packet.ip.src
		destination_ip = packet.ip.dst
		source_ips.add(source_ip)
		destination_ips.add(destination_ip)
	except AttributeError:
		# Some packets may not have IP information, so we skip them
		pass
# Print some basic statistics
print(f'Total packets in the capture: {total_packets}')
print(f'Unique source IPs: {len(source_ips)}')
print(f'Unique destination IPs: {len(destination_ips)}')
