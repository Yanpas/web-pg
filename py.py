#!/usr/bin/python3

import socket
import selectors

sel = selectors.DefaultSelector()
serv_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)

def handle():
	cli, addr = serv_sock.accept()
	def clihandle():
		data = cli.recv(1024)
		if data == b'close':
			serv_sock.close()
			exit(0)
		cli.send(data)
		cli.close()
	sel.register(cli, selectors.EVENT_READ, clihandle)



serv_sock.bind(('0.0.0.0', 2222))
serv_sock.listen(1)

sel.register(serv_sock, selectors.EVENT_READ, handle)
while True:
	for res, n in sel.select():
		res.data()
