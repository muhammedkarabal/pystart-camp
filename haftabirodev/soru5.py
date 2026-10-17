kisi1_girdi = input("1. kişinin hobileri (virgülle ayırarak giriniz): ")
kisi2_girdi = input("2. kişinin hobileri (virgülle ayırarak giriniz): ")
kisi1_son = kisi1_girdi.replace(" ", "")
kisi2_son = kisi2_girdi.replace(" ", "")

kume1 = set(kisi1_son.split(","))
kume2 = set(kisi2_son.split(","))
ortak_hobiler = kume1.intersection(kume2)
sadece_kisi1 = kume1.difference(kume2)
sadece_kisi2 = kume2.difference(kume1)
tum_hobiler = kume1.union(kume2)

print("\nOrtak hobiler:", sorted(ortak_hobiler))
print("Yalnızca 1. kişide olanlar:", sorted(sadece_kisi1))
print("Yalnızca 2. kişide olanlar:", sorted(sadece_kisi2))
print("Tüm hobiler:", sorted(tum_hobiler))

ortak_var_mi = int(len(ortak_hobiler)) > int(0)
esit_mi = int(len(kume1)) == int(len(kume2))
uc_hobi_mi = int(len(kume1)) >= int("3") and int(len(kume2)) >= int("3")
satranc_var_mi = "satranç" in tum_hobiler

print("\nOrtak hobi var mı?", ortak_var_mi)
print("Hobi sayıla eşit mi?", esit_mi)
print("İkiniz de en az 3 hobi yazdınız mı?", uc_hobi_mi)
print("'satranç' ikinizden birinin hobisi mi?", satranc_var_mi)