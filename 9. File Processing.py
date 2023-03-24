# "r" untuk membaca
# "w" untuk menulis kata kata baru dan menghilangkan text yang lama
# "a" untuk memambah sebuah file
file = open("File.txt", "a")
# file.write("Ini adalah text yang baru")
file.write("\nIni adalah text yang di append")
file.close

# print(file.read()) #Mencetak isi dari file
