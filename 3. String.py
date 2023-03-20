text = "luthfi Adnan r"
text1 = "seorang data Scientist"
umur = 20

#String Methods
print(text.upper()) #Membuat kalimat menjadi huruf kapital semua
print(text.lower()) #Membuat kalimat menjadi huruf kecil
print(len(text)) #Menghitung berapa banyak character
print(text.split(' ')) #Memotong berdasarkan spasi
print(text.capitalize()) #Merubah huruf depan menjadi besar
print(text.index('a')) #Mencari index dalam sebuah karater
print(text[-1]) #Mencetak karater dari -1
print(text[:]) #Mecetak dari karater pertama hingga akhir
print(text + " " + text1 + " ")

text2 = "{} berumur {} tahun sebagai {}"
print(text2.format(text,umur,text1))

print("tahun" in text2) #Mecari tahun dalam text2
print("Umur" in text2) #Mecari Umur dalam text2