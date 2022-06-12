import socket

HOST = '127.0.0.1'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

s.bind((HOST, PORT))
print (f'''UDP Server Llistening on {HOST}:{PORT}..''')

while True:
	msg, addr = s.recvfrom(1024) # buffer size is 1024 bytes
	print (f'''{addr[0]}:{addr[1]}>> "{msg}"...''')
	
