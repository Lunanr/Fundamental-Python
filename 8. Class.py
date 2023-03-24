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

    def greet(self):
        print("Halo, " + self.name + "!")

p1 = x("Lunan", 32, "Data Science")
p3 = x("Abiyyu", 15, "Pelajar")

# print(p1.__dict__)
# print(p3.__dict__)    
p1.greet()

class Binatang: #Class yang lebih general / Parent Class
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Binatang): #Child Class
    def __init__(self, name, age, color, weight):
        super().__init__(name,age)
        self.color = color
        self.weight = weight

class Dog(Binatang): #Child Class
    def __init__(self, name, age, type):
        super().__init__(name,age)
        self.type = type

a = Dog("Herder", 15, "Mamals")
print(a.__dict__)