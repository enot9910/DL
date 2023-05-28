from model import *
from data import *
from PIL import Image
from imagehash import dhash


'''
testGene = testGenerator("data/membrane/test")
new_model1 = load_model('unet_membrane.hdf5')
results = new_model1.predict_generator(testGene, 5, verbose=1)
saveResult("data/membrane/test", results)
flag = True
for i in range(2):
    image1 = dhash(Image.open('data/membrane/test/' + str(i) + '_predict.png'))
    image2 = dhash(Image.open('test_im/' + str(i) + '_test.png'))
    if image1 != image2:
        flag = False
        break
if flag:
    print('Tests passed')
else:
    print('Something went wrong')
'''    
import os
os.environ["NPY_ALLOW_DEPRECATED_API"] = "1"
import cv2
import numpy as np

testGene = testGenerator("data/membrane/test")
new_model1 = load_model('new_model.hdf5')
results = new_model1.predict_generator(testGene, 5, verbose=1)
saveResult("data/membrane/test", results)

img1 = cv2.imread('data/membrane/test/' + str(1) + '_predict.png')
img2 = cv2.imread('test_im/' + str(1) + '_test.png')

# Computing the pixel-wise difference between the two images
difference = cv2.subtract(img1, img2)

# Computing image similarity (in percentages)
similarity = (np.sum(difference == 0) / difference.size) * 100

if similarity > 95:
	print("Test passed")
else:
	print("Test failed")
print("Image similarity: ", similarity, "%")
