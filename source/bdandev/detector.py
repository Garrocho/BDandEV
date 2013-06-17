# @author: Charles Tim Batista Garrocho
# @contact: charles.garrocho@gmail.com
# @copyright: (C) 2013 Python Software Open Source

"""
Este e o modulo que detecta um corpo.
"""

import cv2.cv as cv
from datetime import datetime

tamanho_menor = (20, 20)
escala_imagem = 2
escala_haar = 1.2
minimo_vizinhos = 2
bandeiras_haar = 0

def detectar_corpos(imagem, cascade):

    # Criando imagens temporarias.
    gray = cv.CreateImage((imagem.width, imagem.height), 8, 1)
    imagem_pequena = cv.CreateImage((cv.Round(imagem.width / escala_imagem), cv.Round(imagem.height / escala_imagem)), 8, 1)

    # Converte a imagem em tons de cinza.
    cv.CvtColor(imagem, gray, cv.CV_BGR2GRAY)

    # Redimensiona imagem para um rapido processamento.
    cv.Resize(gray, imagem_pequena, cv.CV_INTER_LINEAR)

    cv.EqualizeHist(imagem_pequena, imagem_pequena)

    return cv.HaarDetectObjects(imagem_pequena, cascade, cv.CreateMemStorage(0), escala_haar, minimo_vizinhos, bandeiras_haar, tamanho_menor)

    

if __name__ == '__main__':

    cascade = cv.Load("../data/todo_corpo.xml")
    camera = cv.CreateCameraCapture(0)

    cv.NamedWindow("BDandEV", 1)

    while True:
        imagem = cv.QueryFrame(camera)
        if not imagem:
            imagem = cv.CreateImage((640, 480), 8, 1)
            fonte = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)
            cv.Zero(imagem)
            cv.PutText(imagem, "WebCam Desligada...", (25, 30), fonte, 255)
            cv.ShowImage("BDandEV", imagem)
            break
        else:
            corpos_detectados = detectar_corpos(imagem, cascade)
            if corpos_detectados:
                imagem = colorir(imagem, corpos_detectados)
                imagem = escrever(imagem, "Corpo Detectado")
            else:
                imagem = escrever(imagem, "Nenhum Corpo Detectado")
        
        cv.ShowImage("BDandEV", imagem)
       
        c = cv.WaitKey(1)
        if c == 27:
            break

    cv.DestroyWindow("BDandEV")
