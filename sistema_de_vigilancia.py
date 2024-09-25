from ultralytics import YOLO
import cv2 as cv
import time

# Importando o modelo yolov8n.pt (nano)
modelo = YOLO('./classificadores/yolov8n.pt')
video = cv.VideoCapture('./videos/aeroporto.mp4')

# Inicializar a contagem de FPS
tempo_inicio = time.time()

# Contador de frames
contador_frames = 0

# Faz um looping nos frames do vídeo
while video.isOpened():
    rect, frame = video.read()
    if rect:
        contador_frames += 1  # Incrementa o contador de frames

        # Reduzindo o tamanho da janela
        frame_reduzido = cv.resize(frame, (900, 600), interpolation=cv.INTER_LINEAR)

        # Realizando a deteção de pessoas
        previsao = modelo(frame_reduzido, verbose=False, classes=[0])
        caixas = previsao[0].boxes

        # Desenhando os contornos
        for caixa in caixas:
            left, top, right, bottom = caixa.xyxy[0].int().tolist()
            cv.rectangle(frame_reduzido, (left, top), (right, bottom), (255, 0, 0), 2)

        # Calculando e mostrando os FPS
        tempo_atual = time.time()
        fps = contador_frames / (tempo_atual - tempo_inicio)  # FPS baseado no tempo decorrido
        cv.putText(frame_reduzido, f'FPS: {fps:.2f}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Apresentando os frames
        cv.imshow('Sistema de Vigilancia', frame_reduzido)

        # Pressione "q" para fechar
        if cv.waitKey(1) & 0xFF == ord('q'):  # Reduzido o tempo de espera para acelerar o vídeo
            break
    else:
        break

# Fechando todas as janelas
video.release()
cv.destroyAllWindows()
