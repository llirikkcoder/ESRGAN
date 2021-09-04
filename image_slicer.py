import image_slicer
import shutil

image_slicer.slice('pic_rlt.png', 4)

#todo - сохранять в папку "to_cut_2"

newPath = shutil.move('pic_rlt_01_01.png', 'to_cut')
newPath = shutil.move('pic_rlt_01_02.png', 'to_cut')
newPath = shutil.move('pic_rlt_02_01.png', 'to_cut')
newPath = shutil.move('pic_rlt_02_02.png', 'to_cut')