# Run as: blender -b <filename> -P <this_script> -- <image_path> <width-inches> <height-inches> <depth-inches> <renderer>
# ex: blender -b .\art-vis.blend -P render.py   -- <file-with-extension> 9 12 1 CYCLES

import bpy, sys, os
import pathlib


argv = sys.argv

renderer = sys.argv[-1]
imagePath = sys.argv[-5]
width = float(sys.argv[-4])
height = float(sys.argv[-3])
depth = float(sys.argv[-2])


if os.path.exists(imagePath):
    # Assume object, material and texture name (and settings) are valid
    canvas = bpy.data.objects['Canvas']
    canvasMat = canvas.material_slots['CanvasMat'].material

    canvasMat.use_nodes = True
    bsdf = canvasMat.node_tree.nodes["Principled BSDF"]
    texImage = canvasMat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(bpy.path.relpath(imagePath))
    canvasMat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
    
    bpy.context.scene.render.engine = renderer

    if(renderer == "CYCLES"):
        bpy.context.scene.render.engine = 'CYCLES' 
        bpy.data.scenes["Scene"].cycles.device='GPU' 
        bpy.context.scene.cycles.device = 'GPU'
        # bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = "OPTIX"
        # bpy.context.user_preferences.addons['cycles'].preferences.devices[0].use = True

    # Set dimensions
    # top = bpy.data.objects["Sizer"].data.bones["Top"]
    bpy.ops.object.mode_set(mode='POSE')

    context = bpy.context
    ob = context.object
    scene = context.scene
    bones = ob.pose.bones

    # Covert units from inches to meters
    # height /= 39.3701
    # width /= 39.3701
    # depth /= 39.3701

    # Set height
    top = bones['Top']
    bottom = bones['Bottom']
    top.location = (0, height/2 - 2, 0)
    bottom.location = (0, height/2 - 2, 0)

    # Set width
    left = bones['Left']
    right = bones['Right']
    left.location = (0, width/2 - 2, 0)
    right.location = (0, width/2 - 2, 0)

    # Set Depth
    depthb = bones['Depth']
    depthb.location = (0, depth - 0.1, 0)

    # Render to separate file, identified by texture file
    path = str(pathlib.Path(__file__).parent.resolve())
    path += '/'
    

    bpy.context.scene.render.filepath = path + imagePath + '_viz'
    
    # Render still image, automatically write to output path
    bpy.ops.render.render(write_still=True)

    print(width)
    print(height)
    print(depth)


else:
    print("Missing Image:", imagePath)