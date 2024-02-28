from PIL import Image, ImageChops

SOURSE_DIR = 'images/'


"""
#-------------------------------------------- Дзеркальне відображення
pict1 = Image.open(SOURSE_DIR+'5.jpg')
ava = pict1.crop((0, 0, pict1.width, pict1.height)).resize((700, 700)).transpose(Image.FLIP_LEFT_RIGHT)
ava.save(SOURSE_DIR+'ava.jpg')
ava.show()"""

first = Image.open(SOURSE_DIR+'2.jpg')
back = Image.open(SOURSE_DIR+'3.jpg')
r, g, b = first.split()

"""
r.show()
g.show()
b.show()
"""
#--------------------------------------------------------- Нашарування
mask_temp = g.point(lambda x: (70 < x < 140) and 255)
mask = ImageChops.invert(mask_temp)
new_first = Image.composite(first, back, mask)
new_first.show()
