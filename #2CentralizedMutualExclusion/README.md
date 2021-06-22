**Client**
The client executes the following sequence of steps:
1. Connect to the server via a socket.
2. Provide the server with a unique user name.
a. May be a string provided by the user; or,
b. Some value associated with the process.
3. Generate a random integer between 3 and 10.
4. Upload that integer to the server.
5. Wait until response received from the server.
6. Parse the HTTP message and print response from the server in normal text.
7. Inform the user of the total time spent waiting for the server response.
8. Repeat at step 3 until the process is killed by the user.

**Server**
The server executes the following sequence of steps:
1. Startup and listen for incoming connections.
2. Print that a client has connected and fork a thread to handle that client.
3. Queue the integers received from clients.
4. Pop the queued integers in the order they were received from clients.
5. Print the current integer to the GUI and announce that it is waiting for that period
of time.
6. Pause (sleep or otherwise wait) all client-handling threads for the number of
seconds equal to that integer.
7. After waiting, return a message to client stating, “Server waited <#>
seconds for client <name>.”
8. Begin at step 3 until connection is closed by the client.
  
Instructions to run the program:

1. Open terminal in the directory where you extracted the files.
2. Run the server by typing ‘./Server.py’ Once, the server is up and running and listening for connections, time to initiate the client connection.
3. Open another terminal in the same directory, and type ‘./Client.py’ You can run desired number of clients on different terminal windows.
