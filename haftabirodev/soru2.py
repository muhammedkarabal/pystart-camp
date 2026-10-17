cumle = input("Lütfen bir cümle giriniz: ")

toplam_karakter = len(cumle) 
bosluksuz_cumle = cumle.replace(" ", "")
bosluksuz_karakter = len(bosluksuz_cumle)
kelimeler = cumle.split() 
kelime_sayisi = len(kelimeler)
ilk_kelime = kelimeler[0]
son_kelime = kelimeler[-1] 
buyuk_harfli = cumle.upper()
ters_cumle = cumle[::-1] 
kucuk_cumle = cumle.lower() 
a_sayisi = kucuk_cumle.count("a")
i_sayisi = kucuk_cumle.count("i")

python_var_mi = "python" in kucuk_cumle

print("\n--- Cümle Analizi Sonuçları ---")
print("Karakter sayısı:", toplam_karakter)
print("Boşluksuz karakter sayısı:", bosluksuz_karakter)
print("Kelime sayısı:", kelime_sayisi)
print("İlk kelime:", ilk_kelime)
print("Son kelime:", son_kelime)
print("Büyük harfli hali:", buyuk_harfli)
print("Tersten yazılışı:", ters_cumle)
print("'a' harfi sayısı:", a_sayisi)
print("'i' harfi sayısı:", i_sayisi)
print("Cümlede 'python' geçiyor mu?:", python_var_mi)


# Gözlem: küçük "ı" ile küçük "i" farklı karakterler ancak küçük "i" ile büyük "İ" aynı karakter.




