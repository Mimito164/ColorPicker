from string_to_color import string_to_color
import CONSTANTS

def _is_grey(hsv_color:tuple, grey_constant) -> bool:
    return hsv_color[1] < grey_constant

def _is_white(hsv_color:tuple, white_constant) -> bool:
    return hsv_color[2] >= white_constant

def _is_black(hsv_color:tuple, black_constant) -> bool:
    return hsv_color[2] <= black_constant

def filter_grey(detected_colors:dict, grey_constant=CONSTANTS.GREY):
    grey_colors = {}
    non_grey_colors = {}

    grey_colors = {
        key: value for key, value in detected_colors.items() if _is_grey(string_to_color(key), grey_constant)
    }

    non_grey_colors = {
        key: value for key, value in detected_colors.items() if not _is_grey(string_to_color(key), grey_constant)
    }
    return non_grey_colors, grey_colors

def filter_garbage_pixels(detected_colors:dict):
    return {
        key: value for key, value in detected_colors.items() if value > CONSTANTS.GARBAGE
    }

def filter_black_white(grey_colors:dict):
    white = {
        key: value for key, value in grey_colors.items() if _is_white(string_to_color(key), CONSTANTS.WHITE_V)
    }

    black = {
        key: value for key, value in grey_colors.items() if _is_black(string_to_color(key), CONSTANTS.BLACK_V)
    }


    return white, black