import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
x = str(input())
clientsocket.send(bytes(x, 'UTF-8'))
