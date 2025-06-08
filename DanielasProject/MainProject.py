####pyuic5 -x DoSomething.ui -o DoSomething.py

#### იმპორტები
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from DoSomething import Ui_Danielaswindow
from random import randint

#### აპლიკაციის კლასი
class MyApp(QMainWindow, Ui_Danielaswindow):
    def __init__(self):
        #### გამოაქ ინფო DoSomething.py დან
        super().__init__()
        self.setupUi(self)
        self.imReadyPushButton.clicked.connect(self.linkLabelWithCheckbox)
        self.resetButton.clicked.connect(self.reset)
        self.checkboxList = [
            self.naskiCheckbox,
            self.sharvaliCheckbox,
            self.shortebiCheckbox,
            self.iubkaCheckbox,
            self.maisuriCheckbox,
            self.svitriCheckbox,
            self.hoodieCheckbox,
            self.bezrukavkaCheckbox,
            self.sharfiCheckbox,
            self.qudiCheckbox,
            self.xeltatmanebiCheckbox,
            self.botasebiCheckbox,
            self.qoshebiCheckbox,
            self.ketebiCheckbox,
            self.sandlebiCheckbox,
            ]
        self.labelList = [
            self.naskiFeriLabel,
            self.naskiFeriLabel_3,
            self.naskiFeriLabel_4,
            self.naskiFeriLabel_5,
            self.naskiFeriLabel_6,
            self.naskiFeriLabel_7,
            self.naskiFeriLabel_8,
            self.naskiFeriLabel_9,
            self.naskiFeriLabel_10,
            self.naskiFeriLabel_11,
            self.naskiFeriLabel_12,
            self.naskiFeriLabel_13,
            self.naskiFeriLabel_14,
            self.naskiFeriLabel_15,
            self.naskiFeriLabel_17,
        ]

        self.colors = [
            'black',
            'white',
            'black',
            'white',
            'red',
            'blue',
            'green',
            'purple',
            'magenta',
            'orange',
            'yellow',
            'RAINBOW',
        ]


        self.imReadyPushButton.clicked.connect(self.on_imReady_clicked)
        # self.imReadyPushButton.clicked.connect(self.linkLabelWithCheckbox)

    def truelist(self):
        returnlist = []
        for each in self.checkboxList:
            if each.isChecked():
                returnlist.append(each.text)
        return returnlist

    def on_imReady_clicked(self):
        checked = self.truelist()
        print("Checked checkboxes:", checked)

    def linkLabelWithCheckbox(self):
        for i in range(0, len(self.checkboxList)):
            if self.depresiaRadioButton.isChecked() and self.checkboxList[i].isChecked():
                x = randint(0, 3)
                self.labelList[i].setText(self.colors[x])
            elif self.checkboxList[i].isChecked() and self.happiRadioButton.isChecked():
                x = randint(4, len(self.colors))
                self.labelList[i].setText(self.colors[x])
            elif self.checkboxList[i].isChecked():
                x = randint(0, len(self.colors))
                self.labelList[i].setText(self.colors[x])
            else:
                self.labelList[i].hide()
                self.checkboxList[i].hide()

    def reset(self):
        for i in range(0, len(self.checkboxList)):
            self.checkboxList[i].show()
            self.labelList[i].show()





app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())