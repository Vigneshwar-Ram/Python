import cv2
image=cv2.imread("crop1.jpg")
r=cv2.selectROI(image)
imCrop=image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv2.imshow("crpimg.jpg",imCrop)
cv2.imwrite("crpimg1.jpg",imCrop)
cv2.waitKey(0)
cv2.destroyAllWindows()
