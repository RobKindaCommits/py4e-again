'''
Created on Feb 4, 2024

@author: rob.fenoglio
'''
'''
# make a socket connection
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
'''

'''
# following along
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(1024)
    #if you set the data length to 512 bits, it cuts off the 4th line
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
'''

