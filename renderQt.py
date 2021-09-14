import os
from os import curdir, pipe
import sys
from PySide6.QtWidgets import (QAbstractButton, QCheckBox, QComboBox, QFileDialog, QLabel, QLineEdit, QPushButton, QApplication, QRadioButton, QSpinBox, QToolButton, QDoubleSpinBox,
    QVBoxLayout, QDialog)    
from PySide6 import QtGui
import subprocess
import frames as fr
import prefs
import glob
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

                            "QSpinBox {"
                            "color: #DBEDF3;"
                            "}"

                            "QDoubleSpinBox {"
                            "color: #DBEDF3;"
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


        self.blendLabel = QLabel("Blender File")
        self.blend = QComboBox()
        # blendFiles = glob.glob('*.blend')
        # self.blend.addItems(blendFiles)
        self.blend.setEditable(True)
                            
        self.imgLabel = QLabel("Image")
        self.image = QComboBox()
        self.image.setEditable(True)
        self.image.addItem(lastUsed['image'])
        

        self.imgFiles = []
        self.refreshFileLists()
        self.refreshButton = QPushButton("Refresh Lists")
        self.refreshButton.clicked.connect(self.refreshFileLists)

        # extensions = ('*.png', '*.jpg', '*.jpeg', '*.PNG')
        # for extension in extensions:
        #     imgFiles.extend(glob.glob(extension))
        
        # if(lastUsed['image'] in imgFiles):
        #     imgFiles.remove(lastUsed['image'])
        
        # self.image.addItems(self.imgFiles)

        self.widthLabel = QLabel("Width")
        self.w = QSpinBox()
        self.w.setValue(int(lastUsed['width']))

        self.heightLabel = QLabel("Height")
        self.h = QSpinBox()
        self.h.setValue(int(lastUsed['height']))

        self.depthLabel = QLabel("Depth")
        self.d = QDoubleSpinBox()
        self.d.setValue(float(lastUsed['depth']))

        self.rendererLabel = QLabel("Renderer")
        self.renderer = QComboBox()
        renderers = fr.getRenderersList()
        self.renderer.addItems(renderers)
        self.renderer.setCurrentIndex(renderers.index(lastUsed['renderer']))


        self.renderDeviceLabel = QLabel("Render Device")

        self.renderDevice = QComboBox()
        renderTypes = ['GPU', 'CPU']
        self.renderDevice.addItems(renderTypes)
        self.renderDevice.setCurrentIndex(renderTypes.index(lastUsed['renderDevice']))

        self.frameDropdown = QComboBox()
        self.frameDropdown.addItems(framesList)
        self.frameDropdown.setCurrentIndex(framesList.index(lastUsed['frameType']))

        self.frameTypeLabel = QLabel("Frame Type")

        self.wallColorLabel = QLabel("Wall Color")
        self.wallColor = QLineEdit(lastUsed['wallColor'])
        
        self.wallColorSelect = QComboBox()
        self.wallColorSelect.addItems(fr.colorDict)
        self.wallColorSelect.setEditable(True)

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

        layout.addWidget(self.blendLabel)
        layout.addWidget(self.blend)

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

        layout.addWidget(self.renderDeviceLabel)
        layout.addWidget(self.renderDevice)

        layout.addWidget(self.frameTypeLabel)
        layout.addWidget(self.frameDropdown)

        layout.addWidget(self.wallColorLabel)
        layout.addWidget(self.wallColorSelect)
        # layout.addWidget(self.wallColor)

        layout.addWidget(self.outputLabel)
        layout.addWidget(self.output)

        layout.addWidget(self.outputWidthLabel)
        layout.addWidget(self.outputWidth)

        layout.addWidget(self.outputHeightLabel)
        layout.addWidget(self.outputHeight)
        
        layout.addWidget(self.openWhenFinished)

        layout.addWidget(self.button)
        layout.addWidget(self.openButton)
        layout.addWidget(self.refreshButton)

        self.setLayout(layout)

        self.openButton.clicked.connect(self.openButtonClicked)
        self.button.clicked.connect(self.setLastUsedValues)
        self.button.clicked.connect(self.runWithArgs)

       
    def openButtonClicked(self):
        print('opening ' + currentDir + self.output.text())
        os.startfile(currentDir + self.output.text())

    def refreshFileLists(self):
        self.imgFiles = []
        extensions = ('*.png', '*.jpg', '*.jpeg', '*.PNG')
        for extension in extensions:
            self.imgFiles.extend(glob.glob(extension))
        
        self.image.clear()
        self.image.addItems(self.imgFiles)
        if(lastUsed['image'] in self.imgFiles):
            self.image.setCurrentIndex(self.imgFiles.index(lastUsed['image']))

        blendFiles = glob.glob('*.blend')
        self.blend.clear()
        self.blend.addItems(blendFiles)
        if(lastUsed['blend'] in blendFiles):
            self.blend.setCurrentIndex(blendFiles.index(lastUsed['blend']))

 
    def setLastUsedValues(self):
        lastUsed['image'] = self.image.currentText()
        lastUsed['width'] = self.w.text()
        lastUsed['height'] = self.h.text()
        lastUsed['depth'] = self.d.text()
        lastUsed['renderer'] = self.renderer.currentText()
        lastUsed['frameType'] = self.frameDropdown.currentText()
        lastUsed['wallColor'] = self.wallColorSelect.currentText()
        lastUsed['output'] = self.output.text()
        lastUsed['outputHeight'] = self.outputHeight.text()
        lastUsed['outputWidth'] = self.outputWidth.text()
        lastUsed['openWhenFinished'] = self.openWhenFinished.isChecked()
        lastUsed['renderDevice'] = self.renderDevice.currentText()
        lastUsed['blend'] = self.blend.currentText()

        print('Setting last used values in prefs file')
        prefs.setLastUsed(lastUsed)

    def runWithArgs(self):
        if("- - - " in self.frameDropdown.currentText()):
            print("Please pick a legitimate frame type")
            return
        a = args.RenderArgs()
        a.image = self.image.currentText()
        a.width = self.w.text()
        a.height = self.h.text()
        a.depth = self.d.text()
        a.renderer = self.renderer.currentText()
        a.frameType = self.frameDropdown.currentText()
        wallColor = self.wallColorSelect.currentText()

        if(wallColor in fr.colorDict):
            print('Converting preset ' + wallColor + ' to ' + fr.colorDict[wallColor])
            wallColor = fr.colorDict[wallColor]

        a.wallColor = wallColor
        a.output = self.output.text()
        a.outputWidth = self.outputWidth.text()
        a.outputHeight = self.outputHeight.text()
        a.openWhenFinished = self.openWhenFinished.isChecked()
        a.renderDevice = self.renderDevice.currentText()
        a.blend = self.blend.currentText()
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
