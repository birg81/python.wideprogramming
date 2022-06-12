import socket

HOST = '127.0.0.1'
PORT = 12345
MSG = b'Un wisky maschio senza rischio'


# UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(MSG, (HOST, PORT))

print (f'''{HOST}:{PORT} >> send "{MSG}"..''')
