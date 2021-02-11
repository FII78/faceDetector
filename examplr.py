import cv2

trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img= cv2.imread("RD.jpg")
greyScaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Face Detector", greyScaled_img)
cv2.waitKey()

print("code compiled")