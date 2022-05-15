import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=pkMIkNMV76c")
img.save("MoonKnight.jpg")