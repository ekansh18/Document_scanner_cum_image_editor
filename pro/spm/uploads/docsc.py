import cv2

def scan(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray= cv2.GaussianBlur(gray, (5,5), 0)
    edged=cv2.Canny(gray, 75, 200)
    
    cnts=cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    cnts=sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    
    for c in cnts:
        peri=cv2.arcLength(c, True)
        approx=cv2.approxPolyDP(c, 0.02*peri, True)
        if len(approx)==4:
            screenCnt=approx
            break
    warped=four_point_transform()    