from PyQt6.QtWidgets import *

app = QApplication([])


window = QWidget()
window.resize(800, 600)

main_line = QHBoxLayout()



window.setLayout(main_line)


window.show()
app.exec()