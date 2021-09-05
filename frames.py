def getFrameList():
    l = ['- - - Wood Floating Frames - - -']
    l.append('BlackFloatingFrame')
    l.append('WhiteFloatingFrame')
    l.append('WoodFloatingFrame01')
    l.append('WoodFloatingFrame02')
    l.append('WoodFloatingFrame03')
    l.append('WoodFloatingFrame04')
    l.append('WoodFloatingFrame05')

    l.append('- - - Metal Floating Frames - - -')
    l.append('MetalFloatingFrameBlack')
    l.append('MetalFloatingFrameSilver')
    l.append('MetalFloatingFrameGold')
    
    l.append('- - - Verona Frames - - -')
    l.append('VeronaFrameBlack')
    l.append('VeronaFrameMattedBlack')
    l.append('VeronaFrameMattedCherry')
    l.append('VeronaFrameMattedEspresso')
    l.append('VeronaFrameMattedWalnut')
    l.append('VeronaFrameMattedMaple')
    l.append('VeronaFrameMattedWashedBlack')
    l.append('VeronaFrameMattedWashedWhite')
    l.append('VeronaFrameMattedRoughGrey')

    l.append('- - - Ornamental Frames - - -')
    l.append('OrnamentalFrame01')
    return l

def getRenderersList():
    return ['CYCLES', 'BLENDER_EEVEE', 'BLENDER_WORKBENCH']