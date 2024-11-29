ascii_art = {
    'A': [
        "   A   ",
        "  A A  ",
        " AAAAA ",
        "A     A",
        "A     A"
    ],
    'B': [
        "BBBBB  ",
        "B    B ",
        "BBBBB  ",
        "B    B ",
        "BBBBB  "
    ],
    'C': [
        " CCCCC ",
        "C      ",
        "C      ",
        "C      ",
        " CCCCC "
    ],
    'D': [
        "DDDDD  ",
        "D    D ",
        "D    D ",
        "D    D ",
        "DDDDD  "
    ],
    'E': [
        "EEEEEE ",
        "E      ",
        "EEEEEE ",
        "E      ",
        "EEEEEE "
    ],
    'F': [
        "FFFFFF ",
        "F      ",
        "FFFFF  ",
        "F      ",
        "F      "
    ],
    'G': [
        " GGGGG ",
        "G      ",
        "G  GGG ",
        "G     G",
        " GGGGG "
    ],
    'H': [
        "H     H",
        "H     H",
        "HHHHHHH",
        "H     H",
        "H     H"
    ],
    'I': [
        "IIIIII ",
        "  II   ",
        "  II   ",
        "  II   ",
        "IIIIII "
    ],
    'J': [
        "JJJJJJ ",
        "    JJ ",
        "    JJ ",
        "J   JJ ",
        " JJJJ  "
    ],
    'K': [
        "K    K ",
        "K  K   ",
        "KK     ",
        "K  K   ",
        "K    K "
    ],
    'L': [
        "L      ",
        "L      ",
        "L      ",
        "L      ",
        "LLLLLL "
    ],
    'M': [
        "M     M",
        "MM   MM",
        "M M M M",
        "M  M  M",
        "M     M"
    ],
    'N': [
        "N     N",
        "NN    N",
        "N N   N",
        "N  N  N",
        "N   N N"
    ],
    'O': [
        " OOOOO ",
        "O     O",
        "O     O",
        "O     O",
        " OOOOO "
    ],
    'P': [
        "PPPPPP ",
        "P    P ",
        "PPPPPP ",
        "P      ",
        "P      "
    ],
    'Q': [
        " QQQQQ ",
        "Q     Q",
        "Q     Q",
        "Q   Q Q",
        " QQQQQ "
    ],
    'R': [
        "RRRRRR ",
        "R    R ",
        "RRRRRR ",
        "R   R  ",
        "R    R "
    ],
    'S': [
        " SSSSS ",
        "S      ",
        " SSSSS ",
        "      S",
        " SSSSS "
    ],
    'T': [
        "TTTTTT ",
        "  TT   ",
        "  TT   ",
        "  TT   ",
        "  TT   "
    ],
    'U': [
        "U     U",
        "U     U",
        "U     U",
        "U     U",
        " UUUUU "
    ],
    'V': [
        "V     V",
        "V     V",
        " V   V ",
        "  V V  ",
        "   V   "
    ],
    'W': [
        "W     W",
        "W     W",
        "W  W  W",
        "W W W W",
        " W   W "
    ],
    'X': [
        "X     X",
        " X   X ",
        "  X X  ",
        " X   X ",
        "X     X"
    ],
    'Y': [
        "Y     Y",
        " Y   Y ",
        "  Y Y  ",
        "  Y Y  ",
        "  Y Y  "
    ],
    'Z': [
        "ZZZZZZ ",
        "    Z  ",
        "   Z   ",
        "  Z    ",
        "ZZZZZZ "
    ],
    '0': [
        "  000  ",
        " 0   0 ",
        "0     0",
        " 0   0 ",
        "  000  "
    ],
    '1': [
        "   1   ",
        "  11   ",
        "   1   ",
        "   1   ",
        "  111  "
    ],
    '2': [
        "  222  ",
        " 2   2 ",
        "    2  ",
        "   2   ",
        "  2222 "
    ],
    '3': [
        "  333  ",
        " 3   3 ",
        "    33 ",
        " 3   3 ",
        "  333  "
    ],
    '4': [
        "   44  ",
        "  4 4  ",
        " 4  4  ",
        " 44444 ",
        "    4  "
    ],
    '5': [
        "  5555 ",
        " 5     ",
        "  555  ",
        "     5 ",
        "  555  "
    ],
    '6': [
        "   666 ",
        "  6    ",
        " 6666  ",
        " 6   6 ",
        "  666  "
    ],
    '7': [
        " 77777 ",
        "     7 ",
        "    7  ",
        "   7   ",
        "  7    "
    ],
    '8': [
        "  888  ",
        " 8   8 ",
        "  888  ",
        " 8   8 ",
        "  888  "
    ],
    '9': [
        "  999  ",
        " 9   9 ",
        "  9999 ",
        "     9 ",
        "   99  "
    ],
    ' ': [
        "       ",
        "       ",
        "       ",
        "       ",
        "       "
    ],
    '@': [
        "  @@@  ",
        " @   @ ",
        "@  @@ @",
        "@     @",
        " @@@@  "
    ],
    '#': [
        "  # #  ",
        " ##### ",
        "  # #  ",
        " ##### ",
        "  # #  "
    ],
    '*': [
        "   *   ",
        "  * *  ",
        " ***** ",
        "  * *  ",
        "   *   "
    ],
    '.': [
        "       ",
        "       ",
        "       ",
        "       ",
        "   .   "
    ]
}


def print_ascii_art(text, symbol):
    lines = ['' for _ in range(5)]
    for char in text.upper():
        if char in ascii_art:
            for i in range(5):
                lines[i] += ascii_art[char][i].replace(char, symbol) + '  '
    return "\n".join(lines)