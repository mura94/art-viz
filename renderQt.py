import os
from os import curdir, pipe
import sys
from PySide6.QtWidgets import (QAbstractButton, QCheckBox, QComboBox, QFileDialog, QLabel, QLineEdit, QPushButton, QApplication, QRadioButton, QToolButton,
    QVBoxLayout, QDialog)    
from PySide6 import QtGui
import subprocess
import frames as fr
import prefs
import args
import invokeRender

currentDir = os.path.dirname(os.path.abspath(__file__)) + '/'

bashCommand = "blender -b " + currentDir + "art-viz.blend -P " + currentDir + "render.py   -- "

framesList = fr.getFrameList()
lastUsed = prefs.getLastUsed()

brightColor = '#00818A'
lightColor = '#DBEDF3'
medColor = '#404B69'
darkColor = '#283149'

textColor = lightColor

style = ("QPushButton { background-color: %s;"
                            "border-radius: 3px;"
                            "border-color: %s;"
                            "border-style: none;"
                            "border-width: 2px;"
                            "color: %s;"
                            "padding: 4px"
                            "}" 

                            "QPushButton:!hover { background-color: #283149; border-style: none; }"
                            "QPushButton:hover { background-color: #00818A; border-style: none; }"
                            "QPushButton:pressed { background-color: %s; border-style: none; color: black}"

                            "QLineEdit {"
                            "border: 1px solid gray;"
                            "border-radius: 3px;"
                            "padding: 0 2px;"
                            "background: %s;"
                            "selection-background-color: %s;"
                            "color: #DBEDF3;"
                            "}"

                            "QMainWindow {"
                            "background: %s;"
                            "width: 10px;"
                            "height: 10px;"
                            "}"

                            "QLineEdit:hover {"
                            "background: #283149;"
                            "}"

                            "QComboBox {"
                            "border: 1px solid %s;"
                            "border-radius: 2px;"
                            "background-color: %s;"
                            "color: #DBEDF3;"
                            "}"

                            "QComboBox QAbstractItemView {"
                            "color: #DBEDF3;"
                            "selection-background-color: #00818A;"
                            "}"

                            "QLabel {"
                            "font-weight: bold;"
                            "color: %s;"
                            "}"

                            "QWidget {"
                            "background-color: %s;"
                            "}"

                            "QRadioButton {"
                            "color: #DBEDF3;"
                            "}"
                            % (darkColor, lightColor, lightColor, lightColor, lightColor, brightColor, lightColor, 'gray', lightColor, lightColor, medColor))

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setStyleSheet(style)
                            
        self.imgLabel = QLabel("Image")
        self.image = QLineEdit(lastUsed['image'])

        self.widthLabel = QLabel("Width")
        self.w = QLineEdit(lastUsed['width'])

        self.heightLabel = QLabel("Height")
        self.h = QLineEdit(lastUsed['height'])

        self.depthLabel = QLabel("Depth")
        self.d = QLineEdit(lastUsed['depth'])

        self.rendererLabel = QLabel("Renderer")
        self.renderer = QComboBox()
        renderers = fr.getRenderersList()
        self.renderer.addItems(renderers)
        self.renderer.setCurrentIndex(renderers.index(lastUsed['renderer']))

        self.frameDropdown = QComboBox()
        self.frameDropdown.addItems(framesList)
        self.frameDropdown.setCurrentIndex(framesList.index(lastUsed['frameType']))

        self.frameTypeLabel = QLabel("Frame Type")

        self.wallColorLabel = QLabel("Wall Color")
        self.wallColor = QLineEdit(lastUsed['wallColor'])

        self.outputLabel = QLabel("Output")
        self.output = QLineEdit(lastUsed['output'])

        self.outputWidthLabel = QLabel("Output Width")
        self.outputWidth = QLineEdit(str(lastUsed['outputWidth']))

        self.outputHeightLabel = QLabel("Output Height")
        self.outputHeight = QLineEdit(str(lastUsed['outputHeight']))

        self.button = QPushButton("Run with Args")
        self.openButton = QPushButton("Open Output File")

        self.openWhenFinished = QRadioButton("Open When Finished")
        self.openWhenFinished.setChecked(bool(lastUsed['openWhenFinished']))

        layout = QVBoxLayout()

        layout.addWidget(self.imgLabel)
        layout.addWidget(self.image)

        layout.addWidget(self.widthLabel)
        layout.addWidget(self.w)

        layout.addWidget(self.heightLabel)
        layout.addWidget(self.h)

        layout.addWidget(self.depthLabel)
        layout.addWidget(self.d)

        layout.addWidget(self.rendererLabel)
        layout.addWidget(self.renderer)

        layout.addWidget(self.frameTypeLabel)
        layout.addWidget(self.frameDropdown)

        layout.addWidget(self.wallColorLabel)
        layout.addWidget(self.wallColor)

        layout.addWidget(self.outputLabel)
        layout.addWidget(self.output)

        layout.addWidget(self.outputWidthLabel)
        layout.addWidget(self.outputWidth)

        layout.addWidget(self.outputHeightLabel)
        layout.addWidget(self.outputHeight)
        
        layout.addWidget(self.openWhenFinished)

        layout.addWidget(self.button)
        layout.addWidget(self.openButton)

        self.setLayout(layout)

        self.openButton.clicked.connect(self.openButtonClicked)
        self.button.clicked.connect(self.setLastUsedValues)
        self.button.clicked.connect(self.runWithArgs)

       
    def openButtonClicked(self):
        print('opening ' + currentDir + self.output.text())
        os.startfile(currentDir + self.output.text())

 
    def setLastUsedValues(self):
        lastUsed['image'] = self.image.text()
        lastUsed['width'] = self.w.text()
        lastUsed['height'] = self.h.text()
        lastUsed['depth'] = self.d.text()
        lastUsed['renderer'] = self.renderer.currentText()
        lastUsed['frameType'] = self.frameDropdown.currentText()
        lastUsed['wallColor'] = self.wallColor.text()
        lastUsed['output'] = self.output.text()
        lastUsed['outputHeight'] = self.outputHeight.text()
        lastUsed['outputWidth'] = self.outputWidth.text()
        lastUsed['openWhenFinished'] = self.openWhenFinished.isChecked()
        print('Setting last used values in prefs file')
        prefs.setLastUsed(lastUsed)

    def runWithArgs(self):
        if("- - - " in self.frameDropdown.currentText()):
            print("Please pick a legitimate frame type")
            return
        a = args.RenderArgs()
        a.image = self.image.text()    
        a.width = self.w.text() 
        a.height = self.h.text() 
        a.depth = self.d.text() 
        a.renderer = self.renderer.currentText() 
        a.frameType = self.frameDropdown.currentText() 
        a.wallColor = self.wallColor.text() 
        a.output = self.output.text()
        a.outputWidth = self.outputWidth.text()
        a.outputHeight = self.outputHeight.text()
        a.openWhenFinished = self.openWhenFinished.isChecked()
        invokeRender.render(a)

def showRenderWindow():
    app = QApplication(sys.argv)
    form = Form()
    form.setWindowTitle("art-viz")
    form.setMinimumWidth(300)
    form.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    showRenderWindow()
