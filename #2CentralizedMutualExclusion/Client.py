# Name - Sidharth Raj#####
# Student Id - 1001548027#
# LAB - 2 CLIENT  ########
##########################
# importing all the necessary libraries
# socket library is used to create and handle various sockets
# easygui library is used to create gui
import socket
import random
import json
from easygui import *
from tkinter import *
from time import gmtime, strftime
import time
import timeit
import datetime

request = 'GET / HTTP/1.1\r\nHost: LOCALHOST\r\n\r\n'


# Client function to send the encoded JSON object to the server
def client(info):
    s.send(info.encode())
    print("Data sent")


# Function to generate random integer between 5 and 15
def randtime():
    number = random.randint(3, 10)
    return number


# specifying the host as localhost so that the server and clients both connect to the same node
host = ''
port = 8888

# A socket is created where the first argument refers to the IPV4 addressing
# scheme and the second argument refers to the TCP protocol.
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Fail to connect\n")

print("Socket Created\n")
# Connect the socket to the LocalHost
s.connect((host, port))
# Pop-up dialog box for user to enter the username
c_name = enterbox(msg="Please enter username: ", title="Enter User Name", default="")

choice = "Wait request"
while choice != "Disconnect":
    # c_name = raw_input("Enter Username for the client: ")
    number = randtime()
    # Dumping JSON object into DATA container
    data = json.dumps({"name12": c_name, "samay": number, "khat": request})
    print("Username and wait interval value collected")
    # Calling function CLIENT()
    client(data)
    # Message sent timestamp
    t1 = time.time()
    # Receiving the HTTP message
    result = s.recv(2048)
    # HTTP message receive timestamp
    t2 = time.time()
    result = result.decode('UTF-8')
    intezaar = t2 - t1
    # Printing the HTTP message to the client and asking for next step
    choice = buttonbox(result, "Client: {} || Time spent waiting : {}".format(c_name, round(intezaar)), ["Wait request", "Disconnect"], None, None)

s.close()
