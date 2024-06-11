# Chat Application

This project is a chat application with a server and multiple clients. Clients can connect to the server and chat with each other in real-time. The server has controls to start and stop the service, and each client can send and receive messages.

## Group Members
- Foisal Ahmed Fahim (221-134-008)
- Dipto Deb Nath (221-134-013)

## Prerequisites

Before running this project, ensure you have the following installed on your device:

- Python 3.x
- `tkinter` library (usually comes pre-installed with Python)
- An IDE or text editor (VS Code is recommended)

## How to Run the Project

### 1. Clone the Repository
First, clone the repository to your local machine using Git:
```bash
git clone https://github.com/fahimx51/Chat-Server.git
cd chat-application
```


### 2. Run the Server
Navigate to the project directory and run the server script.

### 3. Run the Client(s)
In the project directory, run the client script.

## Server GUI Description

The server GUI consists of:
- **Start Button**: Starts the server and begins listening for client connections.
- **Stop Button**: Stops the server and disconnects all clients.
- **Text Area**: Displays connection messages and chat messages received from clients.
- **Server Info**: Displays the server's IP address and port number.

When you start the server, the IP address and port number are displayed in the GUI, and clients can connect using these details. The text area shows all messages sent by the clients and status messages like when a client connects or disconnects.

## Client GUI Description

The client GUI consists of:
- **Username Entry**: Field to enter your username.
- **IP Address Entry**: Field to enter the server's IP address.
- **Port Entry**: Field to enter the server's port number.
- **Connect Button**: Connects to the server using the provided details.
- **Text Area**: Displays chat messages from all clients, including your own.
- **Message Entry**: Field to enter your chat message.
- **Send Button**: Sends the entered message to the server.

To connect to the server, you need to provide a username, the server IP address, and the port number. Once connected, you can send messages to all other clients connected to the server. The messages will appear in the text area along with messages from other clients.

## Additional Information

- **Server IP Address**: The server will bind to `0.0.0.0` and listen on port `12345`. The actual IP address of the server will be displayed in the server GUI.
- **Message Broadcasting**: Messages sent by a client are broadcasted to all connected clients, including the sender, ensuring everyone sees all messages in real-time.

Feel free to contribute to the project by submitting issues or pull requests on GitHub.

---

This project was developed as part of a group assignment for our course. We hope you find it useful and educational!
