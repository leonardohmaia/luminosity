import socket
import random
from time import sleep


# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8180))

while True:
    mensagem = 'Publicar luminosidade ' + str(random.randint(0, 100))
    client.send(mensagem.encode())
    
    sleep(5)
   
