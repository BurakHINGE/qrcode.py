import qrcode

img = qrcode.make("Your link")
img.save("QRCode.png")
print("QRCode.png olarak kaydedildi.")
