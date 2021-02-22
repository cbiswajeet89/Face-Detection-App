import cv2

#Pre-trained faces
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#reading image
#img=cv2.imread('mypic.png')
#To capture video from webcam
webcam=cv2.VideoCapture(0, cv2.CAP_DSHOW)	# 0 value takes the default cam in the system

#Iteration over frames
while True:
	successful_frame_read, frame=webcam.read()

	#Converting the coloured img to grayscaled image
	grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	#Detect faces
	face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

	#Draw rectangle around the faces
	for (x,y,w,h) in face_coordinates:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

	#Draw rectangle around the eyes
	cv2.imshow('Face Detector',frame)
	key=cv2.waitKey(1)		#holding the image on screen for 1 milisecond

	#Stop if Q is pressed
	if key==81 or key==113:
		break
webcam.release()
	
#print(face_coordinates)

#showing the image
#cv2.imshow('Face Detector',img)
#cv2.waitKey()		#holding the image on screen