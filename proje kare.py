import cv2
import numpy as np
from tkinter import *
from PIL import Image
from PIL import ImageTk
import threading
import time

def rectangle_detector(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200)

    contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            if 0.8 <= ar <= 1.2:
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
                cv2.putText(frame, f"W:{w}, H:{h}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    return frame

def video_loop():
    global panel
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image = rectangle_detector(frame)
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        if panel is None:
            panel = Label(image=image)
            panel.image = image
            panel.pack(side="bottom", padx=10, pady=10)
        else:
            panel.configure(image=image)
            panel.image = image

    cap.release()
    cv2.destroyAllWindows()

root = Tk()
panel = None
thread = threading.Thread(target=video_loop)
thread.start()
root.mainloop()
