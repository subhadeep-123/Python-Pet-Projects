import sys
import os
from PIL import Image

# check is new/ exixts if not create a new one
if not os.path.exists(sys.argv[2]):
    os.mkdir(sys.argv[2])

# loop through the pokedex and grab all files to make them .jpg
for files in os.listdir(sys.argv[1]):
    img = Image.open(f'{sys.argv[1]}{files}')
    clean_name = os.path.splitext(files)[0]
    img.save(f'{sys.argv[2]}{clean_name}.png', 'png')
    print('all done!!')
