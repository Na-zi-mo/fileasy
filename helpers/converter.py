from PIL import Image
from pathlib import Path
# import pdf2image

def jpg_to_pdf(input_file, output_file):
    img = Image.open(input_file)
    img.convert("RGB").save(output_file)

    print('done')

def images_to_pdf(images):
    for image in images:
        img = Image.open(image)
        path = Path(image)
        img.convert("RGB").save(path.rename(path.with_suffix('.pdf')))
