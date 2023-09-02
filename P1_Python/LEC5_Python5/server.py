import socket
import threading

def handler(client):
    rodata = client.recv(1024)
    print(f"{add} sended {rodata.decode('UTF-8')}")
    msg = str(input(f"Reply to {add}: "))
    msg = msg.encode('UTF-8')
    client.send(msg)
    client.close()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1235))
s.listen()

while True:
    client , add = s.accept()
    print(f"{add} connected")
    print('-------------------------------------------------------')
    clients = threading.Thread(target=handler,args=(client,))
    clients.start()