import qrcode

img = qrcode.make("Linkiniz")
img.save("QRCode.png")
print("QRCode.png olarak kaydedildi.")
