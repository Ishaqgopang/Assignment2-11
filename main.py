# for i in range (0, 101):
#     if i % 3 ==0:
#         print('Fizz')
#         continue
#     # print(i)
#     if i % 5 ==0:
#         print('Fizz')
#         continue
#     print(i)


# for x in range(0 , 100 + 1):
#     if x % 3 == 0:
#         print('Fizz')
#         continue
#     if x % 5 ==0:
#         print('Buzz')
#         continue
#     print(x)


# class Human:
#     def __init(self, name, age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# a1 = Human("ishaq")
# print(a1.name)


# class Father:
#    def __init__(self , name, age, gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
# class Mother:
#     def __init__(self , name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# class Son:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.father = Father("John", 40, "Male")
#         self.mother = Mother("Jane", 38, "Female")  

class Car:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model
    def drive(self):
        print("car is driving")
    def stop(self):
        print("car is braking")

car1 = Car("honda", "red", 2023)
car2 = Car("toyota", "green", 2020)

print(car2.name)
print(car1.model)