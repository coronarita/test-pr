# ch 6.6.1 ui.py

## main.py의 Calculator 클래스에서 화면정의, 초기화, 에디트 화면처리 분리
# 거듭제곱 기능 연산자 추가

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QPlainTextEdit,
    QHBoxLayout,
    QLineEdit,
    QComboBox,
)

from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton("Calc", self)  # 버튼 이름 변경
        self.btn2 = QPushButton("Clear", self)

        self.le1 = QLineEdit("0", self)  # 라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        self.le1.setFocus(True)  # 포커스 설정
        self.le1.selectAll()  # 텍스트 전체 선택

        self.cb = QComboBox(self)
        self.cb.addItems(["+", "-", "*", "/", "^", "%"])  # %연산자 추가

        self.le2 = QLineEdit("0", self)  # 라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 공백
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()  # 수직 레이아웃
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)  # 빈 공간

        self.setLayout(vbox)  # 수직 배치 된 레이아웃 설정

        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(256, 256)
        self.show()

    def setDisplay(self, text):  # 메서드 이름 변경
        self.te1.appendPlainText(text)

    def clearMessage(self):
        self.te1.clear()
