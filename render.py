# ex: blender -b .\art-viz.blend -P render.py -- -I .\garlic.png -W 24 -H 18 -D .5 -R  CYCLES -FT BlackFloatingFrame -WC E4DED5

import bpy, sys, os
import pathlib
import argparse

############
#### argparse
parser = argparse.ArgumentParser(description='Generate visually realistic renders of paintings or other 2D artwork.')
parser.add_argument('-I', '--image', metavar='IMG', type=str, help='The relative path of the original image')

parser.add_argument('-W', '--width', metavar='WIDTH', type=float, help='The width of the original in inches',default=10)
parser.add_argument('-H', '--height', metavar='HEIGHT', type=float,help='The height of the original in inches',default=10)
parser.add_argument('-D', '--depth', metavar='DEPTH', type=float, help='The depth of the original in inches', default=1)
parser.add_argument('-R', '--renderer', metavar="RENDERER", type=str, help='The desired renderer to use within Blender. ex: CYCLES', default='CYCLES')
parser.add_argument('-FT', '--frameType', metavar="FRAME", type=str, help='The type of frame to use.')
parser.add_argument('-WC', "--wallColor", type=str, help='The hex value to apply to the wall.', default="E4DED5")
parser.add_argument('-O', "--output", type=str, help='The output file name (with extension)', default="render-output_0000.png")

argv = sys.argv
startArgs = argv.index('--') + 1
argv = argv[startArgs:]
args = parser.parse_args(argv)
#############

# Get arg values
imagePath = args.image
renderer = args.renderer
width = args.width
height = args.height
depth = args.depth
renderer = args.renderer
frame = args.frameType
wallColor = args.wallColor
outputName = args.output

def hex_to_rgb(value):
    gamma = 2.2
    value = value.lstrip('#')
    lv = len(value)
    fin = list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    r = pow(fin[0] / 255, gamma)
    g = pow(fin[1] / 255, gamma)
    b = pow(fin[2] / 255, gamma)
    fin.clear()
    fin.append(r)
    fin.append(g)
    fin.append(b)
    fin.append(1.0)
    return tuple(fin)

if os.path.exists(imagePath):
    # Assign image to canvas object's material
    canvas = bpy.data.objects['Canvas']
    canvasMat = canvas.material_slots['CanvasMat'].material
    canvasMat.use_nodes = True
    bsdf = canvasMat.node_tree.nodes["Principled BSDF"]
    texImage = canvasMat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(bpy.path.relpath(imagePath))
    canvasMat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

    print(wallColor)
    wall = bpy.data.objects['Wall']
    wallMat = wall.material_slots['Wall'].material
    wallMat.use_nodes = True
    principled_bsdf = wallMat.node_tree.nodes['Principled BSDF']
    rgb = hex_to_rgb(wallColor)
    if principled_bsdf is not None:
        principled_bsdf.inputs[0].default_value = (rgb[0], rgb[1], rgb[2], 1)

    #(0.024158, 0.026241, 0.05448, 1)

    # Set renderer type  based on arg
    bpy.context.scene.render.engine = renderer

    # Setup cycles to use GPU compute (comment out if using CPU compute)
    if(renderer == "CYCLES"):
        bpy.context.scene.render.engine = 'CYCLES' 
        bpy.data.scenes["Scene"].cycles.device='GPU' 
        bpy.context.scene.cycles.device = 'GPU'

    # Set dimensions using an armature
    bpy.context.view_layer.objects.active = bpy.data.objects['Sizer']
    bpy.ops.object.mode_set(mode='POSE')


    context = bpy.context
    ob = context.object
    scene = context.scene
    bones = ob.pose.bones

    # Activate frame of choice
    if(frame != 'None'):
        frameObject = bpy.data.objects[frame]
        frameObject.hide_render = False

    # Set height
    top = bones['Top']
    bottom = bones['Bottom']
    top.location = (0, height - 2, 0)
    bottom.location = (0, height - 2, 0)

    # Set width
    left = bones['Left']
    right = bones['Right']
    left.location = (0, width - 2, 0)
    right.location = (0, width - 2, 0)

    # Set Depth
    depthb = bones['Depth']
    depthb.location = (0, depth - 0.1, 0)

    # Render to separate file, identified by texture file
    path = str(pathlib.Path(__file__).parent.resolve())
    path += '/'
    

    bpy.context.scene.render.filepath = path + outputName
    
    # Render still image, automatically write to output path
    bpy.ops.render.render(write_still=True)

    print(frame)
    print(wallColor)

else:
    print("Missing Image:", imagePath)
