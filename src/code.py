import board
import displayio
import json
import terminalio

from adafruit_display_text import label, wrap_text_to_pixels

ZONE_COLOURS = [0x00ff00, 0xff6600, 0xff00ff, 0xffff00]

DISPLAY = board.DISPLAY

# Brightness is inverted
DISPLAY.brightness = 0


def set_display_error(error_str):
    splash = displayio.Group()
    DISPLAY.root_group = splash

    color_bitmap = displayio.Bitmap(160, 80, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette,x=0, y=0)
    splash.append(bg_sprite)

    text = '\n'.join(wrap_text_to_pixels(error_str, 160, terminalio.FONT))

    text_area = label.Label(
        terminalio.FONT, anchor_point=(0.5, 0.5), anchored_position=(80, 40),
        text=text, color=0x000000,
    )
    splash.append(text_area)


def set_display_zone(zone: int, is_comp: bool=True):
    splash = displayio.Group()
    DISPLAY.root_group = splash

    color_bitmap = displayio.Bitmap(160, 80, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = ZONE_COLOURS[zone]

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette,x=0, y=0)
    splash.append(bg_sprite)

    text = str(zone)
    text_area = label.Label(
        terminalio.FONT, label_direction='DWR', anchor_point=(0, 0.5),
        anchored_position=(0, 40), text=text, scale=9, color=0x000000
    )
    splash.append(text_area)

    if not is_comp:
        comp_text = label.Label(
            terminalio.FONT, anchor_point=(1, 0.5), anchored_position=(150, 40),
            text='NOT\nCOMP', scale=2, color=0x000000
        )
        splash.append(comp_text)


def get_zone_from_file(filename):
    "Read the zone and arena from a metadata file"
    with open(filename) as fp:
        config = fp.read()
        data = json.loads(config)

    print(data)

    return data['zone'], data['is_competition']


try:
    zone, is_comp = get_zone_from_file('metadata.json')
except Exception as e:
    set_display_error(str(e))
    print(e)
else:
    set_display_zone(zone, is_comp)

while True:
    pass
