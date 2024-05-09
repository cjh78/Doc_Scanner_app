## Importing necessary packages ##

from functions import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argspace
import cv2 as cv
import imutils


## Contructing the Arg parser and parsing the arguments ##

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
args = vars(ap.parse_args())
