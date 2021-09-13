import renderQt as qt

class RenderArgs():
    def __init__(self, parent=None):
        self.blend = 'art-viz.blend'
        self.image = 'peaches.png'
        self.width = 9
        self.height = 12
        self.depth = 0.5
        self.renderer = 'CYCLES'
        self.frameType = 'BlackFloatingFrame'
        self.wallColor = 'E4DED5'
        self.output = 'render-output.png'
        self.outputWidth = 1024
        self.outputHeight = 1024
        self.openWhenFinished = True
        self.renderDevice = 'GPU'