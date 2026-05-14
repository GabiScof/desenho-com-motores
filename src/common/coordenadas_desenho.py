import cv2

class Desenho():

    def extraiCoordenadas(self, nome_imagem: str):

        img = cv2.imread(f"../../data/imagens/{nome_imagem}")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_LIST,
            cv2.CHAIN_APPROX_NONE
        )

        return contours

    def redesenhaImagem(self,nome_imagem: str, coordenadas):
        img = cv2.imread(f"../../data/imagens/{nome_imagem}")

        for contour in coordenadas:
            for point in contour:
                x, y = point[0]
                cv2.circle(img, (x, y), 1, (0, 0, 255), -1)

        cv2.imwrite(f"../../data/imagens_geradas/{nome_imagem.split('.')[0]}_gerado.png",img)

if __name__ == "__main__":

    classe = Desenho()
    contours = classe.extraiCoordenadas("cachorro.png")
    classe.redesenhaImagem("cachorro.png", contours)
    for contour in contours:
        for point in contour:
            x, y = point[0]
            print(x, y)