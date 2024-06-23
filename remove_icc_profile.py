from PIL import Image

def remove_icc_profile(image_path):
    image = Image.open(image_path)
    data = list(image.getdata())
    image_without_icc = Image.new(image.mode, image.size)
    image_without_icc.putdata(data)
    image_without_icc.save(image_path, format='PNG')

image_files = ['player.png', 'enemy.png', 'bullet.png', 'ufo.png', 'powerup.png']

for image_file in image_files:
    remove_icc_profile(image_file)

print("ICC profiles removed from images.")
