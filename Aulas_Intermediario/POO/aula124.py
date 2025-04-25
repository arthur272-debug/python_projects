# Revisando o conceito de manter estados dentro da classe


class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def iniciarFilmagem(self):
        if self.filmando:
            print(f"{self.nome} já está filmando")
            return

        print(f"{self.nome} está filmando")
        self.filmando = True

    def pararFilmagem(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando")
            return

        print(f"{self.nome} parou de filmar")
        self.filmando = False

    def tirarFoto(self):
        if self.filmando:
            print(f"{self.nome} não pode tirar foto enquanto está filmando")
            return

        print(f"{self.nome} tirou uma foto")


camera1 = Camera("Sony")
camera2 = Camera("Canon")
camera1.iniciarFilmagem()
camera1.tirarFoto()
camera1.pararFilmagem()
camera1.tirarFoto()
print("Câmera 1:", camera1.filmando)
print(camera2.filmando)
camera2.iniciarFilmagem()
camera2.tirarFoto()
