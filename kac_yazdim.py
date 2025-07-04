import random

def kac_yazdim():
    gizli_sayi = random.randint(1, 100)
    print("Ben 1 ile 100 arasında bir sayı tuttum!")

    tahmin = None
    deneme_sayisi = 0

    while tahmin != gizli_sayi:
        try:
            tahmin = int(input("Kaç yazdım? "))
        except ValueError:
            print("Lütfen tam sayı gir.")
            continue  # sadece sayı girilmeyince döngü başa dönsün

        if tahmin < 1 or tahmin > 100:
            print("1 ile 100 arasında bir sayı yazmalısın!")
            continue  # sınır dışıysa yine başa dön

        deneme_sayisi += 1

        if tahmin < gizli_sayi:
            print("Daha büyük söyle.")
        elif tahmin > gizli_sayi:
            print("Daha küçük söyle.")
        else:
            print(f"Bravo! {deneme_sayisi} denemede bildin.")

# Oyunu tekrar oynamak için dış döngü
while True:
    kac_yazdim()
    cevap = input("Tekrar oynamak ister misin? ('e' / 'h'): ")
    if cevap.lower() != "e":
        print("Görüşmek üzere!")
        break
