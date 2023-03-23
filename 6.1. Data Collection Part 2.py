#Tuple
# tupleExample = (2, 3, 'python', 3.8, True) #Perbedaan dengan list dari kurungnya
# # Tuple tidak bisa merubah isi dari valuenya
# print(tupleExample[0:3])

#Dictionary
"""Kamus yang digunakan untuk menyimpan data dalam bentuk key:value dan
menggunakan kurung kurawal """
# customer = {
#     "id" : 100,
#     "nama" : "Luthfi",
#     "Umur" : 22
# }

# customer["pekerjaan"] = "pengusaha" #Menambahkan nilai dan value
# # customer.pop("umur") #Untuk menghilangkan value

# print(customer)
# # print(customer["nama"])
# # print(customer["Umur"])

#Set
numbers1 = {1, 3, 5, 7, 10}
numbers2 = {3, 4, 6, 8, 10}

# numbers_union = numbers1.union(numbers2) #Menggabungkan dua nilai dan angka duplikat muncul sekali
# numbers_different = numbers1.difference(numbers2) #Mencari nilai yang berbeda dari numbers1
# numbers_symetric = numbers1.symmetric_difference(numbers2) #Mencetak semua nilai yang berbeda
numbers_intersection = numbers1.intersection(numbers2) #Mencetak nilai yang sama
print(numbers_intersection)