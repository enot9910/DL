from model import *
from data import *
import cv2
import numpy as np

testGene = testGenerator("data/membrane/test")
new_model = load_model('model.hdf5')
results = new_model.predict_generator(testGene, 5, verbose=1)
saveResult("data/membrane/test", results)

img1 = cv2.imread('data/membrane/test/' + str(1) + '_predict.png')
img2 = cv2.imread('test_im/' + str(1) + '_test.png')
difference = cv2.subtract(img1, img2)

#MAE = np.sum(np.abs(np.subtract(img1,img2,dtype=np.float))) / img1.shape[0]
MAE = np.sum(difference != 0) / img1.shape[0]

if MAE < 0.05:
	print("Test passed")
else:
	print("Test failed")
print("MAE: ", MAE)
