import cv2
import os

root = os.path.dirname(os.path.abspath(__file__))

hercescad =os.path.join(root, "haarcascade_russian_plate_number.xml")

cap = cv2.VideoCapture(1)

while True:
    succes, img= cap.read()
    
    plate_cascade = cv2.CascadeClassifier(hercescad)
    
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    plates = plate_cascade.detectMultiScale(img_gray,1.1,4)
    
    for (x,y,w,h) in plates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
    
    cv2.imshow("car Plate",img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()