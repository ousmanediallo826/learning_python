from PIL import Image, ImageFilter
import sys
import os

image_folder = sys.argv[1]
output_folder = sys.argv[2]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# for filename in os.listdir(image_folder):
#     img = Image.open(f"{image_folder}/{filename}")
#
#     clean_img = os.path.splitext(filename)[0]
#     img.save(f"{output_folder}/{clean_img}.png")
# print("all done")


# for filename in os.listdir(image_folder):
#     img = Image.open(os.path.join(image_folder, filename))
#     converted_img = img.convert('L')
#     converted_img.save(f"{output_folder}/{filename}")
#
# print('done')

for filename in os.listdir(image_folder):
    img = Image.open(os.path.join(image_folder, filename))
    resized_img = img.resize((56, 56))
    resized_img.save(f"{output_folder}/{filename}")
    print("all done")
