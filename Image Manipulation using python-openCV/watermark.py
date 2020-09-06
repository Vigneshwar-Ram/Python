import cv2
import numpy as np
image = cv2.imread("crop.jpg")
src = np.zeros(image.shape, image1.dtype)
height, width = image.shape[:2]
alpha = 0.3
namestamp = "ReelGraphy"
cv2.putText(image1, namestamp.format(alpha), (width-400, height-24), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,255,255), thickness=2)
cv2.addWeighted(image1, alpha, output, 1 - alpha, 0, output)
cv2.imshow(image1)
cv2.imwrite("stamped.jpg", output)
