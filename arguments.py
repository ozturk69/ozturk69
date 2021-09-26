# def add(*params):
#     sum=0
#     for n in params:
#         sum= sum + n
#     return sum
# print(add(10,20,30,50,60,20))

def displayUser(**args):
    for key, value in args.items():
        print("{} is {}".format(key, value))

displayUser(name= "ibos", age=26, city="Bayburt")
displayUser(name= "İbrahim", age=35, city="istanbul", phone= "123456")
displayUser(name="Ahmet", age=22, city="Ankara", phone="1234567", email= "ahmet@gmail.com")
