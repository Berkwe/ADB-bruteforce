import socket
import threading
import sys
import subprocess
#coded by berkwe_
avabileports = []
debug = False
# Port taramak için bir fonksiyon
def scan_port(host, port):
    try:
        # TCP isteği at (socket modulu ile max bu)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # deneme yap
            result = sock.connect_ex((host, port))
            if debug == True:

                print(f"TARANDI : {port}",f"BULUNDU : {avabileports}", sep="\t\t")
            # Cevap gelirse port açık
            if result == 0:

                #avable ports listesine eklersin ve main dosyasında çağrırsın
                avabileports.append(port)
    except Exception as f:
        print("Hata oluştu :",f)
taranan = [30000,40000]
def tara(host):
    try:

        cevap = subprocess.check_output(f"ping {host}", shell=True, text=True)
        if "unreachable" in cevap.lower():
            print("*HATA : Host cevap vermiyor.*")
            sys.exit()
    except subprocess.CalledProcessError as e:
        print("*HATA : Girdiğiniz ip yanlış.")
        sys.exit()
    for port in range(taranan[0], taranan[1]):
        threading.Thread(target=scan_port, args=(host, port)).start()
    taranan[0] = taranan[1]
    taranan[1] += 10000

