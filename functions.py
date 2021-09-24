def sayHello (name="user"):
    return "Hello" + name

msg= sayHello("ibos")
msg= sayHello("ibrahim")
print(msg)

def total (num1,num2):
    return num1+num2
result= total(10,20)
result= total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2021-dogumYili
ageibos= yasHesapla(1995)
ageibrahim= yasHesapla(1985)
ageismail= yasHesapla(2000)
print(ageibos, ageibrahim, ageismail)

def EmekliligeKacYilKaldi(dogumYili, isim):
    yas= yasHesapla(dogumYili)
    emeklilik= 65-yas

    if emeklilik >0:
        print(f"emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz.")
EmekliligeKacYilKaldi(1983, "Ali")
EmekliligeKacYilKaldi(1975, "Ahmet")
EmekliligeKacYilKaldi(1969, "Mehmet")

