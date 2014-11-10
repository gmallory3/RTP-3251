# Test class
# @author aashish9patel
# @version 0.10

from connection import Connection
from packet import Packet

def client():
    clientConn = Connection()
    clientConn.open(12000, '127.0.0.1')
    while 1:
        clientConn.send(raw_input('>>'));

def server():
    serverConn = Connection()
    serverConn.open(12000)
    serverConn.receive()


if __name__ == '__main__':
    print ("main")
    
    inp = int(raw_input('0:Client or 1:server = '))
    if(inp == 0):
        client()
    else:
        server()