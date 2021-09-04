import image_slicer
import glob
import os

test_img_folder = 'to_cut/*'

for path in glob.glob(test_img_folder):
    print(path)
    image_slicer.slice(path, 4)
    os.remove(path)