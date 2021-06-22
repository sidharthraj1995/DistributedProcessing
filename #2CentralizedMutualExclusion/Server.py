# Name - Sidharth Raj######
# importing all the necessary libraries
# socket library is used to create and handle various sockets
# Threading library is used to create threads which help in multi-threading
import json
import socket
import sys
import threading
import time
from time import gmtime, strftime
from urllib.parse import urlparse
from easygui import *
import os

# get the middle string, actually the URL
def getMidStr(d, startStr, endStr):
    startIndex = d.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
        endIndex = d.index(endStr)
        return d[startIndex:endIndex]


# return the response of the GET request
# param:
#   getRequestPath: URL of client request
def responseGetRequest(getRequestPath):
    o = urlparse(getRequestPath)
    msgSendtoClient = "HTTP/1.1 200 OK\n"
    # Date and time
    t = strftime("%a, %d %b %Y %H:%M:%S %Z", gmtime())
    msgSendtoClient += "Data: " + t + "\n"
    # Server
    msgSendtoClient += "Server: " + "CSE5306_server" + "\n"
    # Content type
    msgSendtoClient += "Content Type: JSON/HTML" + "\n"
    # User agent
    msgSendtoClient += "User agent: Pycharm/Python" + "\n"

    # content length
    msgSendtoClient += "Content-Length:" + str(len(o)) + "\n"
    msgSendtoClient += "\r\n\r\n"

    return msgSendtoClient


# A class is created for clients so that easch thread will be its object and have the same particular mechanism as other threads
class ClientThread(threading.Thread):

    # This is the constructor which assigns the ip address, port number and socket to each client
    def __init__(self, clientaddress, clientsocket):
        threading.Thread.__init__(self)
        # Creaing a socket
        self.csocket = clientsocket
        print("New connection added: ", clientaddress)


    # This is the code which will run from the server side for each and every client
    def run(self):
        while True:
            # Collect data from JSON object and deserialize it.
            data = self.csocket.recv(2048)
            if not data:
                break

            data = json.loads(data.decode())
            # Deserializing the JSON object
            name12 = data.get('name12')
            time12 = data.get('samay')
            khat12 = data.get('khat')
            # msgbox("Waiting for Client {} for {} seconds".format(name12, time12), title="Server/CurrentClient")
            ThreadLock.acquire()
            # Printing username and wait interval
            print("\nClient name: ", name12)
            print("Wait interval: ", time12)

            # Putting the client thread to sleep for the given time interval
            time.sleep(time12)
            message12 = responseGetRequest(getMidStr(khat12, 'GET ', 'HTTP/1.1'))
            message12 = message12.encode('utf-8', 'strict')
            self.csocket.send(message12)
            print("\nServer waited for: {} seconds for client: {}\n\n".format(time12, name12))
            ThreadLock.release()


# defining the Host name and port number for the client to connect
LOCALHOST = ''
PORT = 8888
# A socket is created where the first argument refers to the IPV4 addressing scheme and the second argument refers to the TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This line makes sure that sockets do not use the same port number again
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# This binds the server to the given host address and port number so that it can listen to incoming requests
try:
    server.bind((LOCALHOST, PORT))
except socket.error:
    print("Bind fail!")
    sys.exit()

print("Server started")
print("Listening for clients...")
# 3 specifies that server will wait for 3 connections if it busy
# and the 4th connection will be refused
server.listen(3)
client_count = 0
clients = []

ThreadLock = threading.Lock()

while True:
    # This line will accept a particuar incoming request and save the
    # address and port number of that client from which the request is coming from
    clientsock, clientAddress = server.accept()
    # Add clients to the connection list
    clients.append(clientsock)
    # A new thread is created for each and every client request which is accepted
    # that too on the exact same address and port number
    newthread = ClientThread(clientAddress, clientsock)
    client_count += 1
    # start() method starts the client thread and calls the run method of that thread
    newthread.start()
    msgbox("Connected to {} clients" .format(client_count))


s.close()



