import cv2 as cv
import pytesseract
import os


def text_detection_and_extraction(path):
    pytesseract.pytesseract.tesseract_cmd = "tesseract"

    img = cv.imread(path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    
    return text

if __name__=='__main__':
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, "yolo_text.png")

    text = text_detection_and_extraction(path)
    print(text)

    file = open(root+"/recognized.txt", "w+t", )
    file.write(text)
    file.close()
