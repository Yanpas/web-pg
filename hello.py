#!/usr/bin/python3
# coding:utf-8

'stepik example'

bind = "127.0.0.1:8000"

def worker(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    for item in environ['QUERY_STRING'].split('&'):
		yield item + '\n'
		#d = item.split('=')
		#yield "{}:{}".format(d[0], d[1])

