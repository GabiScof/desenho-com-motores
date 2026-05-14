from src.common.coordenadas_desenho import Desenho
from src.common.plotter import Plotter
from env import Env
import cv2
import serial
import time


desenho = Desenho()
Env = Env()

imagem = "cachorro.png"

img = cv2.imread(f"data/imagens/{imagem}")

coordenadas_pixel = desenho.extraiCoordenadas(nome_imagem="cachorro.png")
coordenadas_reais = desenho.pixel_para_real(coordenadas_pixel, largura_real_cm=20)

plotter = Plotter(distancia_motores=Env.DISTANCIA_MOTORES, raio_carretel=Env.RAIO_CARRETEL, passos_por_volta=200)

arduino = serial.Serial(Env.COM, 9600)
time.sleep(2)

posicao_atual = Env.POSICAO_INCIAL

for contour in coordenadas_reais:

    for ponto_destino in contour:

        passos_esq, passos_dir = plotter.calcula_passos_entre_pontos(posicao_atual, ponto_destino)

        mensagem = f"{passos_esq} {passos_dir}\n"

        arduino.write(mensagem.encode())

        print(f"Destino: {ponto_destino}")
        print(f"Enviado: {mensagem.strip()}")

        resposta = arduino.readline().decode().strip()
        print(f"Arduino: {resposta}")

        posicao_atual = ponto_destino

arduino.close()