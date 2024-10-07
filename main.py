import re
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# SQL dosyasından verileri okuma
try:
    with open('dbs2.sql', 'r', encoding='utf-8') as f:
        sql_verisi = f.read()
    print("SQL dosyası başarıyla okundu.")
except FileNotFoundError:
    print("SQL dosyası bulunamadı.")
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
    'erkek': {},
    'kiz': {}
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
    if cinsiyet not in cevap_dagilimi:
        cevap_dagilimi[cinsiyet] = {}

    if cevap not in cevap_dagilimi[cinsiyet]:
        cevap_dagilimi[cinsiyet][cevap] = 0
    cevap_dagilimi[cinsiyet][cevap] += 1

# Renkleri analiz etme
resim = Image.open('elma.jpeg')
resim = resim.convert('RGB')
pikseller = list(resim.getdata())

# Temel renk frekanslarını tutacak bir dict
renk_frekanslari = {
    'Beyaz': sum(1 for r, g, b in pikseller if r > 200 and g > 200 and b > 200),
    'Siyah': sum(1 for r, g, b in pikseller if r < 50 and g < 50 and b < 50),
    'Mavi': sum(1 for r, g, b in pikseller if b > 150 and r < 100 and g < 100),
    'Kırmızı': sum(1 for r, g, b in pikseller if r > 150 and g < 100 and b < 100),
    'Sarı': sum(1 for r, g, b in pikseller if r > 150 and g > 150 and b < 100)
}

# Analiz
for renk, frekans in renk_frekanslari.items():
    erkek_olumlu = cevap_dagilimi['erkek'].get('1', 0)
    erkek_olumsuz = cevap_dagilimi['erkek'].get('0', 0)
    kiz_olumlu = cevap_dagilimi['kiz'].get('1', 0)
    kiz_olumsuz = cevap_dagilimi['kiz'].get('0', 0)

    if frekans > 0:
        if erkek_olumlu > 0:
            print(f"{renk} rengini gören erkeklerin olumlu görüş sayısı: {erkek_olumlu}. Bu, erkeklerin bu resme olumlu yaklaşabileceğini gösteriyor.\n")
        else:
            print(f"{renk} rengini gören erkeklerin olumsuz görüş sayısı: {erkek_olumsuz}. Bu, erkeklerin bu resme olumsuz yaklaşabileceğini gösteriyor.\n")

        if kiz_olumlu > 0:
            print(f"{renk} rengini gören kızların olumlu görüş sayısı: {kiz_olumlu}. Bu, kızların bu resme olumlu yaklaşabileceğini gösteriyor.\n")
        else:
            print(f"{renk} rengini gören kızların olumsuz görüş sayısı: {kiz_olumsuz}. Bu, kızların bu resme olumsuz yaklaşabileceğini gösteriyor.\n")
    else:
        print(f"{renk} rengi yok, analiz yapılamaz.\n")
