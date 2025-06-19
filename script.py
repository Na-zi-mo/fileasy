from PIL import Image

file = "passport_visa"

img = Image.open(f"{file}.jpg")
img.convert("RGB").save(f"{file}.pdf")
