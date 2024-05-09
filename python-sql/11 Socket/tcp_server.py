import socket
s_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_socket.bind(('127.0.0.4',12345))
s_socket.listen(5)
while True:
    print("Server waiting for connection")
    c_socket,add=s_socket.accept()
    print("client connected")
    while True:
        data=c_socket.recv(1024)
        if not data or data.decode('utf-8')=="END":
            break
        print("recieved from client : %s", data.decode('utf-8'))
        try:
            c_socket.send(bytes("Hey client","utf-8"))
        except:
            print("Exited by the user")
    c_socket.close()
s_socket.close()