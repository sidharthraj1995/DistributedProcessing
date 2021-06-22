import socket
import threading
from collections import deque
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, ttk
import requests
# from sympy import *

# GUI
# setting of window's title
top = tkinter.Tk()
top.title("Server Control Panel")
top.geometry("720x300")

arr_flag = []
reply_str = ''
whole = []

# Poll Button Click Handler
def onBtnPoll():
    global reply_str
    calc_val.set(initial_val.get())
    calc_rest_val.set(initial_val.get())
    reply_str = initial_val.get()
    # Set all Clients Flag Value to Poll State

    for i in range(0, len(arr_flag)):
        arr_flag[i] = 1

        
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.number_q = []
        self.arr_clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        # Open Listen Thread
        threading.Thread(target = self.listenInterface,args = ()).start()
    
    def listenInterface(self):
        # Listen to New Clients
        self.sock.listen(3)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()        

    def listenToClient(self, client, address):
        global reply_str
        size = 1024 
        # Receive Clients Name
        client_val = client.recv(size)  
        client_name = str(client_val).replace("'", "")[1:]
        print("Connected to client: {}\n".format(client_name))
        flg = 0
    
        myclient_id = len(arr_flag)
        
        self.arr_clients.append(client_name)
        arr_flag.append(False)
        # Update Client Names
        client_arr_str = ''
        for i in self.arr_clients:
            client_arr_str = client_arr_str + i + '\n'
            
        conn_cli_val.set(client_arr_str)
        while True:
            try:
                # Poll State.
                if arr_flag[myclient_id] == 1:
                    arr_flag[myclient_id] = 0
                    # Send 'polled' to Get Client Value.
                    client.send('polled'.encode(encoding="utf-8"))
                    data = client.recv(size)
                    # data = data.decode("UTF-8")
                    calc_rec_str = str(data, "UTF-8")
                    # calc_rec_str = str(data)
                    # calc_rec_str = calc_rec_str.replace("'", "")[2:]
                    reply_str = reply_str + calc_rec_str


                    finish_flag = True
                    for i in range(0, len(arr_flag)):
                        if arr_flag[i]:
                            finish_flag = False
                    # If all clients are polled.
                    if finish_flag:
                        calc_val.set(reply_str)
                        # calc_rest_val.set(str(round(eval(reply_str[1:]), 4)))
                        calc_rest_val.set(round(eval(reply_str), 4))
                        # calc_rest_val.set(round(reply_str.evalf, 4))
                        initial_val.set(round(eval(reply_str), 4))
                        # Set all Clients Flag to Update Value.
                        for i in range(0, len(arr_flag)):
                            arr_flag[i] = 2 
                # Send Updated Value to Client.
                elif arr_flag[myclient_id] == 2:
                    arr_flag[myclient_id] = 0
                    client.send(calc_rest_val.get().encode(encoding="utf-8"))                                
            except:
                client.close()
                #if (len(self.arr_clients) > 0):
                #    self.arr_clients.remove(client_name)
                return False


initial_val = tkinter.StringVar()
initial_val.set('1')

calc_val = tkinter.StringVar() 
calc_rest_val = tkinter.StringVar()

initial_str_label = Label(text="Initial Value : ")
initial_str_label.grid(row=6, column=8, sticky = W + E)

initial_value_label = Label(text="", textvariable=initial_val)
initial_value_label.grid(row=6, column=10, sticky = W + E)

# Poll Button
poll_button = Button(top, text="Poll", command=onBtnPoll)
poll_button.grid(row=200, column=9, sticky=W+E)

# Calculator String
calc_str_label = Label(text="Expression : ")
calc_str_label.grid(row=3, column=8, sticky=W+E)

calc_str_text = Label(text="", textvariable=calc_val)
calc_str_text.grid(row=3, column=10, sticky=W+E)
calc_str_text.focus_set()

calc_res_str_label = Label(text="Result: ")
calc_res_str_label.grid(row=4, column=8, sticky = W + E)

calc_res_value_label = Label(text="", textvariable=calc_rest_val)
calc_res_value_label.grid(row=4, column=10, sticky = W + E)


# Server Menu
cate_label = Label(text="Server")
cate_label.grid(row=1, column=9, sticky=E)
cate_label.config(font=("", 40))

# Generated number label
num_label = Label(text="Active connections: ")
num_label.grid(row=80, column=1, sticky=W+E)


num_val = tkinter.StringVar()
conn_cli_val = tkinter.StringVar()
calc_res_val = tkinter.StringVar()

num_val_label = Label(text="", textvariable=num_val)
num_val_label.grid(row=10, column=2, sticky=W+E)
num_val_label.config(font=("", 12))

num_val_label = Label(text="", textvariable=conn_cli_val)
num_val_label.grid(row=80, column=2, sticky=W+E)
num_val_label.config(font=("", 12))

if __name__ == "__main__":
    while True:
        port_num = 80
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass
    ThreadedServer('', port_num).listen()
    tkinter.mainloop()