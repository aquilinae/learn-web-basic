# [STEPIK]
# Web-технологии https://stepik.org/course/154
# 1.6 Сетевые протоколы (7)

'''
Измените ваш echo сервер так, что бы он работать одновременно с 10 клиентами. 

Протокол передачи такой же как в прошлой задаче.
'''

import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

pid = os.fork()

if pid == 0:
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		conn.send(data)		
		conn.close()