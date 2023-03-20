x = 5
y = 10
z = 15
a = 10

# Conditional Statement 
print(not(x > y))
print(x < y)
print(x < y or y > z)

if x == y: #False
    print("X tidak sama dengan Y")

if x != y: #True
    print("X tidak sama dengan Y")

if (x < y):
    print("X lebih kecil dari Y") #Ketika kondisinya True
else:
    print("X lebih besar dari Y")

if x > y:
    print("X lebih kecil dari Y")
elif y == a:
    print("Y sama dengan Z")
else:
    print("Tidak ada kondisi True")