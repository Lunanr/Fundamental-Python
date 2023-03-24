#Function create and call
def greet(name,age):
    print("Hello, " + name)
    print("Age: " + str(age))

greet("Lunan",20)
greet("Rahman",22)
greet(age = 30, name = "cecep")

def add5(x):
    total = x + 5
    return total

print(add5(2))

#Lambda Function Untuk membuat sebuah function menjadi singkat
add4 = lambda n: n+5
print(add4(4))