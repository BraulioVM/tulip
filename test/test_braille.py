from tulip.braille import get_braille_character

def test_get_braille_character():
    char1 = [
        (False, False),
        (False, False),
        (False, False),
        (False, False)
    ]

    char2 = [
        (True, True),
        (False, True),
        (True, False),
        (False, False)
    ]

    char3 = [
        (False, False),
        (False, False),
        (False, False),
        (True, True)
    ]
    
    char4 = [
        (False, False),
        (True, True),
        (True, True),
        (False, True)
    ]

    assert get_braille_character(char1) == '⠀' # empty braille
    assert get_braille_character(char2) == '⠝'
    
    assert get_braille_character(char3) == '⣀'

    assert get_braille_character(char4) == '⢶'
