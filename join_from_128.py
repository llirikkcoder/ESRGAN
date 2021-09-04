from __future__ import print_function
import os
from PIL import Image
import glob

path = 'to_scale_final_large/'
files = [path + 'pic_rlt_01_01_01_01_rlt_rlt.png', path + 'pic_rlt_01_01_02_01_rlt_rlt.png', path + 'pic_rlt_01_01_01_02_rlt_rlt.png',   path + 'pic_rlt_01_01_02_02_rlt_rlt.png']
im = Image.open(path + 'pic_rlt_01_01_01_01_rlt_rlt.png')
width, height = im.size

result = Image.new("RGB", (width*2, height*2))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((width, height), Image.ANTIALIAS)
  x = index // 2 * width
  y = index % 2 * height
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))
  

result.save(os.path.expanduser('image_1.png'))
im.close()

#//////////////////////////////////////////////

path = 'to_scale_final_large/'
files = [path + 'pic_rlt_01_02_01_01_rlt_rlt.png', path + 'pic_rlt_01_02_02_01_rlt_rlt.png', path + 'pic_rlt_01_02_01_02_rlt_rlt.png',   path + 'pic_rlt_01_02_02_02_rlt_rlt.png']
im = Image.open(path + 'pic_rlt_01_02_01_01_rlt_rlt.png')
width, height = im.size

result = Image.new("RGB", (width*2, height*2))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((width, height), Image.ANTIALIAS)
  x = index // 2 * width
  y = index % 2 * height
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('image_2.png'))
im.close()

#//////////////////////////////////////////////

path = 'to_scale_final_large/'
files = [path + 'pic_rlt_02_01_01_01_rlt_rlt.png', path + 'pic_rlt_02_01_02_01_rlt_rlt.png', path + 'pic_rlt_02_01_01_02_rlt_rlt.png',   path + 'pic_rlt_02_01_02_02_rlt_rlt.png']

im = Image.open(path + 'pic_rlt_02_01_01_01_rlt_rlt.png')
width, height = im.size

result = Image.new("RGB", (width*2, height*2))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((width, height), Image.ANTIALIAS)
  x = index // 2 * width
  y = index % 2 * height
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('image_3.png'))
im.close()

#//////////////////////////////////////////////

path = 'to_scale_final_large/'
files = [path + 'pic_rlt_02_02_01_01_rlt_rlt.png', path + 'pic_rlt_02_02_02_01_rlt_rlt.png', path + 'pic_rlt_02_02_01_02_rlt_rlt.png',   path + 'pic_rlt_02_02_02_02_rlt_rlt.png']

im = Image.open(path + 'pic_rlt_02_02_01_01_rlt_rlt.png')
width, height = im.size

result = Image.new("RGB", (width*2, height*2))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((width, height), Image.ANTIALIAS)
  x = index // 2 * width
  y = index % 2 * height
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('image_4.png'))
im.close()

#//////////////////////////////////////////////

# path = 'to_scale_final/'
files = ['image_1.png', 'image_3.png', 'image_2.png',   'image_4.png']

im = Image.open('image_1.png')
width, height = im.size

result = Image.new("RGB", (width*2, height*2))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((width, height), Image.ANTIALIAS)
  x = index // 2 * width
  y = index % 2 * height
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('image_final.png'))
im.close()
path = 'to_scale_final/'


