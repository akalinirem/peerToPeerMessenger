#'socket' modülü, TCP/IP veya UDP protokollerini kullanarak ağ üzerinde veri iletişimi yapmamıza izin verir.
import socket

#'send_message' fonksiyonu ip,port,message parametrelerini alır
def send_message(ip,port,message):
    #TCP/IP protokolünü kullanacak bir soket nesnesi yaratır
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#'try' bloğu başlar, çünkü bağlantı kurma ve veri gönderme işlemleri hatalar üretebilir
    try:
        #IP adresi ve bağlantı noktasına bir bağlantı kurulur
        sock.connect((ip, port))

        #'message' dizesi 'encode()' yöntemiyle baytlara dönüştürülerek 'sock.sendall(message.encode())' ile sunucuya gönderilir
        sock.sendall(message.encode())

        #'sock.recv(1024)' kullanılarak sunucudan gelen 1024 baytlık bir yanıt alınır,boyutu değiştirilebilir
        response = sock.recv(1024).decode()
        print("Sunucudan gelen yanıt:", response)

    finally:
        sock.close()

#IP adresi ve bağlantı noktasına bir sunucu başlatır
def start_server(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        #soket bağlantı noktasına bağlanılır
        sock.bind((ip, port))

        #gelen bağlantıları kabul etmek için dinlemeye başlar.1 parametresiyle belirtilen maksimum bağlantı sayısı sınırlaması vardır.
        #sunucu aynı anda en fazla 1 istemci bağlantısını kabul edebilir. Bu sayı değiştirilebilir.
        sock.listen(1)
        print("Sunucu başlatıldı.İşlemci bekleniyor...")

        while True:

            #gelen bir bağlantı kabul edilir
            client_sock, client_address = sock.accept()
            print("İstemci bağlandı:", client_address)

            data = client_sock.recv(1024).decode()
            print("İstemciden gelen mesaj:", data)

            #'response' dizesi önce 'encode()' yöntemiyle baytlara dönüştürülür ve ardından 'sendall()' yöntemiyle istemciye gönderilir
            response = "Mesaj alındı: " + data
            client_sock.sendall(response.encode())

            client_sock.close()

    finally:
        sock.close()

ip = "192.168.11.202"
port = 5555
message = "Hay Maşallah"

send_message(ip,port,message)