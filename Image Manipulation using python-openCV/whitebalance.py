import cv2
image=cv2.imread("crop1.jpg")
image1=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
image2=cv2.cvtColor(image,cv2.COLOR_RGB2YUV)
image3=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
cv2.imshow("newimage0",image)
cv2.imshow("newimage",image1)
cv2.imshow("newimage1",image2)
cv2.imshow("newimage2",image3)
cv2.waitKey(0)
cv2.destroyAllWindows()

