BRAILLE_BASE = 0x2800
PIXEL_MAP = (
    (0x01, 0x08),
    (0x02, 0x10),
    (0x04, 0x20),
    (0x40, 0x80)
)

def get_braille_character(grid):
    character_code = BRAILLE_BASE
    for i, (pleft, pright) in enumerate(grid):
        if pleft:
            character_code += PIXEL_MAP[i][0]
        if pright:
            character_code += PIXEL_MAP[i][1]

    
    return chr(character_code)
    
