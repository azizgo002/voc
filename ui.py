import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QListWidget, QVBoxLayout, QLineEdit

from core import Core

class Button(QPushButton):
    def __init__(self, text = ''):
        super().__init__(text)
        self.setFixedSize(200,60)
        self.setStyleSheet('background: #191970;' 'font-size: 20px;' 'font-weight: bold;' 'color: #fff;')



class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Translator")
        self.setFixedSize(500,600)

        self.v_box = QVBoxLayout()

        self.add_new_word_btn = Button('Add new word')
        self.list_words_btn = Button('List of words')
        self.search_word_btn = Button('Search word')
        self.exit_btn = Button('Exit')
    
        self.v_box.addWidget(self.add_new_word_btn)
        self.v_box.addWidget(self.list_words_btn)
        self.v_box.addWidget(self.search_word_btn)
        self.v_box.addWidget(self.exit_btn)

        self.setLayout(self.v_box)

        self.show()

class AddWordWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.core = Core()

        self.setWindowTitle("Add New Word")
        self.setFixedSize(500,600)

        self.v_box = QVBoxLayout()
        self.v_box_lang = QVBoxLayout()
        self.h_box_lang = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText('English...')
        self.v_box_lang.addWidget(self.eng_edit)

        self.uzb_edit = QLineEdit()
        self.uzb_edit.setPlaceholderText('Uzbek...')
        self.v_box_lang.addWidget(self.uzb_edit)
        self.h_box_lang.addLayout(self.v_box_lang)

        self.send_btn = QPushButton('Send')
        self.h_box_lang.addWidget(self.send_btn)
        self.v_box.addLayout(self.h_box_lang)
        self.send_btn.clicked.connect(self.saveWord)

        self.info_label = QLabel()
        self.v_box.addWidget(self.info_label)

        self.menu_btn = QPushButton('Menu')
        self.list_btn = QPushButton('List of words')
        self.search_btn = QPushButton('Search word')
        self.h_box_btns.addWidget(self.menu_btn)
        self.h_box_btns.addWidget(self.list_btn)
        self.h_box_btns.addWidget(self.search_btn)
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)
        self.show()

    def clearDisplay(self):
        self.eng_edit.clear()
        self.uzb_edit.clear()

    def saveWord(self):
        eng, uzb = self.eng_edit.text(), self.uzb_edit.text()
        self.core.insert(eng, uzb)
        self.clearDisplay()
        self.info_label.setText('Ok uraaaaa')
        

class ListWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.core = Core()

        self.setWindowTitle("List of words")
        self.setFixedSize(500,600)

        self.v_box = QVBoxLayout()
        self.v_box_eng = QVBoxLayout()
        self.v_box_uzb = QVBoxLayout()
        self.h_box_lang = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.eng_label = QLabel('English')
        self.v_box_eng.addWidget(self.eng_label)

        self.eng_qlw = QListWidget()
        self.v_box_eng.addWidget(self.eng_qlw)

        self.uzb_label = QLabel('Uzbek')
        self.v_box_uzb.addWidget(self.uzb_label)

        self.uzb_qlw = QListWidget()
        self.v_box_uzb.addWidget(self.uzb_qlw)

        self.h_box_lang.addLayout(self.v_box_eng)
        self.h_box_lang.addLayout(self.v_box_uzb)
        self.v_box.addLayout(self.h_box_lang)

        self.menu_btn = QPushButton('Menu')
        self.add_word_btn = QPushButton('Add new word')
        self.search_btn = QPushButton('Search word')
        self.h_box_btns.addWidget(self.menu_btn)
        self.h_box_btns.addWidget(self.add_word_btn)
        self.h_box_btns.addWidget(self.search_btn)
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)
        self.show_words()
        self.show()
    
    def show_words(self):
        data = self.core.select_all()
        for eng, uzb in data:
            self.eng_qlw.addItem(eng)
            self.uzb_qlw.addItem(uzb)


class SearchWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.core = Core()

        self.setWindowTitle("Search word")
        self.setFixedSize(500,600)

        self.v_box = QVBoxLayout()
        self.h_box_search = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText('Enter a word...')
        self.h_box_search.addWidget(self.search_edit)

        self.search_btn = QPushButton('Search')
        self.h_box_search.addWidget(self.search_btn)
        self.search_btn.clicked.connect(lambda: self.getSearchWord(self.search_edit.text()))

        self.v_box.addLayout(self.h_box_search)

        self.search_qlw = QListWidget()
        self.v_box.addWidget(self.search_qlw)

        self.menu_btn = QPushButton('Menu')
        self.add_word_btn = QPushButton('Add new word')
        self.list_btn = QPushButton('List of words')
        self.h_box_btns.addWidget(self.menu_btn)
        self.h_box_btns.addWidget(self.add_word_btn)
        self.h_box_btns.addWidget(self.list_btn)
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)
        self.show()

    def getSearchWord(self, search_word):
        word = self.core.get_search_word(search_word)
        if word:
            self.search_qlw.addItem(word)
        else:
            self.search_qlw.addItem('Word not found')
            

app = QApplication(sys.argv)
# win = MainWindow()
# win1 = AddWordWindow()
# win2 = ListWindow()
win3 = SearchWindow()
sys.exit(app.exec_())