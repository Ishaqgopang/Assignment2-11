# class Parent:
#     def __init__(self, p_name, skin_color, hair_color):
#         self.p_name = p_name
#         self.skin_color = skin_color
#         self.hair_color = hair_color
# class Son(Parent):
#     def __init__(self, son_name)  -> None:
#         super().__init__ ("rahul", "black", "grey")
#         self.son_name = son_name
# s1= Son("Sudhir")
# print(s1.p_name)
# print(s1.son_name)

# class Parent:
#     def __init__(self, p_name, skin_color, hair_color):
#         self.p_name = p_name
#         self.skin_color = skin_color
#         self.hair_color = hair_color
# class Son(Parent):
#     def __init__(self,s_name):
#         super().__init__("Khan", "White", "Black")
#         self.s_name = s_name
# s1 = Son("Abdullah")
# print(s1.s_name)
# print(s1.p_name)
# print(s1.skin_color)
# print(s1.hair_color)

class Father:
    def __init__(self, f_name, skin_color, hair_color):
        self.f_name = f_name
        self.skin_color = skin_color
        self.hair_color = hair_color
class Son(Father):
    def __init__(self, s_name):
        super().__init__("khan", "white", "black")
        self.s_name = s_name
s1 = Son("Adil")
print(s1.s_name)
print(s1.f_name)
print(s1.skin_color)
print(s1.hair_color)