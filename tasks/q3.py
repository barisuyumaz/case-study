#--------------------------------------------
#3 basamaklı tüm sayıların çarpım ihtimallerini elde etmek için iç içe 2 for döngüsü kullanıyoruz.
#daha az işlem için içteki for döngüsünde başlangıç değeri olarak dış for'un itemını kullanıyoruz.
#product değişkenine tüm 2 tane 3 basamaklı sayıların çarpımını aşşağıda tekrar tekrar denemesi için atıyoruz.
#str(product) == str(product)[::-1] product değişkeninde elde edilen çarpımı stringe çevirip, düz haliyle tersini karşılaştırıyoruz.
#ör: "10022" == "22001" şeklinde sorgulama yapıyor ve False döndürüyor. "110011" == "110011" olsa True döner
#Yukarıdaki koşul karşılandığı takdirde daha sonra gelecek aynı koşulları sağlayan değer bir öncekinden yüksek mi kontrol ediyoruz.
#Sonra gelen değerler daha yüksek değilse eğer bu if bloğu bir çalışmıyor.
#max_palindrom, koşulları sağlayan en yüksek çarpıma atanıyor.
def find_max_pal():
    max_palindrom = 0

    for j in range(1000, 99, -1):
        for i in range(j, 99, -1): 
            product = i * j
            if str(product) == str(product)[::-1] and product > max_palindrom:
                max_palindrom = product

    return max_palindrom
#--------------------------------------------

print(find_max_pal())
#Output: 906609