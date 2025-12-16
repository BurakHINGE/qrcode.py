import qrcode

link = input("Enter the link to be converted into a QR code: ")

filename = input("Enter the filename to save the QR code: ")

if ".png" not in filename:
    filename += ".png"

img = qrcode.make(link)
img.save(filename)

print(f"Saved as {filename}.")