# Name - Sidharth Raj
# importing all the necessary libraries
# socket library is used to create and handle various sockets
# Threading library is used to create threads which help in multithreading
import socket, threading
import json
import time
import sys
import datetime
from easygui import *



# A class is created for clients so that easch thread will be its object and have the same particular mechanism as other threads
class ClientThread(threading.Thread):

    # This is the constructor which assigns the ip address, port number and socket to each client
    def __init__(self, clientaddress, clientsocket):
        threading.Thread.__init__(self)
        # Creaing a socket
        self.csocket = clientsocket
        print("New connection added: ", clientaddress)

    # def message(self):
    #     x = datetime.datetime.now()
    #     c_t = "TEXT/JSON"
    #     content = json.dumps({"host": '127.0.0.1', "date": x, "content_type": c_t, })
    #     self.csocket.send(content.encode())

    # This is the code which will run from the server side for each and every client
    def run(self):

        # Collect data from JSON object and deserialize it.
        data = self.csocket.recv(2048)
        data = json.loads(data.decode())

        # Deserializing the JSON object
        name12 = data.get('name12')
        time12 = data.get('samay')

        # Printing username and wait interval
        print("Client name: ", name12)
        print("Wait interval: ", time12)
        # msgbox("Connected to Client: " , "Server: Active Client")
        # Putting the client thread to sleep for the given time interval
        time.sleep(time12)
        print("\nServer waited for: {} seconds for client: {}".format(time12, name12))
        # self.message()



        # if choice == 'disconnect'
        # self.csocket.close()





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
while True:
    # 3 specifies that server will wait for 3 connections if it busy and the 4th connection will be refused
    server.listen(3)
    # This line will accept a particuar incoming request and save the address and port number of that client from which the request is coming from
    clientsock, clientAddress = server.accept()
    # A new thread is created for each and every client request which is accepted that too on the exact same address and port number
    newthread = ClientThread(clientAddress, clientsock)
    # start() method starts the client thread and calls the run method of that thread
    newthread.start()


s.close()