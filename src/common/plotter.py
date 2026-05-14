import math

class Plotter():

    def __init__(self, distancia_motores: float, raio_carretel: float, passos_por_volta: int):
        self.distancia_motores = distancia_motores
        self.raio_carretel = raio_carretel
        self.passos_por_volta = passos_por_volta

    def calcula_comprimentos(self, x: float, y: float):
        l_esquerda = math.sqrt(x ** 2 + y ** 2)
        l_direita = math.sqrt((self.distancia_motores - x) ** 2 + y ** 2)

        return l_esquerda, l_direita

    def comprimento_para_passos(self, delta_comprimento: float, raio_carretel: float) -> int:
        passos_por_volta = 200
        comprimento_por_volta = 2 * math.pi * raio_carretel
        comprimento_por_passo = comprimento_por_volta / passos_por_volta
        passos = delta_comprimento / comprimento_por_passo

        return round(passos)

    def calcula_passos_entre_pontos(self, ponto_atual, ponto_destino):
        x_atual, y_atual = ponto_atual
        x_destino, y_destino = ponto_destino

        l1_atual, l2_atual = self.calcula_comprimentos(x_atual, y_atual)
        l1_destino, l2_destino = self.calcula_comprimentos(x_destino, y_destino)

        delta_l1 = l1_destino - l1_atual
        delta_l2 = l2_destino - l2_atual

        passos_l1 = self.comprimento_para_passos(delta_l1, self.raio_carretel)
        passos_l2 = self.comprimento_para_passos(delta_l2, self.raio_carretel)

        return passos_l1, passos_l2