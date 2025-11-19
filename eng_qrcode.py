import qrcode

img = qrcode.make("Your link")
img.save("QRCode.png")
print("Saved as QRCode.png")
