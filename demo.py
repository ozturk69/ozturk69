yazili1= float(input("1.yazılı: "))
yazili2= float(input("2.yazılı: "))
sozlu= float(input("sözlü: "))
ortalama=(yazili1 + yazili2 + sozlu)/3

if(ortalama>=0) and (ortalama<25):
     print(f"ortalamanız: {ortalama} Notunuz:0 Kaldınız") 
if(ortalama>=25) and (ortalama<45):
     print(f"ortalamanız {ortalama} Notunuz:1 Kaldınız")
if(ortalama>=45) and (ortalama<55):
     print(f"ortalamanız {ortalama} Notunuz:2 Kaldınız")
if(ortalama>=55) and (ortalama<70):
     print(f"ortalamanız {ortalama} Notunuz:3 Şartlı geçtiniz")
if(ortalama>=70) and (ortalama<85):
     print(f"ortalamanız {ortalama} Notunuz:4 Geçtiniz")
if(ortalama>=85) and (ortalama<=100):
     print(f"ortalamanız {ortalama} Notunuz:5 Geçtiniz")