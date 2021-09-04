import os
from os import curdir, pipe
import sys
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)    
import subprocess

currentDir = os.path.dirname(os.path.abspath(__file__)) + '/'

bashCommand = "blender -b " + currentDir + "art-viz.blend -P " + currentDir + "render.py   -- "

print(bashCommand)
class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Create arg widgets
        self.imgLabel = QLabel("--image")
        self.image = QLineEdit("garlic.png")

        self.widthLabel = QLabel("--width")
        self.w = QLineEdit("24")

        self.heightLabel = QLabel("--height")
        self.h = QLineEdit("18")

        self.depthLabel = QLabel("--depth")
        self.d = QLineEdit(".5")

        self.rendererLabel = QLabel("--renderer")
        self.renderer = QLineEdit("CYCLES")

        self.frameTypeLabel = QLabel("--frameType")
        self.frame = QLineEdit("BlackFloatingFrame")

        self.wallColorLabel = QLabel("--wallColor")
        self.wallColor = QLineEdit("E4DED5")

        self.outputLabel = QLabel("--output")
        self.output = QLineEdit("render-output.png")

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
        layout.addWidget(self.frame)

        layout.addWidget(self.wallColorLabel)
        layout.addWidget(self.wallColor)

        layout.addWidget(self.outputLabel)
        layout.addWidget(self.output)

        layout.addWidget(self.button)
        layout.addWidget(self.openButton)
        
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.openButton.clicked.connect(self.openButtonClicked)
        self.button.clicked.connect(self.greetings)

       
    def openButtonClicked(self):
        print('opening ' + currentDir + self.output.text())
        os.startfile(currentDir + self.output.text())

    # Greets the user
    def greetings(self):
        s = bashCommand + '-I' + currentDir + self.image.text()
        s +=  ' -W ' +self.w.text() 
        s +=  ' -H ' +self.h.text() 
        s +=  ' -D ' +self.d.text() 
        s +=  ' -R ' +self.renderer.text() 
        s +=  ' -FT ' +self.frame.text() 
        s +=  ' -WC ' +self.wallColor.text() 
        s += ' -O ' + self.output.text()
        print(s)
        process = subprocess.run(s)

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
