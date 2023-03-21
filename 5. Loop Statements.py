for i in range(5, 26, 5):
    print(i)

# Start = 0, stop = 6, step = 1, start and stop adalah default parameter
for i in range(6):
    print("Looping!")

for i in range(10, 25, 3):
    if i == 16:
        continue
    print(i)

for i in range(3, 20):
    if i % 2 == 0:
        print(i)

#While statement Akan berjalan ketika kondisi true

angka = 0

while(angka < 50):
    print("Angka yang muncul: "+ str(angka))
    angka += 10
    
    