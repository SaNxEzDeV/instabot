import os
from glob import glob
import rafael_config

pics = sorted([
    os.path.basename(x) for x in glob(rafael_config.PICS_PATH + "/*.jpg")
])
print('Pics under: ' + rafael_config.PICS_PATH)

for pic in pics:
    print(pic)