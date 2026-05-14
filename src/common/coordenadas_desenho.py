import cv2

class Desenho():

    def extraiCoordenadas(self, nome_imagem: str):

        #img = cv2.imread(f"../../data/imagens/{nome_imagem}") # Utilizar esse path quando rodar ESSE arquivo
        img = cv2.imread(f"data/imagens/{nome_imagem}")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_LIST,
            cv2.CHAIN_APPROX_NONE
        )

        return contours

    def redesenhaImagem(self,nome_imagem: str, coordenadas):
        #img = cv2.imread(f"../../data/imagens/{nome_imagem}") # Utilizar esse path quando rodar ESSE arquivo
        img = cv2.imread(f"data/imagens/{nome_imagem}")


        for contour in coordenadas:
            for point in contour:
                x, y = point[0]
                cv2.circle(img, (x, y), 1, (0, 0, 255), -1)

        #cv2.imwrite(f"../../data/imagens_geradas/{nome_imagem.split('.')[0]}_gerado.png",img) # Utilizar esse path quando rodar ESSE arquivo
        cv2.imwrite(f"data/imagens_geradas/{nome_imagem.split('.')[0]}_gerado.png",img)


    def calcula_limites_pixel(self, coordenadas):
        xs = []
        ys = []

        for contour in coordenadas:
            for point in contour:
                x, y = point[0]
                xs.append(x)
                ys.append(y)

        return min(xs), max(xs), min(ys), max(ys)


    def pixel_para_real(self, coordenadas, largura_real_cm):
        x_min, x_max, y_min, y_max = self.calcula_limites_pixel(coordenadas)

        largura_px = x_max - x_min
        escala = largura_real_cm / largura_px

        coordenadas_reais = []

        for contour in coordenadas:
            novo_contorno = []

            for point in contour:
                x_px, y_px = point[0]

                x_real = round((x_px - x_min) * escala,2)
                y_real = round((y_px - y_min) * escala,2)

                novo_contorno.append((x_real, y_real))

            coordenadas_reais.append(novo_contorno)

        return coordenadas_reais

if __name__ == "__main__":

    classe = Desenho()
    contours = classe.extraiCoordenadas("cachorro.png")
    classe.redesenhaImagem("cachorro.png", contours)
    for contour in contours:
        for point in contour:
            x, y = point[0]
            print(x, y)

    xsmin,xsmax, ysmin,ysmax = classe.calcula_limites_pixel(contours)
    coordenadas_reais = classe.pixel_para_real(contours, 100)