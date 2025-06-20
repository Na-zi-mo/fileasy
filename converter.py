from PIL import Image

file = "th-3612395174"

img = Image.open(f"{file}.jpg")
img.convert("RGB").save(f"./runs/{file}.pdf")


def jpg_to_pdf():
    print('done')
