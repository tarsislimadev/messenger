import threading
import socket
import config
import actions

from libs.http.request import Request
from libs.http.response import Response

def listen() -> None:
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((config.address, int(config.port)))
  server.listen()

  while True:
    client, _ = server.accept()
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

def handle(client: socket) -> None:
  request = Request(client)
  client.send(run(request).__str__())
  client.close()

def run(request: Request = Request(None)) -> Response:
  response = Response(request)

  match request.getPath():
    case 'message':
      return actions.message(request, response)

  return response
