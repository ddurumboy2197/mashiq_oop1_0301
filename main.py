from  dokon import Dokon
from  maxsulot import Mahsulot

product1 = Mahsulot('Olma', 20000, 100)
product2 = Mahsulot('Anjir', 23000, 30)
product3 = Mahsulot('Olma', 37000, 50)

market = Dokon()
market.mahsulot_qoshish(product1)
market.mahsulot_qoshish(product2)
market.mahsulot_qoshish(product3)
market.maxsulotlar_royxati()

market.umumiy_qiymat()
