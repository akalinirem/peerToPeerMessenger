import socket

def send_message(ip,port,message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((ip, port))

        sock.sendall(message.encode())

        response = sock.recv(1024).decode()
        print("Sunucudan gelen yanıt:", response)

    finally:
        sock.close()

def start_server(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((ip, port))
        sock.listen(1)
        print("Sunucu başlatıldı.İşlemci bekleniyor...")

        while True:
            client_sock, client_address = sock.accept()
            print("İstemci bağlandı:", client_address)

            data = client_sock.recv(1024).decode()
            print("İstemciden gelen mesaj:", data)

            response = "Mesaj alındı: " + data
            client_sock.sendall(response.encode())

            client_sock.close()

    finally:
        sock.close()

ip = "192.168.11.202"
port = 5555
message = "Hay Maşallah"

send_message(ip,port,message)