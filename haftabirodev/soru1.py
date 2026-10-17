ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")
bolum = input("Bölümünüzü giriniz: ")
gun = int(input("Doğum gününüz (Sayı olarak): "))
ay = int(input("Doğum ayınız (Sayı olarak): "))
yil = int(input("Doğum yılınız (Sayı olarak): "))

dogum_tarihi = (gun, ay, yil)
yas = 2026 - dogum_tarihi[2]

print("\n========================================")
print("PyStart Katılımcı Kartı")
print("========================================")
print("Ad Soyad    :", ad.title(), soyad.title())
print("Bölüm       :", bolum.title())
print("Doğum       : {:02d}.{:02d}.{}".format(dogum_tarihi[0], dogum_tarihi[1], dogum_tarihi[2]))
print("Yaş         :", yas)
print("========================================")