# import the cv2 library
import cv2
from matplotlib import pyplot as plt

def launching():
   grayscale('pic_gi.jpg')
   
   

   cv2.waitKey(0)
 

   cv2.destroyAllWindows()

 
def grayscale(image):
    img_grayscale = cv2.imread(image,0)

    histr = cv2.calcHist([img_grayscale],[0],None,[256],[0,256])
  

    height, width = img_grayscale.shape[:2]
    # get the center coordinates of the image to create rotation matrix
    center = (width/2, height/2)
 
    # using cv2.getRotationMatrix2D() to get the rotation matrix
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
 
    # rotate the image using cv2.warpAffine
    rotated_image = cv2.warpAffine(src=img_grayscale, M=rotate_matrix, dsize=(width, height))



    c=cv2.imshow('Original image', img_grayscale)
    e=cv2.imshow('Rotated image', rotated_image)
    edg(img_grayscale)

    return cv2.imshow('graycsale image',img_grayscale),c,e,

def edg(image):
    img_blur = cv2.GaussianBlur(image, (3,3), 0) 
 
    # Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    # Display Sobel Edge Detection Images
    f=cv2.imshow('Sobel X', sobelxy)
    return f
 
 
launching()


 
