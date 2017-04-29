#!/usr/bin/python3

import socket
import selectors

serv_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)

def handle():
	cli, addr = serv_sock.accept()
	data = cli.recv(1024)
	if data == b'close':
		serv_sock.close()
		exit(0)
	cli.send(data)
	cli.close()


serv_sock.bind(('0.0.0.0', 2222))
serv_sock.listen()
sel = selectors.DefaultSelector()
sel.register(serv_sock, selectors.EVENT_READ, handle)
while True:
	for res, n in sel.select():
		res.data()
