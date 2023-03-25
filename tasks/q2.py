#--------------------------------------------
def fibonacci_total(max):
    first = 1
    second = 1       # first ve second değişkenlerinde ilk 2 fibonacci sayısını belirtiyoruz
    num_holder = 0   # kümemizdeki son 2 sayının toplamını tutacak değişken
    total = 0 

    while first < max:
        #print(first) # max değere kadar olan tüm fibonacci sayılarını yazdırır.
        if(first%3 == 0):
            #print(first) # 3'e tam bölünebilen fibonacci sayılarını yazdırır
            total += first #burada total değişkene ekler

        num_holder = first + second # fibonacci kümesindeki son 2 sayıyı toplar
        first = second              # yeni sayı eklemek için first değişkeni secondun yerine geçer
        second = num_holder         # yeni sayı olmak için second, first ile toplamı olan sayı yerine geçer

    return total
#--------------------------------------------

print(fibonacci_total(5000000))
#Output: 2550408