from PyQt6.QtWidgets import *

app = QApplication([])


window = QWidget()
window.resize(450, 600)

main_line = QVBoxLayout()

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
h5 = QHBoxLayout()
h6 = QHBoxLayout()
h7 = QHBoxLayout()

persha_valuta = QComboBox()
druga_valuta = QComboBox()

deletvse_btn = QPushButton("C")
delet_btn = QPushButton("<-")
swipe_btn = QPushButton("^")
dilutu_btn = QPushButton(":")
mnoshutu_btn = QPushButton("x")
vidnatu_btn = QPushButton("-")
dodatu_btn = QPushButton("+")
dorivnye_btn = QPushButton("=")
one_btn = QPushButton("1")
two_btn = QPushButton("2")
three_btn = QPushButton("3")
four_btn = QPushButton("4")
five_btn =QPushButton("5")
six_btn = QPushButton("6")
seven_btn = QPushButton("7")
eight_btn = QPushButton("8")
nine_btn = QPushButton("9")
zero_btn = QPushButton("0")
koma_btn = QPushButton(",")
vidcotok_btn = QPushButton("%")

polevalut = QLineEdit()
persha_valuta_lbl = QLabel("перша валюта")
druga_valuta_lbl = QLabel("друга валюта")

polevalut2 = QLineEdit()

main_line.addLayout(h1)
h1.addWidget(persha_valuta_lbl)
h1.addWidget(persha_valuta)
main_line.addWidget(polevalut)
persha_valuta.addItems(["USD ", "UAH","EUR","PLN","CNY", "GBP", "CAD" ])

main_line.addLayout(h2)
h2.addWidget(druga_valuta_lbl)
h2.addWidget(druga_valuta)
main_line.addWidget(polevalut2)
druga_valuta.addItems(["USD ", "UAH","EUR","PLN","CNY", "GBP", "CAD" ])

main_line.addLayout(h3)
h3.addWidget(deletvse_btn)
h3.addWidget(delet_btn)
h3.addWidget(swipe_btn)
h3.addWidget(dilutu_btn)

main_line.addLayout(h4)
h4.addWidget(one_btn)
h4.addWidget(two_btn)
h4.addWidget(three_btn)
h4.addWidget(mnoshutu_btn)

main_line.addLayout(h5)
h5.addWidget(four_btn)
h5.addWidget(five_btn)
h5.addWidget(six_btn)
h5.addWidget(vidnatu_btn)

main_line.addLayout(h6)
h6.addWidget(seven_btn)
h6.addWidget(eight_btn)
h6.addWidget(nine_btn)
h6.addWidget(dodatu_btn)

main_line.addLayout(h7)
h7.addWidget(zero_btn)
h7.addWidget(koma_btn)
h7.addWidget(vidcotok_btn)
h7.addWidget(dorivnye_btn)

window.setLayout(main_line)

window.show()
app.exec()