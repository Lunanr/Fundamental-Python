#Blue Printnya
class Person:
    nama = "Budi"
    umur = 20

obj = Person()
print(type(obj))
print(obj.nama)
print(obj.umur)

#__init__() Untuk mendeklarasi property yang dimiliki oleh sebuah class
class x:
    def __init__(self, name, age, pekerjaan):
        self.name = name
        self.age = age
        self.pekerjaan = pekerjaan

p1 = x("Lunan", 32, "Data Science")

print(p1.name)
print(p1.age)
print(p1.pekerjaan)
    