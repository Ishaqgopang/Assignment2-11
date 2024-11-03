# data = open("data.txt", "r")
# content = data.read()
# data.close()
# print(content)

# with open ("data.txt", "r") as file:
#     content = file.readline()
    
    
# print(content)

# a = 3
# b = 6
# try:
#     c = (a+b)/ (a-b)
#     print(c)
# except ZeroDivisionError as e:
#     print(e)

# print("Hello")


# print("Muhammad", " Ishaq", " Gopang", sep = " \u2764 ")    #Heart emoji code u2764

# print("Someone said \'Ali\' is a \'good\' boy' \n\t\tbut \nhe often makes mistakes")

# name = "Muhammad Ishaq"
# email = "ishaq.khan.gopang@gmail.com"
# print(f"My name is {name}, my email is {email}")

# print("\u2764")


# name = "Muhammad Ishaq"
# print(" \u2764 ".join(name) )



# name = "Muhammad Ishaq"
# li = list(name)
# li.pop()
# name2 = ("".join(li))
# print(name2)



marks = int(input("Enter Your Marks: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B+")
elif marks >= 70:
    print("B-")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")



