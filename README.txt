microservice.py README.txt:

Introduction:

microservice.py is a simple Python script that functions as a microservice using ZeroMQ (ZMQ). The microservice 
generates random player information by reading data from a CSV file (all_players.csv) and responds to client 
requests over the ZeroMQ protocol.


Dependencies:

Make sure to have the following dependencies installed:
    -pandas
    -zmq (ZeroMQ)
You can install these dependencies using the following command: pip install pandas zmq


Usage:

Ensure that the required CSV file (all_players.csv) is in the same directory as microservice.py. The CSV file 
should contain player information, such as Name, Club, Nation, and Overall rating.


Run the microservice.py script using the following command:

python3 microservice.py
The microservice will bind to tcp://*:5555 and start listening for client requests.


Functionality:

The microservice performs the following steps

-Waits for a request from a client.
-Generates random player information by reading a random row from the all_players.csv file.
-Constructs a dictionary with player information (Name, Club, Nation, Overall rating).
-Sends the formatted player information back to the client.
-ZeroMQ Configuration
-The microservice uses ZeroMQ's Request-Reply (REQ-REP) pattern. It binds to the address tcp://*:5555 and waits for 
 incoming requests from clients.


Communication Contract:

This microservice follows a simple Request-Reply (REQ-REP) communication pattern using ZeroMQ (ZMQ). Please adhere to the following contract for seamless communication.

Requesting Data:
To programmatically request data from the microservice, follow these steps ---

Establish a connection: Use a ZMQ Request socket to connect to the microservice at tcp://localhost:5555.

Send a request message: Send an empty message to the microservice to request player information.

Example Call:


    import zmq

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Send a request for player information
    socket.send(b"")

    # Receive the response
    response = socket.recv_string()
    print(f"Received player information: {response}")


Receiving Data:

To programmatically receive data from the microservice, follow these steps ---

-Run the microservice: Ensure that the microservice.py script is running, binding to tcp://*:5555.
-Receive the response: After sending a request, receive the formatted player information as a string.


UML Sequence Diagram:

+---------------------+         +---------------------+
|      Client         |         |    Microservice     |
+---------------------+         +---------------------+
        |                             |
        |         Establish           |
        |         Connection          |
        |---------------------------->|
        |                             |
        |        Send Request         |
        |---------------------------->|
        |                             |
        |                             |   Wait for Request
        |                             |   ----------------->
        |                             |
        |                             |   Generate Player
        |                             |   Information
        |                             |   ----------------->
        |                             |
        |      Receive Response       |
        |<----------------------------|
        |                             |
