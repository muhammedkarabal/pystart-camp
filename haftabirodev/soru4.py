rehber = {'Ali': '0555 111 22 33', 'Ayşe': '0532 444 55 66'}

yeni_isim = input("Rehbere eklenecek kişinin adı: ")
yeni_numara = input("Numarası: ")
rehber[yeni_isim] = yeni_numara 

rehber['Ali'] = '0555 999 88 77'

silinen_numara = rehber.pop('Ayşe')
print("\nAyşe rehberden silindi. Silinen numara:", silinen_numara)

aranan_isim = input("\nNumarasını öğrenmek istediğin kişinin adı: ")
sonuc = rehber.get(aranan_isim, 'Kayıt yok.')
print(aranan_isim, "için sonuç:", sonuc)

kisi_sayisi = len(rehber)

isimler = list(rehber.keys())
isimler.sort()

print("\nRehberdeki kişi sayısı:", kisi_sayisi)
print("Kişiler:", isimler)