class Dokon:
    def __init__(self):
        self.__mahsulotlar = []

    def mahsulot_qoshish(self, mahsulot):
        self.__mahsulotlar.append(mahsulot)
        print(f"Dokonga {mahsulot} qo'shildi")

    def umumiy_qiymat(self):
        summa = 0
        for mah in self.__mahsulotlar:
            summa += mah.narx * mah.miqdor
        print(f"Umumiy qiymat: {summa}")

    def maxsulotlar_royxati(self):
        for mah in self.__mahsulotlar:
            print(mah)

