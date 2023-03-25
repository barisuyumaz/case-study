ex_sentence = "Merhaba, benim adım Barış. Sizin adınız nedir?" #input
ex2_sentence = "Merhabal, benim be!:," #input

#--------------------------------------------
#noktalma işaretleri dışında da başka karakterler gelebilme ihtimaline karşı
#sadece istediğim karakterleri barındırması için türkçe alfabesindeki harfleri bir listeye tanımladım.
#turkce_harfler içinde olup olmadığını kontrol etmesi için inputdaki tüm harfleri küçük karakter yaptım.
#for döngüsü modifiye edilmiş cümle içinde geziyor ve turkce_harfler içinde bulunmayan veya boşluk(" ") olmayan tüm karakterleri yok ediyor.
#daha sonra split ile " " ları bir ayırcı olarak kullanıp, cümledeki kelimelerden bir liste oluşturdum.
#bu kelime listesinin içinde dolaşıp len ile her bir kelimenin uzunluk bilgisini total'a ekliyoruz.
#en son olarak tüm kelimelerin uzunluluğunun toplam bilgisini, kelime listesindeki eleman sayısına bölerek ortalama uzunluğu buluyoruz.
def avg_sen_words(arg_sentence):
    turkce_harfler = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
    low_letters = arg_sentence.lower()

    for i in low_letters:
        if i not in turkce_harfler and i != " ":
            low_letters = low_letters.replace(i, "")
    
    words_list = low_letters.split(" ")

    total = 0
    for i in words_list:
        total += len(i)

    avg_of_words = total // len(words_list)
    
    return avg_of_words
#--------------------------------------------

print(avg_sen_words(ex2_sentence))
#Output: 5