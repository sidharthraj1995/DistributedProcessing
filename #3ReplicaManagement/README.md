*Client*

The client executes the following sequence of steps:
1. Initialize a local copy of the shared value.
2. Connect to the server via a socket.
3. Provide the server with a unique user name.
    a. May be a string provided by the user; or,
    b. Some value associated with the process.
4. Wait to be polled by server. While waiting:
    a. Allow users to input and execute operations on the four-function
       calculator.
    b. Log user-input in persistent storage.
5. When polled by the server, upload all user-input logged since previous poll.
6. Overwrite local copy of shared value with server copy.
7. Notify user local copy has been updated.
8. Repeat at step 4 until the process is killed by the user.

*Server*

The server executes the following sequence of steps:
1. Initialize server copy of shared value.
2. Startup and listen for incoming connections.
3. Print that a client has connected and fork a thread to handle that client.
4. When instructed by the user, poll clients for user-input sequence.
5. Display received input sequences from clients on GUI.
6. Apply user-input sequence to server copy of shared value.
7. Push updated copy of shared value to clients.
8. Begin at step 4 until server is closed by the user.
