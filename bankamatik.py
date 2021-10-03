ibrahimHesap= {
    "ad": "İbrahim Öztürk",
    "hesapNo": "1234567",
    "bakiye": 4000,
    "ekHesap": 3000,
}

AliHesap= {
    "ad": "Ali Öztürk",
    "hesapNo": "9807654",
    "bakiye": 3500,
    "ekHesap": 2500,
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        print("Paranızı alabilirsiniz.")
    else:
        toplam= hesap["bakiye"] + hesap["ekHesap"]
        
        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == "e":
                print("Paranızı alabilirsiniz")

            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("Üzgünüz bakiyeniz yetersiz")

    
paraCek(AliHesap, 6005)