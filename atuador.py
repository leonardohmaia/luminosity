import socket
from time import sleep


# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8180))

while True:
    client.send('Assinar luminosidade'.encode())
    message = client.recv(1024).decode()
    print(f'message: {message}')
    luminosidade = int(message)
    if luminosidade > 60:
        print('Abrindo as cortina')
    else:
        print('Fechando as cortina')
        sleep(10)
   
