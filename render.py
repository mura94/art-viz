# Run as: blender -b <filename> -P <this_script> -- <image_path>
import bpy, sys, os

# Assume the last argument is image path
imagePath = sys.argv[-1]

if os.path.exists(imagePath):
    # Assume object, material and texture name (and settings) are valid
    charObj = bpy.data.objects['Char01']
    charMat = charObj.material_slots['Char01Mat'].material

    mat = bpy.data.materials.new(name="New_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(bpy.path.relpath(imagePath))
    mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
    
    charObj.material_slots['Char01Mat'].material = mat

    # Render to separate file, identified by texture file
    path = 'C:/Users/blake/Documents/Blender/art-viz/'

    bpy.context.scene.render.filepath = path + imagePath + '_test01'
    
    # Render still image, automatically write to output path
    bpy.ops.render.render(write_still=True)
else:
    print("Missing Image:", imagePath)