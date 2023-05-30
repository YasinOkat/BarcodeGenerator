import os
import barcode
from PIL import Image, ImageDraw, ImageFont
from barcode.writer import ImageWriter

background_width = 750
background_height = 500
scaling_factor = 1.8

barcode.base.Barcode.default_writer_options['write_text'] = True
directory = os.getcwd()
itibaren = int(input("Kaçtan?\n"))
kadar = int(input("Kaça?\n"))
fontpath = directory + "/" + "bin" + "/" + "/LiberationSans-Regular.ttf"
barcode_folder = os.path.join(directory, 'barcode')

for i in range(itibaren, kadar + 1):
    options = {
        'dpi': 200,
        'module_height': 40,
        'module_width': 1.3,
        'text_distance': 8,
        'font_size': 20,
    }
    code = barcode.get('code128', str(i), writer=ImageWriter())

    barcode_image = code.render(writer_options=options)
    barcode_width, barcode_height = barcode_image.size

    background_image = Image.open(directory + "/" + "bin" + "/" + "background.png")
    draw = ImageDraw.Draw(background_image)
    font = ImageFont.truetype(fontpath, 40)
    x_coord = int((background_width - barcode_width) / 2)
    y_coord = int((background_height - barcode_height) / 2)

    pos = (x_coord, y_coord)
    background_image.paste(barcode_image, pos)

    filename = os.path.join(barcode_folder, f'barcode_{i}.png')
    background_image.save(filename)
    print(f'barcode_{i}.png' + " kaydedildi")

print("\nBitti")
