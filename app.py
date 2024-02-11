import socket;
import threading;

# ip version4 ,  protocol tcp
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# give it an ip and port and listen on it
server.bind(('127.0.0.1', 5555))
server.listen()

# while True:
#     # do handshaking => get data and address from the client
#     client , address = server.accept()
#     data = client.recv(1024)
#     # decode data as it's asciicode => ascii to string
#     print(data.decode())
#     # string to ascii
#     client.send("hi client".encode() )
#     client.close()

list_of_clients = [];

def handle(client:socket.socket):
    while True:
        data = client.recv(2048)
        with open("./log.txt", '+a') as f:
            if (data.decode()).strip() != '':
                f.write(str(id(client)) + ' ' + data.decode() + '\n')

while True:
    # do handshaking => get data and address from the client
    client , address = server.accept()
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()