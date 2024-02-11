import socket;
import time;

client = socket.socket()
client .connect(("127.0.0.1", 5555))

time.sleep(1)
client.send('log-1'.encode())
time.sleep(1)
client.send('log-2'.encode())
time.sleep(1)
client.send('log-3'.encode())
time.sleep(1)
client.send('log-4'.encode())

client.close()