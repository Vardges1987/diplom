import os
from PIL import Image

img = Image.open('C:/Users/hp/Desktop/pzzl/static/logo.png')

output_dir = 'C:/Users/hp/Desktop/pzzl/static/images/'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

width, height = img.size

part_width = width // 4
part_height = height // 4

for i in range(4):
    for j in range(4):
        left = i * part_width
        top = j * part_height
        right = left + part_width
        bottom = top + part_height

        part = img.crop((left, top, right, bottom))

        part.save(f'{output_dir}/logo-part-{i * 4 + j + 1}.png')
