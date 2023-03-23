# Collection List
# Append, insert, remove, pop, del, clear
listExample = ['Python', 42, 3.4, True, 42]
print(listExample)
listExample.remove('Python') #Menghapus sesuai dengan nilai
listExample.pop() #Akan menghapus elemen ter akhir
del listExample[2] # Untuk menghapus index yang dipilih
listExample.clear() # Untuk menghapus seluruh index

listExample_1 = [40, 50, 25, 75, 80]
listExample_2 = [10, 50, 33]
listExample_3 = listExample_1.copy()
print(listExample_3)
listExample_1.extend(listExample_2)
print(listExample_1)
print(listExample_1.index(10))
listExample_1.reverse()
print(listExample_1)

for item in listExample_1:
    if item == 40:
        print("Terdapat angka 40 didalam list")

length = len(listExample_1)