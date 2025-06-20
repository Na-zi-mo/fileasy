from PIL import Image
# import pdf2image

def jpg_to_pdf(input_file, output_file):
    img = Image.open(input_file)
    img.convert("RGB").save(output_file)

    print('done')
