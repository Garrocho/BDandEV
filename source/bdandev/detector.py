# @author: Charles Tim Batista Garrocho
# @contact: charles.garrocho@gmail.com
# @copyright: (C) 2013 Python Software Open Source

"""
Este e o modulo que detecta um corpo.
"""

import cv2.cv as cv

camera = cv.CaptureFromCAM(0)
cascade = cv.Load("../data/todo_corpo.xml")

while True:
    imagem = cv.QueryFrame(camera)
    corpos_detectados = cv.HaarDetectObjects(imagem, cascade, cv.CreateMemStorage(), 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (0, 0) )
    
    for ((x,y,w,h), stub) in corpos_detectados:
        cv.Rectangle(imagem, (int(x), int(y)), (int(x) + w, int(y) + h), (0, 255, 0), 2, 0)

    cv.ShowImage("Janela", imagem)
    c = cv.WaitKey(1)
    if c == 27:
        break
