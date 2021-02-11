import cv2

trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img= cv2.imread("RD.jpg")
greyScaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_coordinates=trained_face_data.detectMultiScale(greyScaled_img)
print(face_coordinates)

cv2.rectangle(img,(77,98),(233+77,233+98),(0,255,0),2)

cv2.imshow("Face Detector", img)
cv2.waitKey()

print("code compiled")