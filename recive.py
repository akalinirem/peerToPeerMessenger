import socket


def receive_message(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        # soket bağlantı noktasına bağlanılır
        sock.bind((ip, port))

        # gelen bağlantıları kabul etmek için dinlemeye başlar.1 parametresiyle belirtilen maksimum bağlantı sayısı sınırlaması vardır.
        # sunucu aynı anda en fazla 1 istemci bağlantısını kabul edebilir. Bu sayı değiştirilebilir.
        sock.listen(1)
        print("Sunucu başlatıldı. İstemci bekleniyor...")

        # gelen bir bağlantı kabul edilir
        client_sock, client_address = sock.accept()
        print("İstemci bağlandı:", client_address)

        #'client_sock.recv(1024)' ile alınır ve data değişkenine atanır.
        data = client_sock.recv(1024).decode()
        print("İstemciden gelen mesaj:", data)


        client_sock.close()

    finally:

        sock.close()



ip = "192.168.11.209"
port = 5555

while True:
    receive_message(ip, port)
