#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:

			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break

			user = getUser(line)
			message = getMessage(line)
			message = message.lower()
			print user + " typed :" + message
			
			if message != "":
				if "cabron" in message:
					sendMessage(s, "Cuida tu vocabulario, @" + user)
					