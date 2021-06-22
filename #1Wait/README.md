**Client**
The client executes the following sequence of steps:
1. Connect to the server via a socket.
2. Provide the server with a unique user name.
    a. May be a string provided by the user; or,
    b. Some value associated with the process.
3. Generate a random integer between 5 and 15.
4. Upload that integer to the server.
5. Wait until response received from the server.
6. Parse the HTTP message and print response from the server in normal text.
7. Repeat at step 3 until the process is killed by the user.


**Server**
The server supports three concurrently connected clients and displays a list of
which clients are connected in real-time. The server then executes the following sequence
of steps:
1. Startup and listen for incoming connections.
2. Print that a client has connected and fork a thread to handle that client.
3. Print integer received from client to GUI and announce that it is waiting for that
period of time.
4. Pause (sleep or otherwise wait) for the number of seconds equal to that integer.
5. After waiting, will return a message to client stating, “Server waited <#>
seconds for client <name>.”
6. Begin at step 3 until connection is closed by the client.


Instructions to run the program:

1. Open terminal in the directory where you extracted the files.
2. Run the server by typing ‘./Server.py’ Once, the server is up and running and listening for connections, time to initiate the client connection.
3. Open another terminal in the same directory, and type ‘./Client.py’
You can run desired number of clients on different terminal windows.

Working:
User executes the python code.
User is prompt to enter a username.
Program starts generating random numbers between 5 and 15.
Random number is sent to the server and the server puts the client thread to sleep for those seconds.
