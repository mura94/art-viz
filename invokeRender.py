import args
import os
import subprocess
from flask import Flask
from flask import request
from flask import abort
import unittest

currentDir = os.path.dirname(os.path.abspath(__file__)) + '/'

bashCommand = "blender -b " + currentDir + "art-viz.blend -P " + currentDir + "render.py   -- "

def render(args):
    s = bashCommand + '-I' + currentDir + args.image
    s +=  ' -W ' + str(args.width)
    s +=  ' -H ' + str(args.height)
    s +=  ' -D ' + str(args.depth)
    s +=  ' -R ' + args.renderer
    s +=  ' -FT ' + args.frameType
    s +=  ' -WC ' + args.wallColor
    s += ' -O ' +  args.output
    s += ' -OW ' + str(args.outputWidth)
    s += ' -OH ' + str(args.outputHeight)
    print(s)
    subprocess.run(s)
    if(args.openWhenFinished):
        os.startfile(currentDir + args.output)

def renderRequest(request):
    a = args.RenderArgs()
    a.width = request.args.get('width', default = '9')
    a.height = request.args.get('height', default = '12')
    a.depth = request.args.get('depth', default = '.1')
    a.renderer = request.args.get('renderer', default = 'CYCLES')
    a.frameType = request.args.get('frameType', default = 'BlackFloatingFrame')
    a.wallColor = request.args.get('wallColor', default = 'E4DED5')
    a.output = request.args.get('output', default = 'render-output.png')
    a.outputWidth = request.args.get('outputWidth', default = '1024')
    a.outputHeight = request.args.get('outputHeight', default = '1024')
    render(a)


if(__name__ == "__main__"):
    # a = args.RenderArgs()
    # a.renderer = 'BLENDER_EEVEE'
    # render(a)
    req = request()
