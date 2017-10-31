import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        Labelname=QLabel("Name:")
        LineEditname=QLineEdit("",self)
        Labelage=QLabel("Age:")
        LineEditage=QLineEdit("",self)
        Labelscore=QLabel("Score:")
        LineEditscore=QLineEdit("",self)
        LineEditname.textChanged[str].connect(self.nameshift)
        LineEditage.textChanged[str].connect(self.ageshift)
        LineEditscore.textChanged[str].connect(self.scoreshift)

        
        hbox = QHBoxLayout()        
        hbox.addWidget(Labelname)
        hbox.addWidget(LineEditname)
        hbox.addWidget(Labelage)
        hbox.addWidget(LineEditage)
        hbox.addWidget(Labelscore)
        hbox.addWidget(LineEditscore)

        Labelamount=QLabel("Amount:")
        LineEditamount=QLineEdit("",self)
        LineEditamount.textChanged[str].connect(self.amountshift)
        Labelkey=QLabel("Key:")
        combokey=QComboBox(self)
        combokey.addItem('Name')
        combokey.addItem('Age')
        combokey.addItem('Score')
        combokey.activated[str].connect(self.Clicked)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(Labelamount)
        hbox2.addWidget(LineEditamount)
        hbox2.addWidget(Labelkey)
        hbox2.addWidget(combokey)
        
        butadd = QPushButton("Add",self)
        butshow = QPushButton("Show",self)
        butdelete = QPushButton("Del",self)
        butinc = QPushButton("Inc",self)
        butfind = QPushButton("Find",self)

        butadd.clicked.connect(self.addScoreDB)
        butshow.clicked.connect(self.showScoreDB)
        butdelete.clicked.connect(self.delScoreDB)
        butinc.clicked.connect(self.incScoreDB)
        butfind.clicked.connect(self.findScoreDB)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(butadd)
        hbox3.addWidget(butfind)
        hbox3.addWidget(butdelete)
        hbox3.addWidget(butinc)
        hbox3.addWidget(butshow)

        Labelres = QLabel("Result:")
        self.TextEdit = QTextEdit(self)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(Labelres)
        hbox4.addWidget(self.TextEdit)
     

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)
        
                
        
        self.setGeometry(300, 300, 600, 340)
        self.setWindowTitle('Assignment6')    
        self.show()


    def Clicked(self , text):
        self.tempkey = text
    def nameshift(self,text):
        self.name = text
    def ageshift(self,text):
        self.age = text
    def scoreshift(self,text):
        self.score = text
    def amountshift(self,text):
        self.amount = text

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        string =''
        for p in sorted(self.scoredb, key = lambda person : person[self.tempkey]):
            for x in sorted(p):
                string += x+'='+str(p[x])+"     "
            string +='\n'
        self.TextEdit.setText(string)
    def addScoreDB(self):
        name = self.name
        score = self.score
        age = self.age

        record = {'Name' : name, 'Age' : int(age), 'Score' : int(score)}
        self.scoredb +=[record]
        self.showScoreDB()

    def findScoreDB(self):
        string=''
        name = self.name
        for k in self.scoredb:
            if k['Name'] == name:
                string += k['Name'] + 'Age:'+str(k['Age'])+'Score:'+str(k['Score']) + '\n'
        self.TextEdit.setText(string)

    def delScoreDB(self):
        d=0
        while d<len(self.scoredb):
            if self.scoredb[d]['Name'] == self.name:
                self.scoredb.remove(self.scoredb[d])
            else:
                d += 1
        self.showScoreDB()

    def incScoreDB(self):
        amount = self.amount
        a=0
        while a<len(self.scoredb):
            if self.scoredb[a]['Name'] == self.name:
                self.scoredb[a]['Score'] += int(amount)
                a += 1
            else:
                a += 1
        self.showScoreDB()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





