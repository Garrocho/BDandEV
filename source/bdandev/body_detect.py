"""
Modulo que processa imagem da camera e detecta corpos.
"""

import settings
import cv2.cv as cv


def detectar_corpos(imagem, cascade):
    """
    Detecta corpos em uma determinada imagem de acordo com o cascade.
    """
    # Criando imagens temporarias.
    imagem_cinza = cv.CreateImage((imagem.width, imagem.height), 8, 1)
    imagem_pequena = cv.CreateImage((cv.Round(imagem.width / 2), cv.Round(imagem.height / 2)), 8, 1)

    # Converte a imagem em tons de cinza.
    cv.CvtColor(imagem, imagem_cinza, cv.CV_BGR2GRAY)

    # Redimensiona imagem para um rapido processamento.
    cv.Resize(imagem_cinza, imagem_pequena, cv.CV_INTER_LINEAR)
    cv.EqualizeHist(imagem_pequena, imagem_pequena)

    return cv.HaarDetectObjects(imagem_pequena, cascade, cv.CreateMemStorage(0))


def colorir(imagem, corpos_detectados):
    """
    Desenha um retangulo ao retor de um corpo.
    """
    for ((x, y, w, h), n) in corpos_detectados:
        pt1 = (int(x * 2), int(y * 2))
        pt2 = (int((x + w) * 2), int((y + h) * 2))
        cv.Rectangle(imagem, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
    return imagem


def escreve_texto(imagem, texto):
    """
    Escreve um texto em uma imagem.
    """
    fonte = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 2, 8)
    cv.PutText(imagem, texto, (25,30), fonte, 0)
    return imagem


if __name__ == '__main__':
    """
    Carrega o cascade e captura a camera para obter a imagem atual.
    """
    cascade = cv.Load(settings.CORPO_INTEIRO)
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
                imagem = escreve_texto(imagem, "Corpo Detectado")
            else:
                imagem = escreve_texto(imagem, "Nenhum Corpo Detectado")
            cv.ShowImage("BDandEV", imagem)
       
        c = cv.WaitKey(1)
        if c == 27:
            break

    cv.DestroyWindow("BDandEV")
