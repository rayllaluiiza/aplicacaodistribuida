import socket
import threading

PORT = 5000
ADDRESS_CLIENT = "10.90.37.15"
ADDRESS_MID = "10.90.37.16"
ADDRESS_SEVERNAME1 = "10.90.37.17"
ADDRESS_SEVERNAME2 = "10.90.37.19"
ADRESS_SERVER = "10.90.37.18"

MIDD_ADDRESS = "127.0.0.1"
MIDD_PORT = 5000
CLIENT_PORT = 5001
CLIENT_ADRESS = "127.0.0.1"
SERVERNAME1_PORT = 5002
SERVERNAME2_PORT = 5003
SERVER_ADRESS = "127.0.0.1"
SERVER_PORT = 5004

class ServerName1():

	def __init__(self):
		#self.retornaServer(MIDD_ADDRESS, SERVERNAME1_PORT)
		self.retornaServer(ADDRESS_SEVERNAME1, PORT)

	def retornaServer(self, client, port):
		#endereco = '5004' + ' ' #quando testar no if mudar o address
		endereco = '10.90.37.18' + ' ' +'127.0.0.1'
		
		udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		address = (client, port)
		udp_socket.bind((address))
		
		while True:
			msg, cli = udp_socket.recvfrom(1024)

			if msg == 'Soma':
				print 'teste'
				
				udp_socket.sendto(endereco, cli)

			elif msg == 'Subtracao':
				print 'teste 2'
				
				udp_socket.sendto(endereco, cli)

			elif msg == 'Multiplicacao':
				print 'teste 3'
				
				udp_socket.sendto(endereco, cli)

		udp_socket.close()


if __name__ == "__main__":
	servername1 = ServerName1()
		
