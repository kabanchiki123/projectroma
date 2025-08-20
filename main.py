from PyQt6.QtWidgets import *
import requests
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
persha_valuta_lbl = QLabel("Перша валюта")
druga_valuta_lbl = QLabel("Друга валюта")

polevalut2 = QLineEdit()

main_line.addLayout(h1)
h1.addWidget(persha_valuta_lbl)
h1.addWidget(persha_valuta)
main_line.addWidget(polevalut)
persha_valuta.addItems(["USD", "UAH","EUR","PLN","CNY", "GBP", "CAD" ])

main_line.addLayout(h2)
h2.addWidget(druga_valuta_lbl)
h2.addWidget(druga_valuta)
main_line.addWidget(polevalut2)
druga_valuta.addItems(["USD", "UAH","EUR","PLN","CNY", "GBP", "CAD" ])

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

def func():
    count1 = polevalut.text()



    val1 = persha_valuta.currentText()
    val2 = druga_valuta.currentText()
    if val1 != "UAH":
        response = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val1}&json")
        rate1 = response.json()[0]["rate"]
    else:
        rate1 = 1

    if val2 != "UAH":

        response2 = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val2}&json")
        rate2 = response2.json()[0]["rate"]

    else:
        rate2 = 1


    result = rate1 / rate2 *int(count1)
    polevalut2.setText(str(result))


dorivnye_btn.clicked.connect(func)


window.setStyleSheet("""
    /* QPushButton */
    QPushButton {
        background-color: #3498db;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
    QPushButton:pressed {
        background-color: #1c6ca3;
    }

    /* QLineEdit */
    QLineEdit {
        border: 2px solid #ccc;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 18px;
        background-color: #f9f9f9;
        color: #333;
    }
    QLineEdit:focus {
        border: 2px solid #3498db;
        background-color: #ffffff;
    }

    /* QComboBox */
    QComboBox {
        border: 2px solid #ccc;
        border-radius: 8px;
        padding: 6px 12px;
        font-size: 16px;
        background-color: #f0f0f0;
        color: #333;
    }
    QComboBox:hover {
        border: 2px solid #3498db;
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 30px;
        border-left: 1px solid #aaa;
        background-color: #d0d0d0;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
    }
    QComboBox::down-arrow {
        image: url(:/qt-project.org/styles/commonstyle/images/arrowdown-16.png);
        width: 12px;
        height: 12px;
    }

    /* QLabel */
    QLabel {
        font-size: 17px;
        font-weight: bold;
        color: #2c3e50;
        padding: 4px;
    }
""")






window.show()
app.exec()