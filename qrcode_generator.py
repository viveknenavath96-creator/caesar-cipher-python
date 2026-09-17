import qrcode

data = input("ENTER THE TEXT OR LINK :")

image =qrcode.make(data)

image.save("img.png")

print(image)

