import qrcode

link = input("QR koduna dönüştürülecek linki giriniz: ")

filename = input("QR kodun kaydedilmesini istediğiniz adı giriniz: ")

if ".png" not in filename:
    filename += ".png"

img = qrcode.make(link)
img.save(filename)
print(f"{filename} olarak kaydedildi.")