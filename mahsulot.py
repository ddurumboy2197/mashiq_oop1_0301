class Mahsulot:
    def __init__(self, nom, narx, miqdor):
        self.nom = nom
        self.narx = narx
        self.miqdor = miqdor
    def __str__(self):
        return f"Mahsulot: {self.nom}-{self.narx}-{self.miqdor}"
