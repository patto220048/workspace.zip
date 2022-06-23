import os

path ='./mnist_mini_1000/'

files = os.listdir(path)
for file in files:
     if 'num4' in file:
          print(file)