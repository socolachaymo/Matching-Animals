import os
from pygame import image, transform

big_matched = image.load('ending/matched.png')
small_matched = big_matched.copy()
matched = transform.scale(small_matched, (512,512))

congrats_1 = image.load('ending/congrats.png')
congrats = congrats_1.copy()
congrats = transform.scale(congrats, (512,512))

image_size = 128
screen_size = 512
num_tiles_side = 4
num_tiles_total = 16
margin = 4

asset_dir = 'assets'
asset_files = [x for x in os.listdir(asset_dir) if x[-3:] == 'png']

assert len(asset_files) == 8