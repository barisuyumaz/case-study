#--------------------------------------------
#Öncelile kaçıncı asal sayıyı elde etmek istediğimizi fonksiyonun argümanı olarak giriyoruz.
#sayac değişkeni, kaçıncı indexde olduğumuz bilgisini tutacaktır. ilk 2(2 ve 3) asal değeri eklenmiş sayıyoruz(sebebi aşşağıda).
#artan_Sayi değişkeni ise asal sayı olup olmadığını kontrol ettiğimiz değişkendir.
#while ile döngünün ile sayac aracılığı ile 10101. asal değere ulaşana kadar çalışmasını sağlıyoruz. 
#key ile sayı asal mı değil mi kontrol ediyoruz.
#for döngüsü ile artan_Sayi bir asal olup olmamasını kontrol ediyoruz.
#asal sayıları bulmak için kullanılan for döngüsünün daha hızlı çalışması için;
#int(artan_Sayi**0.5)+1 -> kısmında itemın 2'den artan_Sayi'nın karekök değerine kadar gitmesini sağlıyoruz.
#(Bir sayının bölenleri arasında o sayının karekök değerine kadar bir sayı yoksa, daha yüksek değerlere bakmaya gerek yoktur bilgisine dayanarak)
#içerideki if durumu, sayının item'a bölümünden kalanı 0 bulursa o sayının bir asal olmadığı anlamına gelir.
#sayı asal değilse de key False olur ve break ile loopu durdururuz, for döngüsünün o sayı için daha gitmesine gerek yoktur.
#Eğer for döngüsü dönerken hiç if dönmez ise key True'da kalır ve o sayının asal sayı olduğu anlamına gelir. sayacımızı 1 arttırırız.
#artan_Sayi değişkenini 1 arttırarak bir sonraki değerin asal olup olmamasını kontrol ederiz.
def wanted_prime_n_index(max_index):
    sayac = 2 #2'yi ve 3'ü sayarak başlıyoruz
    artan_Sayi = 4 # for döngüsünü hızlı çalıştırmak amacıyla karekökünü bulma işlemi, min değeri maxdan yüksek tutmaması için 4 olarak tanımlıyoruz.

    while sayac < max_index:
        key = True
        for i in range(2,int(artan_Sayi**0.5)+1):
            if artan_Sayi%i==0: # true ise asal sayı değildir
                key = False
                break
        if(key):
            #print(artan_Sayi)
            sayac+=1
        artan_Sayi+=1

    return [max_index, artan_Sayi-1]
#--------------------------------------------

result = wanted_prime_n_index(10101)

print(result[0],". asal sayı :",result[1])
#Output: 10101 . asal sayı : 105953