import os

path ='./mnist_mini_1000/'

files = os.listdir(path)
numOfNum4File=0
for file in files:
     if 'num4' in file:
         numOfNum4File+=1
print('Num4File : ',numOfNum4File)