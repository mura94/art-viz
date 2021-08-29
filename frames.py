import json
import bpy

path = str(pathlib.Path(__file__).parent.resolve())
jsonPath = path + '/frames.json'

def activateFrame(scene, name):
    f = open(jsonPath)
    data = json.loads(f.read())
    
