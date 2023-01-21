import threading
import socket
import config

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((config.address, config.port))
server.listen()

def handle(client):
  print(client.recv(1024).decode('ascii'))

  client.send('HTTP/1.1 200 OK')
  client.close()

def receive():
  while True:
    client, _ = server.accept()
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

receive()
