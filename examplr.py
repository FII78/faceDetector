import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
trained_face_data=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img= cv2.imread("RD.jpg")
# adding the pc's webcam to capture video
webcam=cv2.VideoCapture(0) #0 means from webcam by default

#Iterate forever over frames
while True:
    # Read the current frame
    successful_frame_read,frame=webcam.read()

    # Must convert to grayscale
    greyScaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates=trained_face_data.detectMultiScale(greyScaled_img)

    # Draw rectangles around the faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)


    cv2.imshow("Face Detector", frame)
    key= cv2.waitKey(1)

    # Stop if Q is pressed
    if key==81 or key==113:
        break
webcam.release()

print("code compiled")    