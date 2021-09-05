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
    l.append('VeronaNarrowFrameBlack')
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

    l.append('- - - Classic Frames - - -')
    l.append('ClassicFrameMattedBlack')
    l.append('ClassicFrameMattedCherry')
    l.append('ClassicFrameMattedEspresso')
    l.append('ClassicFrameMattedMaple')
    l.append('ClassicFrameMattedWalnut')
    l.append('ClassicFrameMattedWashedWhite')
    l.append('ClassicFrameMattedWashedBlack')
    l.append('ClassicFrameMattedMetalBlack')
    l.append('ClassicFrameMattedMetalSilver')
    l.append('ClassicFrameMattedMetalGold')

    return l

def getRenderersList():
    return ['CYCLES', 'BLENDER_EEVEE', 'BLENDER_WORKBENCH']