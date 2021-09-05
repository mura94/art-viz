import os
from os import curdir, pipe
import sys
from PySide6.QtWidgets import (QAbstractButton, QComboBox, QLabel, QLineEdit, QPushButton, QApplication, QToolButton,
    QVBoxLayout, QDialog)    
import subprocess
import frames as fr
import prefs

currentDir = os.path.dirname(os.path.abspath(__file__)) + '/'

bashCommand = "blender -b " + currentDir + "art-viz.blend -P " + currentDir + "render.py   -- "

framesList = fr.getFrameList()
lastUsed = prefs.getLastUsed()

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Create arg widgets
        self.imgLabel = QLabel("--image")
        self.image = QLineEdit(lastUsed['image'])

        self.widthLabel = QLabel("--width")
        self.w = QLineEdit(lastUsed['width'])

        self.heightLabel = QLabel("--height")
        self.h = QLineEdit(lastUsed['height'])

        self.depthLabel = QLabel("--depth")
        self.d = QLineEdit(lastUsed['depth'])

        self.rendererLabel = QLabel("--renderer")
        self.renderer = QComboBox()
        renderers = fr.getRenderersList()
        self.renderer.addItems(renderers)
        self.renderer.setCurrentIndex(renderers.index(lastUsed['renderer']))

        self.frameDropdown = QComboBox()
        self.frameDropdown.addItems(framesList)
        self.frameDropdown.setCurrentIndex(framesList.index(lastUsed['frameType']))

        self.frameTypeLabel = QLabel("--frameType")
        # self.frame = QLineEdit(framesList)

        self.wallColorLabel = QLabel("--wallColor")
        self.wallColor = QLineEdit(lastUsed['wallColor'])

        self.outputLabel = QLabel("--output")
        self.output = QLineEdit(lastUsed['output'])

        self.outputWidthLabel = QLabel("--outputWidth")
        self.outputWidth = QLineEdit(str(lastUsed['outputWidth']))

        self.outputHeightLabel = QLabel("--outputHeight")
        self.outputHeight = QLineEdit(str(lastUsed['outputHeight']))

        self.openWhenFinished = QPushButton("Open output when finished")
        self.openWhenFinished.setCheckable(True)
        self.openWhenFinished.setChecked(bool(lastUsed['openWhenFinished']))

        # Submit button
        self.button = QPushButton("Run with Args")
        self.openButton = QPushButton("Open Output File")

        # Create layout and add widgets
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
        # layout.addWidget(self.frame)

        layout.addWidget(self.wallColorLabel)
        layout.addWidget(self.wallColor)

        layout.addWidget(self.outputLabel)
        layout.addWidget(self.output)

        layout.addWidget(self.outputWidthLabel)
        layout.addWidget(self.outputWidth)

        layout.addWidget(self.outputHeightLabel)
        layout.addWidget(self.outputHeight)

        layout.addWidget(self.button)
        layout.addWidget(self.openButton)
        layout.addWidget(self.openWhenFinished)
        
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
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

    # Greets the user
    def runWithArgs(self):
        if("- - - " in self.frameDropdown.currentText()):
            print("Please pick a legitimate frame type")
            return
        s = bashCommand + '-I' + currentDir + self.image.text()
        s +=  ' -W ' +self.w.text() 
        s +=  ' -H ' +self.h.text() 
        s +=  ' -D ' +self.d.text() 
        s +=  ' -R ' +self.renderer.currentText() 
        s +=  ' -FT ' +self.frameDropdown.currentText() 
        s +=  ' -WC ' +self.wallColor.text() 
        s += ' -O ' + self.output.text()
        s += ' -OW ' + self.outputWidth.text()
        s += ' -OH ' + self.outputHeight.text()

        print(s)
        subprocess.run(s)
        if(self.openWhenFinished.isChecked()):
            os.startfile(currentDir + self.output.text())

        # output, error = process.communicate()

        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.setWindowTitle("art-viz")
    form.setMinimumWidth(300)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
