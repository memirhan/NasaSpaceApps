import re
from PIL import Image

try:
    with open('dbs2.sql', 'r', encoding='utf-8') as f:
        sql_verisi = f.read()
    
except FileNotFoundError:
    exit()

# INSERT ifadelerini bul ve verileri işleyelim
insert_ifadeleri = re.findall(r"INSERT INTO `kullanicilar3` \(`id`, `cinsiyet`, `soru1`, `soru2`, `soru3`, `soru4`, `soru5`\) VALUES\s*(.*?);", sql_verisi, re.DOTALL)

veriler = []
for ifade in insert_ifadeleri:
    girdiler = re.findall(r"\((.*?)\)", ifade)
    for girdi in girdiler:
        veri = [eleman.strip().strip("'") for eleman in girdi.split(',')]
        veriler.append(veri)

# Cinsiyet ve soru1 bilgilerini alalım
cinsiyetler = [veri[1] for veri in veriler]
soru1_cevaplar = [veri[2] for veri in veriler]  # İlk soruya verilen cevapları alıyoruz

# Cinsiyete göre cevapları sayma
cevap_dagilimi = {
    'erkek': {'1': 0, '0': 0},
    'kiz': {'1': 0, '0': 0}
}

# 1 ve 0 olarak sınıflandıracağımız cevaplar
pozitif_cevaplar = ['temizlik_ferahlık', 'umut_yenilik', 'huzur']
negatif_cevaplar = ['bosluk', 'yalnizlik', 'sogukluk']

for i in range(len(cinsiyetler)):
    cinsiyet = cinsiyetler[i]
    cevap = soru1_cevaplar[i]

    # Boş olan cevapları atlama
    if cevap.strip() == '':
        continue

    # Cevapları sınıflandırma (1 veya 0 değeri atama)
    if cevap in pozitif_cevaplar:
        cevap = '1'
    elif cevap in negatif_cevaplar:
        cevap = '0'

    # Cinsiyet bazında cevapları toplama
    if cinsiyet in cevap_dagilimi:
        cevap_dagilimi[cinsiyet][cevap] += 1

# Erkek ve kızların olumlu/olumsuz kişi sayıları
erkek_olumlu = cevap_dagilimi['erkek']['1']
erkek_olumsuz = cevap_dagilimi['erkek']['0']

kiz_olumlu = cevap_dagilimi['kiz']['1']
kiz_olumsuz = cevap_dagilimi['kiz']['0']

# Sonuçları gösterme
print(f"Erkeklerin değerlendirmesi:")
print(f"- Erkeklerden {erkek_olumlu} kişi olumlu tepki vermiş.")
print(f"- Erkeklerden {erkek_olumsuz} kişi olumsuz tepki vermiş.")

print(f"\nKızların değerlendirmesi:")
print(f"- Kızlardan {kiz_olumlu} kişi olumlu tepki vermiş.")
print(f"- Kızlardan {kiz_olumsuz} kişi olumsuz tepki vermiş.")