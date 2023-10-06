import socket
import threading

dados = {
	'Luminosidade': 0
}
# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8180))
server.listen(5)

def server_inst():
	while True:
		client, address = server.accept()
		threading.Thread(target=response_manager,args=(client,)).start()

def response_manager(client):
	while True:
		message = client.recv(1024).decode()
		if message.startswith('Publicar luminosidade'):
			print(message)
			dados['Luminosidade'] = int(message.split(' ')[2])
		elif message == 'Assinar luminosidade':
			client.send(str(dados['Luminosidade']).encode())
server_inst()
