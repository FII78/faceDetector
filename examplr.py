import cv2

trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img= cv2.imread("RD.jpg")
webcam=cv2.VideoCapture(0) #0 means from webcam by default

while True:
    successful_frame_read,frame=webcam.read()

    greyScaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coordinates=trained_face_data.detectMultiScale(greyScaled_img)
    # print(face_coordinates)

    # cv2.rectangle(img,(77,98),(233+77,233+98),(0,255,0),2)

    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)


    cv2.imshow("Face Detector", frame)
    key= cv2.waitKey(1)

    if key==81 or key==113:
        break
webcam.release()

print("code compiled")    