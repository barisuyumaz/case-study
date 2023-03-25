#asal_carpan() fonksiyonu, içine verilen sayıyı asal çarpanlarını bulmak için kullanılan yöntemi kullanarak
#önce 2'den kalanını sorgular ve bunu yapabildiği kadar yapar. Bu işlemi 3 ve 5 için de uygular.

#--------------------------------------------
def asal_carpan(num): #örnk 21 verdik
    while num % 2 == 0: #2'e tam bölemez
        num //= 2 # // kullanılmasının sebebi float yerine int çıktı istememiz
    while num % 3 == 0: #3'e tam bölünür
        num //= 3       # 21 // 3 = 7 | 7 tekrar 3'e tam bölünemez
    while num % 5 == 0: #5'e bölünemez
        num //= 5
    return num == 1 # num en son 7'ye eşit olduğundan return False döndürür.
#eğer burada istediğimiz kurallara uygun bir asal sayı verseydik. num değeri en sonunda 1'e eşit olacaktı
#ve sonuçta num değeri True dönecekti.
#--------------------------------------------

#--------------------------------------------
#toplam_asal_carpan() fonksiyonunda ise for döngüsü aracılığıyla 1'den istediğimiz max sayıya kadar sayılar
#arasında geziyoruz. Bu sayılarda asal_carpan() fonksiyonunu True döndüren değerleri total değişkenine
#ekliyoruz ve en sonunda toplam sonucu elde etmiş oluyoruz.
def toplam_asal_carpan(max):
    total = 0
    for num in range(1, max):
        if asal_carpan(num):
            total += num
    return total
#--------------------------------------------

print(toplam_asal_carpan(1000000))
#Output: 86485289