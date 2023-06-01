import socket


def receive_message(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        sock.bind((ip, port))
        sock.listen(1)
        print("Sunucu başlatıldı. İstemci bekleniyor...")


        client_sock, client_address = sock.accept()
        print("İstemci bağlandı:", client_address)


        data = client_sock.recv(1024).decode()
        print("İstemciden gelen mesaj:", data)


        client_sock.close()

    finally:

        sock.close()



ip = "192.168.11.209"
port = 5555

while True:
    receive_message(ip, port)
