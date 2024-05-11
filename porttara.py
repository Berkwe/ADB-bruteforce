import socket
import threading
import sys
import subprocess

error = "[!] "

#coded by berkwe_
avabileports = []
debug = False
# Port taramak için bir fonksiyon
def scan_port(host, port):
    try:
        # TCP isteği atar ve cevap bekler(linuxda sıkıntılı olan kısım bu)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Deneme yap
            result = sock.connect_ex((host, port))
            if debug == True:

                print(f"TARANDI : {port}",f"BULUNDU : {avabileports}", sep="\t\t")
            # Cevap gelirse port açık
            if result == 0:

                # Avabile ports listesine ekler.
                avabileports.append(port)
    except Exception as f:
        print(f"{error}HATA : ",f)


taranan = [30000, 40000]
def tara(host):
    threds = []
    for port in range(taranan[0], taranan[1]):
        thread = threading.Thread(target=scan_port, args=(host, port))
        threds.append(thread)
        thread.start()
    for thread in threds:
        thread.join()
    taranan[0] = taranan[1]
    taranan[1] += 10000 
