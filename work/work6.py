import os
import numpy as np
from PIL import Image

path ='./mnist_mini_1000/'

files = os.listdir(path)

for file in files:
     if 'num4' in file:
         print (file)
         img=Image.open(path+file)
         imgArray = np.array(img)
         print(imgArray)