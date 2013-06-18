"""
Este e o modulo que detecta um corpo.
"""

import cv2.cv as cv


def detectar_corpos(imagem, cascade):

    # Criando imagens temporarias.
    gray = cv.CreateImage((imagem.width, imagem.height), 8, 1)
    imagem_pequena = cv.CreateImage((cv.Round(imagem.width / 2), cv.Round(imagem.height / 2)), 8, 1)

    # Converte a imagem em tons de cinza.
    cv.CvtColor(imagem, gray, cv.CV_BGR2GRAY)

    # Redimensiona imagem para um rapido processamento.
    cv.Resize(gray, imagem_pequena, cv.CV_INTER_LINEAR)
    cv.EqualizeHist(imagem_pequena, imagem_pequena)

    return cv.HaarDetectObjects(imagem_pequena, cascade, cv.CreateMemStorage(0))


def colorir(imagem, corpos_detectados):
    for ((x, y, w, h), n) in corpos_detectados:
        pt1 = (int(x * 2), int(y * 2))
        pt2 = (int((x + w) * 2), int((y + h) * 2))
        cv.Rectangle(imagem, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
    return imagem


def escrever(imagem, texto):
    fonte = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 2, 8)
    cv.PutText(imagem, texto, (25,30), fonte, 0)
    return imagem


if __name__ == '__main__':

    cascade = cv.Load("../data/corpo_inteiro.xml")
    camera = cv.CreateCameraCapture(0)

    cv.NamedWindow("BDandEV", 1)

    while True:
        imagem = cv.QueryFrame(camera)
        if not imagem:
            print "WebCam Desligada"
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
