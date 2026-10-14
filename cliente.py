import socket


MAX_DATE = 1024

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(("192.168.1.120" , 7000))

print("connecté au server !")

while True:
    reponse = client.recv(MAX_DATE)
    if not reponse:
        break

    print("Reponse :", reponse.decode())
    test=input("ZEBI : ")
    client.sendall(test.encode())

client.close
