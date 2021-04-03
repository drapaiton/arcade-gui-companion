# import sys
#
# from PyQt5 import QtWidgets
# from dotenv import load_dotenv
#
# from src import Ui_MainWindow
#
# if __name__ == "__main__":
#     load_dotenv(override=True)
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

if __name__ == "__main__":
    from dotenv import load_dotenv
    from os import environ

    load_dotenv(override=True)
    print(environ["hey"])
