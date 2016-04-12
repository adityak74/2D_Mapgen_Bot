import numpy as np
import cv2
import sys

try:
  if sys.argv[1]=='-noip':
    cap = cv2.VideoCapture(int(sys.argv[2]))
  elif sys.argv[1]=='-ip':
    print "Loading from Network Stream. Might take some time to Stream. Please wait"
    cap = cv2.VideoCapture("http://"+sys.argv[2])
except:
  cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(1)
gray_flag=0
edges_flag=0
face_detection_flag=0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while (True): #Capture frame - by - frame
  ret, frame = cap.read()

  # Our operations on the frame come here
  # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Display the resulting frame
  
  cur_frame = frame
  color = gray = frame
  k = cv2.waitKey(1)

  if k & 0xFF == ord('q'):
      print "Quit"
      break

  if k & 0xFF == ord('g'):
      gray_flag = 1
      face_detection_flag=0
      edges_flag=0

  if k & 0xFF == ord('c'):
      gray_flag = 0
      face_detection_flag=0
      edges_flag=0

  if k & 0xFF == ord('e'):
      edges_flag = 1
      face_detection_flag=0
      gray_flag=0

  if k & 0xFF == ord('f'):
      face_detection_flag = 1
      gray_flag=0
      edges_flag=0

  if k & 0xFF == ord('r'):
      gray_flag=0
      edges_flag=0
      face_detection_flag=0
      cur_frame = frame

  if gray_flag == 1:
      gray = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
      cur_frame = gray

  if edges_flag == 1:
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cur_frame = cv2.Canny(gray,100,200)

  if face_detection_flag == 1:
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      for (x,y,w,h) in faces:
        cv2.rectangle(cur_frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = cur_frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
  
  cv2.imshow("frame", cur_frame)




# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()