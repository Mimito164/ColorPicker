from string_to_color import string_to_color

def get_color(color_tuple:tuple) -> tuple:
    color_str = color_tuple[0]
    return string_to_color(color_str)

def _is_grey(hsv_color:tuple, grey_constant) -> bool:
    return hsv_color[1] < grey_constant

def filter_grey(detected_colors:dict, grey_constant=20):
    grey_colors = {}
    non_grey_colors = {}

    grey_colors = {
        key: value for key, value in detected_colors.items() if _is_grey(string_to_color(key), grey_constant)
    }

    non_grey_colors = {
        key: value for key, value in detected_colors.items() if not _is_grey(string_to_color(key), grey_constant)
    }
    return non_grey_colors, grey_colors