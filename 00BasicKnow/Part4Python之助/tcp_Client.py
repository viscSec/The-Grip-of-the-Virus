import socket

target_host = "127.0.0.1"
target_port = 9998

#建立一个socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#将客户端连接到服务器
client.connect((target_host,target_port))

#发送一些bytes类型数据
client.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

#接收返回的数据并打印到屏幕上
response = client.recv(4096)

print(response.decode())
client.close() 