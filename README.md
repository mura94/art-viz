# art-viz

 Hanging art simulation tool using Blender command line tools & Python. Visualize how your art will look hanging on a wall with photo-realistic, computer-generated lighting.

> This repository is in active development. Check again in the future for future developments.

- [art-viz](#art-viz)
  - [Usage](#usage)
    - [Example](#example)
  - [Dependencies](#dependencies)
  - [Development](#development)
  - [Args](#args)
    - [Blender Command Line Args](#blender-command-line-args)
    - [Image Path](#image-path)
    - [Width](#width)
    - [Height](#height)
    - [Depth](#depth)
    - [Renderer](#renderer)
    - [Frame Type](#frame-type)
      - [Frame Options](#frame-options)
    - [Wall Color](#wall-color)
  - [Tips](#tips)

## Usage

 `blender -b <filename> -P <this_script> -- [--image or -I] <image-path> [--width or -W] <width-inches> [--height or -H] <height-inches> [--depth or -D] <depth-inches> [--renderer or -R] <renderer> [--frameType or -FT] <frame-type> [--wallColor or -WC] <wall-color-hex>`

### Example

```markdown
blender -b .\art-viz.blend -P render.py -- -I .\garlic.png -W 24 -H 18 -D .5 -R  CYCLES -FT BlackFloatingFrame -WC E4DED5
```

|Input |Output       |
|---      |---          |
|<img title="" src="garlic.png" alt="garlic" width="256" data-align="inline">|<img title="" src="assets/garlic_WoodFloatingFrame02.png" alt="garlic_WoodFloatingFrame02" width="256" data-align="inline">|

*More frames will be added in future updates soon!*

[:arrow_up: Back to Top](#art-viz)

## Dependencies

- Blender 2.8+
- Local Blender executable folder **must** be added to PATH
- Python 3.8.2+

## Development

- [x] Render scene via command line

- [x] Import image and apply to material

- [x] Export render to absolute file path

- [x] Resize canvas via args

- [x] Select renderer via args

- [x] Design custom frames

- [x] Select frame type via args

- [x] Make certain args optional

- [x] Set wall color via args

- [ ] Activate decor objects via args & json

- [ ] Control lighting via args or json

- [ ] Arg to save & load certain arg values as default prefs

- [ ] Output resolution arg

[:arrow_up: Back to Top](#art-viz)

## Args

### Blender Command Line Args

Start by copy and pasting this before you add custom args:

```markdown
blender -b .\art-viz.blend -P render.py   -- 
```

Everything that comes after `--` will be user-defined arguments, parsed in `render.py`.

Separate custom arguments with spaces after the `--` symbol. There must be a space on either side of the `--`.

### Image Path

ex: `apples.png`

This should be an image that exists in the root folder of this repository. Example use case could be a raw, cropped picture of a finished piece. Include the file extension in the name.

### Width

ex:`--width 20` or `-W 20` 

The width of the real piece in inches.

### Height

ex: `--height 16` or `-H 16`

The height of the real piece in inches.

### Depth

ex: `--depth .75` or `-D .75`

The depth of the real piece in inches.

### Renderer

ex: `--renderer CYCLES` or `-R CYCLES`

The type of renderer that Blender will use.

|Renderer         |Arg                |
|---              |---                |
|Cycles (default) |`CYCLES`           |
|Eevee            |`BLENDER_EEVEE`    |
|Workbench        |`BLENDER_WORKBENCH`|


### Frame Type

ex: `--frameType WhiteFloatingFrame` or `-FT WhiteFloatingFrame`

The frame that will surround the piece.

[:arrow_up: Back to Top](#art-viz)

#### Frame Options

Current `frameType` options are:

|   Name   |   Preview   |
|---|---|
|`WhiteFloatingFrame`   | <img title="" src="assets/garlic_WhiteFloatingFrame.png" alt="garlic_WhiteFloatingFrame" width="256" data-align="inline">   |
|`BlackFloatingframe`   | <img title="" src="assets/garlic_BlackFloatingFrame.png" alt="garlic_BlackFloatingFrame" width="256" data-align="inline">   |
|`WoodFloatingFrame01`  | <img title="" src="assets/garlic_WoodFloatingFrame01.png" alt="garlic_WoodFloatingFrame01" width="256" data-align="inline"> |
|`WoodFloatingFrame02`  | <img title="" src="assets/garlic_WoodFloatingFrame02.png" alt="garlic_WoodFloatingFrame02" width="256" data-align="inline"> |
|`WoodFloatingFrame03`  | <img title="" src="assets/garlic_WoodFloatingFrame03.png" alt="garlic_WoodFloatingFrame03" width="256" data-align="inline"> |
|`WoodFloatingFrame04`  | <img title="" src="assets/garlic_WoodFloatingFrame04.png" alt="garlic_WoodFloatingFrame04" width="256" data-align="inline"> |
|`WoodFloatingFrame05`  | <img title="" src="assets/garlic_WoodFloatingFrame05.png" alt="garlic_WoodFloatingFrame05" width="256" data-align="inline"> |
|`MetalFloatingFrameSilver`  | <img title="" src="assets/garlic_MetalFloatingFrameSilver.png" alt="garlic_MetalFloatingFrameSilver" width="256" data-align="inline"> |
|`MetalFloatingFrameGold`  | <img title="" src="assets/garlic_MetalFloatingFrameGold.png" alt="garlic_MetalFloatingFrameGold" width="256" data-align="inline"> |
|`MetalFloatingFrameBlack`  | <img title="" src="assets/garlic_MetalFloatingFrameBlack.png" alt="garlic_MetalFloatingFrameBlack" width="256" data-align="inline"> |



> :exclamation: This list will be updated in the near future as I create more frame models!

### Wall Color

ex: `--wallColor E4DED5` or `-WC E4DED5`

Set the hex color of the wall.

Optional. Defaults to E4DED5 - a warm off-white - if not set.

Some colors you can try from [Benjamin Moore](https://convertingcolors.com/list/benjamin-moore.html)

|Color Name       |Hex      |Tint       |
|---              |---      |---        |
|Deep Sea         |`002831` |Blue       |
|Dark Navy        |`2B2D42` |Blue       |
|Cool Grey        |`8D99AE` |Grey       |
|Anti-Flash White |`EDF2F4` |White      |
|Terra            |`DEBFA0` |Green/Brown|
|Fiji             |`4F8093` |Blue       |
|Caponata         |`463234` |Red        |
|Salmon           |`F29479` |Pink       |
|Herb             |`63774A` |Green      |
|Mint             |`D5DFCC` |Green      |
|Vintage          |`575E50` |Green      |
|Deep Red         |`310500` |Red        |
|Dirty Grey       |`545041` |Brown      |
|Strong Blue      |`202B54` |Blue       |
|Honeydew         |`C0E1B9` |Green      |
|Sioux            |`80968F` |Blue       |
|Deep             |`265557` |Blue       |
|Lazy             |`5F90B7` |Blue       |
|Stunning         |`424B63` |Blue       |

## Tips

- If the result is too small, double the size values (height/width/depth) to make the art appear larger in the final image

[:arrow_up: Back to Top](#art-viz)
