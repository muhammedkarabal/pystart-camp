
baslama = input("3 notu da aralarında boşluk olacak şekilde giriniz.")
parcalar = baslama.split() 


not1 = int(parcalar[0])
not2 = int(parcalar[1])
not3 = int(parcalar[2])
notlar = [not1, not2, not3]


ek_not = int(input("Bir not daha ekle: "))
notlar.append(ek_not)


notlar.sort()
print("Notlar (sıralı):", notlar)
en_dusuk = notlar[0]
en_yuksek = notlar[-1]
print("En düşük:", en_dusuk, "En yüksek:", en_yuksek)


toplam = sum(notlar) 
eleman_sayisi = len(notlar)
ortalama = toplam / eleman_sayisi
print("Ortalama:", ortalama)
notlar.pop(0) 
print("En düşük not çıkarıldı:", notlar)


yeni_toplam = sum(notlar)
yeni_eleman_sayisi = len(notlar)
yeni_ortalama = yeni_toplam / yeni_eleman_sayisi
print("Yeni ortalama:", round(yeni_ortalama, 2))