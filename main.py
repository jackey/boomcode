# -*- coding:utf8 -*-

from PIL import Image 
from pytesser import pytesser
import os
import subprocess
import re

run_from_console = __name__ == '__main__'
img = Image.open('code.png')

imgry = img.convert('L')

table = []
threshold = 150

for i in range(256):
  if i < threshold:
    table.append(0)
  else:
    table.append(1)

out = imgry.point(table, '1')

fname = 'test.tiff'

out.save(fname, dpi=(72, 72))

tiff = Image.open(fname);

code = pytesser.image_to_string(tiff)

clean_code = re.sub(r'[^0-9a-zA-Z]', '', code)

print clean_code

os.remove(fname)


