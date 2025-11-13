# Day3:Python之助

## 0x0前言

为什么要学python？

python善于自动化处理，对于一个hacker来说，自动化工具是必不可少的。

所谓工欲善其事必先利其器，工具就是hacker最锋利的刀。

例如netcat，被称为网安的瑞士军刀。

但是，当进入内网后，可能会遇到没有netcat的情况，这个时候就要用python来构建这个通道了。

## 1x0 基础的网络编程工具

```python
#TCP Client
import socket

target_host = "127.0.0.1"
target_port = 9998

#client a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to the server
client.connect((target_host,target_port))

#send some datas
client.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

#recieve return data and print on the screen
response = client.recv(4096)

print(response.decode())

#close the client
client.close()
```

```python
#TCP Server
import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((IP,PORT))
	server.listen(5)
	print(f'[*] Listening on {IP}:{PORT}')
	
	while True:
		client,address = server.accept()
		print(f'[*] Accepted connection from {address[0]}:{address[1]}')
		client_handler = threading.Thread(target=handle_client,args=(client,))
		client_handler.start()
		
def handle_client(client_socket):
	with client_socket as sock:
		request = sock.recv(1024)
		print(f'[*] Received:{request.decode("utf-8", errors="replace")}')
		sock.send(b'ACK')
		
if __name__ == '__main__':
	main()
```

在kali中通信效果如下：

左侧为Client，右侧为Server

![image-20251112162246451](C:\Users\21543\AppData\Roaming\Typora\typora-user-images\image-20251112162246451.png)



