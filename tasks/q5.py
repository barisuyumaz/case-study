liste = [1,None,2,None,None,None,None,3,None,4,None,5,None] #input
#--------------------------------------------
#convert() değişkenine input listesi girilir.
#out_list adında output değeri olacak boş liste tanımlanır.
#for index, item in enumerate(arg_list) ile input içinde dolaşılır. içindeki her itemın indexi ve kendisi alınır.
#eğer bir None itema denk gelirse o itemın indexinin bilgisi alınır. 
#while ile None olmayan değer bulana kadar devamlı bir önceki indexe bakması sağlanır.
#None olmayan bir değere ulaştığında o değeri None itemının yerine atar.
#Eğer for döngüsündeki item None değil ise input değerinin içindeki aynı indexinde yerini alırç
def convert(arg_list):
    out_list = []
    
    for index, item in enumerate(arg_list):
        if(item == None):
            current_index = index
            while(arg_list[current_index] == None):
                current_index -= 1
            out_list.append(arg_list[current_index])
        else:
            out_list.append(item)
    return out_list
#--------------------------------------------

print(convert(liste))
#Output: [1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5]