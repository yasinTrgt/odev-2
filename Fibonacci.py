ilkSayi=1
ikinciSayi=1

fibonacciSerisi = [ilkSayi,ikinciSayi]

for f in range(20):
    ilkSayi,ikinciSayi = ikinciSayi, ilkSayi+ikinciSayi # önce sağdaki işlemleri yapar sonra atam gerçekleşir 
    fibonacciSerisi.append(ikinciSayi)

print(fibonacciSerisi)