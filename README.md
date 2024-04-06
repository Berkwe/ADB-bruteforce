# ADB Brute Force

* Bu repo, Android Debug Bridge (ADB) protokolünü kullanarak Wirelles ADB'nin açık olduğu cihazları tespit etmek için yapılmıştır. ADB Brute Force, ip-port kombinasyonlarını deneyerek cihazlara erişim sağlamaya çalışır.
* Wirellese bağlanmak bir nevi androidde back door oluşturmak gibidir. Uzaktan shell kodları çalıştırabilirsiniz!

# Kurulum

## CMD
1. Öncelikle eğer git varsa repoyu klonlayın `git clone https://github.com/Berkwe/ADB-bruteforce` (yoksa zip olarak indirip açın)
2. Sonrasında cihazınıza ADB toolsu kurmanız gerek `https://www.xda-developers.com/install-adb-windows-macos-linux/` bu linkden kurulumu bulabilirsiniz.
3. Son olarak `main.py` dosyasını çalıştırın

## Linux tabanlı dağıtımlar
NOT : dev, kali üzeridne test ettiğinde çalışmıyordu. İsterseniz indirip test edin.
1. Öncelikle repoyu klonlayın `git clone https://github.com/Berkwe/ADB-bruteforce/`
2. Sonrasında ADB toolsu kurmamız gerek bunun için `apt-get install android-tools-adb && apt-get install android-tools-fastboot`(fastboot isteğe bağlıdır)
3. Son olarak `main.py` dosyasını çalıştırın

# Kullanım
1. Sonrasında `main.py` dosyasını çalıştırın.
2. Program, belirtilen cihaz IP adresine ADB protokolü üzerinden bağlanarak oturum açma denemelerini gerçekleştirir.
3. Başarılı bir geri dönüş alınırsa, ip-port kaydedilir ve çıktı verilir.


# Önemli

* Bu programı doğru kullanmanız için cihazınızın bağlanmak istediğiniz cihazla pairlanmış olması gerekir.
* Bu program sadece açık adb portlarını bulmak için tasarlanmıştır.
* Android 9'dan önceki süürmlerde adb portu varsayılan olarak 5555'dir.
* Kullanımından kesinlikle ben sorumlu değilim, sadece eğitici amaçla kullanın.

# Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.
