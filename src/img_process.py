import rospy
from std_msgs.msg import String
import numpy as np
import cv2 as cv

def img_process():
   #open the picture
    img = cv.imread('pic_test/1.jpg')
   
   #image size
    print img.shape
    #wait a key & exit
    cv.imshow('img_raw',img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ =='__main__':
    img_process()