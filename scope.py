x= "global x"

def function():
    # x= "local x"
    print(x)

function()
print(x)

name= "ibrahim"

def changeName(new_name):
    global name
    name= new_name
    print(name)

changeName("Ada")
print(name)