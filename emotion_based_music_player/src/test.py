import cv2
import imutils

cap = cv2.VideoCapture(0)

img = cv2.imread("happy.png")
    

while True:
    ret,frame = cap.read()
    
    cv2.imshow("win",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
