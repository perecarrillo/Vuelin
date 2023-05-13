import socket as sc

server = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
server.bind(("c8:b2:9b:1a:74:b1", 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message:")
        client.send(message.encode("utf-8"))
except OSError as e:
    pass

client.close()
server.close()