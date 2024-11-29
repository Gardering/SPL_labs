def scale_ascii_art(ascii_art, max_width=None, max_height=None):
    lines = ascii_art.splitlines()

    if max_width:
        scaled_lines = [line[:max_width] for line in lines]
    else:
        scaled_lines = lines

    if max_height and len(scaled_lines) > max_height:
        scaled_lines = scaled_lines[:max_height]

    return "\n".join(scaled_lines)

def replace_with_symbols(ascii_art, symbols):
    if len(symbols) > 1:
        ascii_art = ascii_art.replace('#', symbols[0])
    else:
        ascii_art = ascii_art.replace('#', symbols)

    return ascii_art
