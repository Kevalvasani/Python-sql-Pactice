import socket
c_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c_socket.connect(('127.0.0.4',12345))
payload="Hey Server"
try:
    while True:
        c_socket.send(payload.encode('utf-8'))
        data=c_socket.recv(1024)
        print(str(data)) 
        more=input("want to send more data to the server : ")
        if more.lower()=="y":
            payload=input("input payload : ")
        else:
            break
except KeyboardInterrupt:
    print("enter by user")
    c_socket.close()