import bs4
import urllib.request
import re

#Veri çekme kısmı
link = "https://www.tiny.cc/isimlistesi"
webpage=str(urllib.request.urlopen(link).read().decode('utf8'))
soup = bs4.BeautifulSoup(webpage)

#Çekilen verileri str haline getirip, html taglerinden kurtardık, 
#satır atlama("\n") referansı ile elemanları ayırıp liste oluşturduk
source = soup.get_text() 
pattern = re.compile('<.*?>')
result = re.sub(pattern, '', source)
name_list = result.split("\n")

#Fonksiyonlar
#--------------------------------------------
#(bilgi= büyük harfler arasında alfabetik olarak sondan başa = büyükten küçüğe şeklinde gider, ascii kodları sebebiyle)
#yani A < Z
#quicksort_names() methodunda içine alfabetik olarak sıralamasını istediğimiz listeyi giriyoruz.
#öncelikle pivot elemanı elemanı olarak listenin ilk elemanını seçiyoruz.
#pivot elemanı dışındaki liste elemanları arasında dolaşıyor ve düşük değerde olanlar left listesine, yüksek olanlar right listesine gidiyor.
#sonra pivot kendini ortaya koyacak şekilde sol listeyi gerisine, sağ listeyi ilerisine atıyor. 
#bu pivot elemanı kendi indexini bulmuş oluyor ve bir yeri daha değişmiyor.
#bu işlemlerin aynııs sol, sağ diye ayrılan listelerin içindede recursive olarak gerçekleşiyor ve sonuç olarak kısa yoldan listemiz sıralanıyor.
def quicksort_names(liste):
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste[0]
        left = []
        right = []
        for i in range(1, len(liste)):
            if liste[i] < pivot:
                left.append(liste[i])
            else:
                right.append(liste[i])
        return quicksort_names(left) + [pivot] + quicksort_names(right)
#--------------------------------------------

turkce_harfler = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
#--------------------------------------------
#return_avg_word() fonksiyonu içine konulan stringin harflerinin alfabedeki sırasını toplar ve sonucu return eder
#turkce_harfler listesini word içindeki harfin türkçe alfabedeki kaçıncı sıraya geldiğini bulmak için kullandım.
def return_avg_word(word):
    total_pos_score = 0
    word = word.replace("I","ı").lower() #normalde lower() I'yı i'ye çeviriyor. bunu önledim
    for i in word:
        if i in turkce_harfler: #boşluk karakteri hariç hepsini alıyor.
            pos_letter = turkce_harfler.index(i) + 1
            total_pos_score += pos_letter
    return total_pos_score
#--------------------------------------------

#--------------------------------------------
#içine verilen liste içindeki tüm kelimelerin içindeki karakterlerin alfabedeki sayılarını toplayıp, kelimenin listedeki indexiyle(+1) çarpar
def return_total_score(arg_list):
    total = 0
    for index, item in enumerate(arg_list):
        total_score_word = (index+1) * return_avg_word(item)
        total += total_score_word
    return total
#--------------------------------------------

sorted_list = quicksort_names(name_list) #listeyi quicksort ile sıralıyoruz
mylist = list(dict.fromkeys(sorted_list)) #sıralanan listedeki tekrar eden elemanlardan kurtuluyoruz

print(return_total_score(mylist)) #içine konulan isim listesinin skorlarını veriyor
#Output: 65792263