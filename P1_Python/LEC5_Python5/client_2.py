import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('localhost',1235))
        
while True:
    msg = str(input("please enter the message you want to send : "))
    print('-------------------------------------------------------')
    msg_encoded = msg.encode('UTF-8')
    client.send(msg_encoded)

    rodata = client.recv(1024)
    print(f"localhost sended {rodata.decode('UTF-8')}")
    client.close()