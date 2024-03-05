import os
import time

print("\n✨ https://github.com/merenyprkc")
print("🪄 Programı kapatmak isterseniz terminale tıklayıp CTRL+C tuşlarına aynı anda basın.")

while True:
    saat = int(input("💻 Bilgisayarınızın kaç saat sonra kapatılmasını istersiniz?: "))
    while True:
        dakika = int(input("\n💻 Bilgisayarınızın kaç dakika sonra kapatılmasını istersiniz?: "))
        if(dakika > 60 or dakika < 0):
            print("Dakika değeri maksimum 60, minimum 0 olmak zorundadır. Lütfen tekrar deneyin.")
        else:
            break

    while True:
        saniye = int(input("\n💻 Bilgisayarınızın kaç saniye sonra kapatılmasını istersiniz?: "))
        if(saniye > 60 or saniye < 0):
            print("Saniye değeri maksimum 60, minimum 0 olmak zorundadır. Lütfen tekrar deneyin.")
        else:
            break
    break

toplamSaniye = ((saat * 60) * 60) + (dakika * 60) + saniye

onay = input(f"\nBilgisayarınız {saat}:{dakika}:{saniye} [{toplamSaniye} saniye] sonra kapatılacak onaylıyor musunuz?: (Y/N)").upper()
if(onay == "Y"):
    time.sleep(toplamSaniye)
    os.system("shutdown /s /t 1")
else:
    print("Oh, görüşmek üzere o halde.")