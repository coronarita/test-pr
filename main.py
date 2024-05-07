# ch 5.2.1 main.py

import sys
from ui import View
from ctrl import Control
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    view = View()  # View 인스턴스
    Control(view=view)  # Control 인스턴스
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
