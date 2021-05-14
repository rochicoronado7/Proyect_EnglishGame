from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi 

import sys

class Proyect_EnglishGame (QMainWindow): #ventana principal
    def __init__(self):
        super(Proyect_EnglishGame , self).__init__()
        loadUi ('Proyect_EnglishGame.ui', self)
        self.button_play.clicked.connect(self.Open_Play_EnglishGame) #conectar al boton lo que va a hacer en la funcion
        #en este caso abre la ventana 2 de play
        self.button_exit.clicked.connect(self.exit) #cierra todo el juego
    
    def Open_Play_EnglishGame (self): #para abrir una ventana y cerrar la anterior
        self.hide()
        OtherWindow = Play_EnglishGame(self)
        OtherWindow.show()

    def exit (self):
        sys.exit ()  #para cerrar la aplicacion


class Play_EnglishGame (QMainWindow): #segunda ventana
    def __init__(self, parent=None):
        super(Play_EnglishGame, self).__init__(parent)
        loadUi ('Play_EnglishGame.ui', self)
        self.button_BackMenu.clicked.connect(self.Back_Menu1)
        self.button_Answer.clicked.connect(self.Answer_Text)
        self.button_Next.clicked.connect(self.Open_Play2_EnglishGame)

    def Open_Play2_EnglishGame (self): #para abrir una ventana y cerrar la anterior
        self.hide()
        OtherWindow2 = Play2_EnglishGame(self)
        OtherWindow2.show()

    def Answer_Text (self):
        Correct = str("It's Correct, Congrats!!")
        Wrong = str("It's Wrong, Sorry :(")
        if self.Option4.isChecked():
            self.CorrectOrWrong.setText(Correct)
        else:  #elif self.Option1isChecked == True or self.Option2.isChecked == True or self.Option3.isChecked == True 
            self.CorrectOrWrong.setText(Wrong)
            

    def Back_Menu1 (self):
        self.hide()
        MainMenu1 =  Proyect_EnglishGame()
        MainMenu1.show()
        self.parent().show()
        self.close()

class Play2_EnglishGame (QMainWindow): #segunda ventana
    def __init__(self, parent=None):
        super(Play2_EnglishGame, self).__init__(parent)
        loadUi ('Play2_EnglishGame.ui', self)
        self.button_BackMenu.clicked.connect(self.Back_Menu2)
        self.button_Answer.clicked.connect(self.Answer_Text)
        self.button_Next.clicked.connect(self.Open_Play3_EnglishGame)

    def Open_Play3_EnglishGame (self): #para abrir una ventana y cerrar la anterior
        self.hide()
        OtherWindow2 = Play3_EnglishGame(self)
        OtherWindow2.show()

    def Answer_Text (self):
        Correct = str("It's Correct, Congrats!!")
        Wrong = str("It's Wrong, Sorry :(")
        if self.Option2_2.isChecked():
            self.CorrectOrWrong2.setText(Correct)
        else:  #elif self.Option1isChecked == True or self.Option2.isChecked == True or self.Option3.isChecked == True 
            self.CorrectOrWrong2.setText(Wrong)
            
    def Back_Menu2 (self):
        self.hide()
        MainMenu2 =  Proyect_EnglishGame()
        MainMenu2.show()
        self.parent().show()
        self.close()

class Play3_EnglishGame (QMainWindow): #segunda ventana
    def __init__(self, parent=None):
        super(Play3_EnglishGame, self).__init__(parent)
        loadUi ('Play3_EnglishGame.ui', self)
        self.button_BackMenu.clicked.connect(self.Back_Menu4)
        self.button_Answer.clicked.connect(self.Answer_Text)
        self.button_Next.clicked.connect(self.Open_Play4_EnglishGame)

    def Open_Play4_EnglishGame (self): #para abrir una ventana y cerrar la anterior
        self.hide()
        OtherWindow4 = Play5_EnglishGame(self)
        OtherWindow4.show()

    def Answer_Text (self):
        Correct = str("It's Correct, Congrats!!")
        Wrong = str("It's Wrong, Sorry :(")
        if self.Option1_3.isChecked():
            self.CorrectOrWrong3.setText(Correct)
        else:  #elif self.Option1isChecked == True or self.Option2.isChecked == True or self.Option3.isChecked == True 
            self.CorrectOrWrong3.setText(Wrong)
            
    def Back_Menu4 (self):
        self.hide()
        self.parent().show()
        self.close()
        MainMenu4 =  Proyect_EnglishGame()
        MainMenu4.show()


class Play5_EnglishGame (QMainWindow): #segunda ventana
    def __init__(self, parent=None):
        super(Play5_EnglishGame, self).__init__(parent)
        loadUi ('Play5_EnglishGame.ui', self)
        self.button_BackMenu.clicked.connect(self.Back_Menu5)
        self.button_Answer.clicked.connect(self.Answer_Text)
        self.button_Next.clicked.connect(self.Open_Play5_EnglishGame)

    def Open_Play5_EnglishGame (self): #para abrir una ventana y cerrar la anterior
        self.hide()
        OtherWindow5 = Play5_EnglishGame(self)
        OtherWindow5.show()

    def Answer_Text (self):
        Correct = str("It's Correct, Congrats!!")
        Wrong = str("It's Wrong, Sorry :(")
        if self.Option3_5.isChecked():
            self.CorrectOrWrong5.setText(Correct)
        else:  #elif self.Option1isChecked == True or self.Option2.isChecked == True or self.Option3.isChecked == True 
            self.CorrectOrWrong5.setText(Wrong)
            
    def Back_Menu5 (self):
        self.hide()
        self.parent().show()
        self.close()
        MainMenu5 =  Proyect_EnglishGame()
        MainMenu5.show()


if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Proyect_EnglishGame()
    main.show()                       
    sys.exit(app.exec_())


