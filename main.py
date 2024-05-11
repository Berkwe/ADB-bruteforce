import porttara, subprocess, os, time

# [*] Coded by berkwe_

info = "[*] "
error = "[!] "

bitiş = False

adbports = []

if os.name == 'posix':  # Linux tabanlı işletim sistemi
    sil = "clear"
elif os.name == 'nt':   # Windows işletim sistemi
    os.system("color a")
    sil = "cls"
else:
    print(f"{error}HATA : Bu işletim sistemi desteklenmiyor.")
    sys.exit()

try:
    from prettytable import PrettyTable, DOUBLE_BORDER
except ModuleNotFoundError:
    print(f"{info}Gereklilikler indiriliyor...")
    os.system("pip install prettytable")
    from prettytable import PrettyTable, DOUBLE_BORDER



os.system(sil)
print("REMOTE ADB FİNDER".center(200,"-"))
while True:
    ip = input("Wirelles ADB'nin açık olduğu ip adres : \n>>> ") # Taranacak ip adresi
    if ip == "debug" and not porttara.debug:
        porttara.debug = True
        os.system(sil)
        print(f"{info}Debug mod açıldı")
        continue

    elif not ip or "." not in ip or len([i for i in ip if i == "."]) != 3 or len(ip.replace(".","")) > 12 or len(ip.replace(".","")) < 4 or ip.replace(".","").isdigit() == False:
        print(f"{error}HATA : LÜTFEN GEÇERLİ BİR İP GİRİN!")
        continue
    break

print(f"{info}İP Belirlendi({ip}), olası ADB portları taranıyor...")

def dene(): # ADB Bağlantı testi
    global bitiş
    try:
        subprocess.check_output("adb disconnect", shell=True, text=False)
        for port in porttara.avabileports:
            cevap = subprocess.check_output(f"adb connect {ip}:{port}", shell=True, text=True)
            if str(cevap).startswith("connected to") and port not in adbports:
                adbports.append(port)
                print(f"{info}ADB serveri bulundu : {ip}:{port}")
                while True:
                    soru = input("Taramaya devam etmek istermisiniz?[E/H] : \n>>> ")
                    if soru.lower() == "e":
                        break
                    elif soru.lower() == "h":
                        bitiş = True
                        break
                    else:
                        print(f"{error}HATA : EVET VEYA HAYIR GİRİN!")
                        continue
    except Exception as f:
        print(f"{error}HATA : ", f)

başlama = time.time() # Ölçüm

for _ in range(3):
    if bitiş == False: #Bitiş false ise devam eder
        porttara.tara(ip) #Hostu tarar
        if porttara.avabileports: #eğer açık port varsa deneme yapar
            dene()
    else: #değilse döngüyü kır
        break


table = PrettyTable() # Tablo oluştur

print(f"Program bitti!".center(200))

table.field_names = ["Açık portlar","Açık ADBS"]

# Verileri tabloya ekleme
table.add_row([", ".join(map(str, porttara.avabileports)), ", ".join(map(str, adbports))])
table.set_style(DOUBLE_BORDER)

# Sütun hizalamasını değiştirme
table.align = "l"
print(table)
print(time.time()-başlama)
