
import socket
from random import randint
from time import sleep
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, ttk
from threading import Thread
import requests
from easygui import *

TCP_IP = '127.0.0.1'
TCP_PORT = 80
BUFFER_SIZE = 1024
name = ''
url = "http://localhost"

# GUI
# setting of window's title
top = tkinter.Tk()
top.title("Client Control Panel")
top.geometry("720x300")

# Initialize Values
name_val = tkinter.StringVar() 
calc_val = tkinter.StringVar() 
initial_val = tkinter.StringVar()
initial_val.set('1')
calc_res_val = tkinter.StringVar()
client_str = ''
client_val = 0
log_exp = ''

def receive():
    """ Handles receiving of messages. """

    # Send User Name
    client.send(str(user_name_text.get()).encode())
    
    while True:
        try:
            # Receive Data From Server
            rd = client.recv(BUFFER_SIZE).decode("UTF-8")
            
            # Polled
            if rd == "polled":
                client.send(str(calc_val.get()).encode("UTF-8"))
            # Get Updated Value
            elif rd:
                # log_exp += "<Initial Value: {}> {}\n".format(initial_val.get(), calc_val.get())
                initial_val.set(rd)
        except OSError:  # Possibly client has left the chat.
            break
        
def on_closing(event=None):
    client.close()
    top.quit()


def shut_down():
    client.send("off".encode("utf-8"))
    msgbox(log_exp,"User log")
    client.close()
    top.quit()


def startConn():
    if user_name_text.get() != "":
        receive_thread = Thread(target=receive)
        receive_thread.start()
        user_name_button.configure(state=DISABLED)
        user_name_text.configure(state=DISABLED)
    else:
        messagebox.showinfo('Info', 'Please input the client name!')
        
def onBtnCalculate():
    global log_exp
    # 4 Function Calculator
    if initial_val.get() != "":
        log_exp += "<Initial Value: {}> {}\n".format(initial_val.get(), calc_val.get())
        client_str = initial_val.get() + calc_val.get()
        for i in range(0, len(client_str)):
            if client_str[i] in ['+','-','*','/','.'] or client_str[i].isdigit():
                pass
            else:
                messagebox.showinfo('Info', 'Please input correctly!')
                return
        client_val = round(eval(client_str), 4)
        calc_res_val.set(client_val)

    else:
        messagebox.showinfo('Info', 'Please connect First!')
        
# Client Menu
cate_label = Label(text="Client")
cate_label.grid(row=1, column=3, sticky=E)
cate_label.config(font=("", 40))

# Client name label
user_name_label = Label(text="Username : ")
user_name_label.grid(row=3, column=1, sticky=W+E)

user_name_text = Entry(top, textvariable=name_val)
user_name_text.grid(row=3, column=2, sticky=W+E)
user_name_text.focus_set()

user_name_button = Button(top, text="Connect", command=startConn)
user_name_button.grid(row=4, column=2, sticky=W+E)


initial_str_label = Label(text="Initial Value: ")
initial_str_label.grid(row=8, column=4, sticky = W + E)

initial_value_label = Label(text="", textvariable=initial_val)
initial_value_label.grid(row=8, column=5, sticky = W + E)

calc_str_label = Label(text="Expression: ")
calc_str_label.grid(row=3, column=4, sticky=W+E)

calc_str_text = Entry(top, textvariable=calc_val)
calc_str_text.grid(row=3, column=5, sticky=W+E)
calc_str_text.focus_set()

calc_str_button = Button(top, text="Calculate", command=onBtnCalculate)
calc_str_button.grid(row=4, column=5, sticky=W+E)

shutdown_button = Button(top, text="Disconnect", command=shut_down)
shutdown_button.grid(row=10, column=3, sticky=W+E)

calc_res_str_label = Label(text="Result: ")
calc_res_str_label.grid(row=6, column=4, sticky = W + E)

calc_res_value_label = Label(text="", textvariable=calc_res_val)
calc_res_value_label.grid(row=6, column=5, sticky = W + E)

top.protocol("WM_DELETE_WINDOW", on_closing)

# Socket Connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((TCP_IP, TCP_PORT))
name = user_name_text.get()
tkinter.mainloop()  # Starts GUI execution.
client.close()


    
