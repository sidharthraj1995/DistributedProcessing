# Name - Sidharth Raj#####
# Student Id - 1001548027#
##########################
# importing all the necessary libraries
# socket library is used to create and handle various sockets
# easygui library is used to create gui
import socket
import random
import json
from easygui import *



request = "GET / HTTP/1.1\r\nHost: \r\n\r\n"

# Client function to send the encoded JSON object to the server
def client(info):
    s.send(info.encode())
    print("Data sent")

# Function to generate random integer between 5 and 15
def randtime():
    number = random.randint(5, 15)
    return number


# specifying the host as localhost so that the server and clients both connect to the same node
host = ''
port = 8888

# A socket is created where the first argument refers to the IPV4 addressing scheme and the second argument refers to the TCP protocol
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Fail to connect\n")


print("Socket Created\n")
# Connect the socket to the LocalHost
s.connect((host, port))
# Pop-up dialog box for user to enter the username
c_name = enterbox(msg="Please enter username: ", title= "Enter User Name", default= "")
# c_name = raw_input("Enter Username for the client: ")
number = randtime()
# Dumping JSON object into DATA container
data = json.dumps({"name12": c_name, "samay": number})
print("Username and wait interval value collected")

# Calling function CLIENT()
client(data)

choice = buttonbox('Choose an option:', "Client", ["Wait request", "Disconnect"], None, None, "Disconnect")

# if choice == 'Disconnect':
#     break



s.close()