#!/usr/bin/python3
# coding:utf-8

'stepik example'

bind = "0.0.0.0:8080"

def worker(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	for item in environ['QUERY_STRING'].split('&'):
		yield item.encode() + b'\n'
		#d = item.split('=')
		#yield "{}:{}".format(d[0], d[1])

