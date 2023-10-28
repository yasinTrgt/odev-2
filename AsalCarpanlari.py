sayi = int(input("Bir sayı girin: "))
def asal_carpanlari_bul(sayi):
    carpanlar = []
    carpan = 2
    while sayi > 1:
        if sayi % carpan == 0:
            carpanlar.append(carpan)
            sayi //= carpan
        else:
            carpan += 1
    return carpanlar
print(asal_carpanlari_bul(sayi))