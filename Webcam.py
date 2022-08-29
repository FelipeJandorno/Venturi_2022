import cv2 as cv

def Leitura_Webcam():
    webcam = cv.VideoCapture(0)                     #Conecta o python com a webcam

    if webcam.isOpened():                           #Nos informa se a conexão foi bem sucedida
        validacao, frame = webcam.read()

        while validacao:
            validacao, frame = webcam.read()        #Leitura infinita dos frames retornados pela webcam
            cv.imshow("Video da Webcam", frame)     #imprime os frames da câmera na tela
            key = cv.waitKey(1)                     #Deixa o frame exposto por um determinado período de tempo

            if key == 27:                           #Ao apertar ESC a tela é fechada
                break

        cv.imwrite("Foto_QR_code.png", frame)

    webcam.release()                                #Finaliza a conexão com a webcam
    cv.destroyAllWindows()                          #Fecha todas as janelas abertas
