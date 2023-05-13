import socket as sc

client = sc.socket(sc.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
client.connect(("c8:b2:9b:1a:74:b1", 4))

message = input("input game name:")
message = client.send(message.encode("utf-8"))

client.close()

# try:
#     while True:
#         message = input("Enter message: ")
#         client.send(message.encode("utf-8"))
#         data = client.recv(1024)
#         if not data:
#             break
#         print(f"Message: {data.decode('utf-8')}")
# except OSError as e:
#     pass

# client.close()