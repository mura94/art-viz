# Run as: blender -b <filename> -P <this_script> -- <image_path> <width-inches> <height-inches> <depth-inches> <renderer>
# ex: blender -b .\art-vis.blend -P render.py   -- <file-with-extension> 9 12 1 CYCLES

import bpy, sys, os
import pathlib
import argparse

############
#### argparse
parser = argparse.ArgumentParser(description='Generate visually realistic renders of paintings or other 2D artwork.')
parser.add_argument('image', metavar='IMG', type=str, nargs=1, help='The relative path of the original image')

parser.add_argument('width', metavar='WIDTH', type=float, nargs=1, help='The width of the original in inches',default=10)
parser.add_argument('height', metavar='HEIGHT', type=float, nargs=1,help='The height of the original in inches',default=10)
parser.add_argument('depth', metavar='DEPTH', type=float, nargs=1, help='The depth of the original in inches', default=1)
parser.add_argument('renderer', metavar="RENDERER", type=str, nargs=1, help='The desired renderer to use within Blender. ex: CYCLES', default='CYCLES')
parser.add_argument('frameType', metavar="FRAME", type=str, nargs=1, help='The type of frame to use.')

argv = sys.argv
startArgs = argv.index('--') + 1
argv = argv[startArgs:]
args = parser.parse_args(argv)
#############

# Get arg values
imagePath = args.image[0]
renderer = args.renderer[0]
width = args.width[0]
height = args.height[0]
depth = args.depth[0]
renderer = args.renderer[0]
frame = args.frameType[0]

if os.path.exists(imagePath):
    # Assign image to canvas object's material
    canvas = bpy.data.objects['Canvas']
    canvasMat = canvas.material_slots['CanvasMat'].material
    canvasMat.use_nodes = True
    bsdf = canvasMat.node_tree.nodes["Principled BSDF"]
    texImage = canvasMat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(bpy.path.relpath(imagePath))
    canvasMat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
    
    # Set renderer type based on arg
    bpy.context.scene.render.engine = renderer

    # Setup cycles to use GPU compute (comment out if using CPU compute)
    if(renderer == "CYCLES"):
        bpy.context.scene.render.engine = 'CYCLES' 
        bpy.data.scenes["Scene"].cycles.device='GPU' 
        bpy.context.scene.cycles.device = 'GPU'

    # Set dimensions using an armature
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
    

    bpy.context.scene.render.filepath = path + imagePath + '_viz'
    
    # Render still image, automatically write to output path
    bpy.ops.render.render(write_still=True)

    print(frame)

else:
    print("Missing Image:", imagePath)