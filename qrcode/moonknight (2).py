import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=pkMIkNMV76c")
img.save("MoonKnight.jpg")

img = qrcode.make("Ninja Hattori is eating Biryani")
img.save("NinjaHattori.jpg")

img = qrcode.make("https://www.youtube.com/watch?v=Oqrm-9Wy8iU&t=22s")
img.save("Auugg.jpg")

import cv2

d = cv2.QRCodeDetector()
d.detectAndDecode(cv2.imread("NinjaHattori.jpg"))
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("NinjaHattori.jpg"))

print(val)