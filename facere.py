import threading
import cv2
from deepface import DeepFace
from scipy.datasets import face


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_GIGA_FRAME_WIDTH_MAX , 600)
cam.set(cv2.CAP_PROP_GIGA_FRAME_HEIGH_MAX , 500)

count = 0 
face_match  = False

reference = cv2.imread("img\IMG_20240801_093457.jpg")

def check(frame):
    global face_match
    try:
        if DeepFace.verify(frame,reference.copy())['verified']:
              face_match = True
        else:
             face_match = False
    except ValueError:
         face_match = False         

while True:
    ret , frame  = cam.read()
    if ret :
        if count%30 == 0:
                try:
                     threading.Thread(target=check,args=(frame.copy(),)).start()
                except ValueError :
                     pass
        count+=1
        if face_match:
             cv2.putText(frame,"match",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
             cv2.putText(frame,"NO match",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
        cv2.imshow("video",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cv2.destroyAllWindows() 