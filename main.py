
from ast import arg
from concurrent.futures import thread
import porttara
import subprocess
import os
import time
if os.name == 'posix':  # Linux tabanlı işletim sistemi
    sil = "clear"
elif os.name == 'nt':   # Windows işletim sistemi
    sil = "cls"
else:
    print("Bu işletim sistemi desteklenmiyor.")
    sys.exit()
#coded by berkwe_
bitiş = False

adbports = []
os.system(sil)

print("REMOTE ADB BULUCU TOOL".center(200,"-"))
while True:
    ip = input("Wirelles ADB'nin açık olduğu ip adres : ") #Taranacak ip adresi
    if ip == "debug":
        porttara.debug = True
        os.system(sil)
        print("Debug mod açıldı")
        continue

    elif not ip or "." not in ip: 
        os.system(sil)
        print("LÜTFEN GEÇERLİ BİR İP GİRİN")
        continue
    
    elif len([i for i in ip if i == "."]) != 3 or len(ip.replace(".","")) > 12 or len(ip.replace(".","")) < 4 or ip.replace(".","").isdigit() == False:
        print("LÜTFEN GEÇERLİ BİR İP GİRİN!")
        continue

    pair  = input("Cihaz eşleştirildimi? (E/H) : ").lower()
    
    if pair == "h":
        os.system(sil)
        print("Pair brute force yakında!")
        break
    elif pair == "e":
        os.system(sil)
        break
    else:
        os.system(sil)
        print("EVET(E)/HAYIR(H) KULLANIN.")
print(f"İP Belirlendi({ip}), olası ADB portları taranıyor...")

def dene(): #ADB Bağlantı testi
    try:
        if not porttara.avabileports: 
            print("Hiç açık port bulunamadı hedef bilgisayarda wirelles adb kapalı.") 
        else:
            subprocess.check_output("adb disconnect")
            for port in porttara.avabileports:
                cevap = subprocess.check_output(f"adb connect {ip}:{port}", shell=True, text=True)
                if str(cevap).startswith("connected to") and port not in adbports:
                    adbports.append(port)
                    print(f"ADB serveri bulundu : {ip}:{port}")
                    while True:
                        soru = input("Taramaya devam etmek istermisiniz?[E/H] : ")
                        if soru.lower() == "e":
                            break
                        elif soru.lower() == "h":
                            bitiş = True
                            break
                        else:
                            print("EVET VEYA HAYIR GİRİN!")
                            continue
    except Exception as f:
        print("Bir hata oluştu", f)

başlama = time.time() # Ölçüm

for _ in range(2):
    if bitiş == False: #Bitiş false ise devam eder
        porttara.tara(ip) #Hostu tarar
        if porttara.avabileports: #eğer açık port varsa deneme yapar
            dene()
    else: #değilse döngüyü kır
        break
print("\t\t\tPROGRAM BİTTİ!\n\t---------------------------------------------------\n")
print("\t\tAçık portlar : ", end="")
for i in porttara.avabileports:
    print(i, end=" , ")
print("\t\t\n\n\t---------------------------------------------------\n")
print("\t\tAçık adb portları : ",end='')
for i in adbports:
    print(f"{i}", end=" , ")
print(f"\t\t\n\n\t---------------------------------------------------\nGeçen zaman : {time.time()-başlama}")

            




