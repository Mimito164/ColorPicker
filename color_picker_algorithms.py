import numpy as np
import CONSTANTS

from string_to_color import string_to_color 
from weight_average_hsv import weight_average_hsv, _get_pixel_count_from_window
from string_to_color import string_to_color

def highest_appearance(color_dict:dict) -> tuple:
    if not color_dict:
        return None  

    return string_to_color(max(color_dict, key=color_dict.get))


def _get_top_n_different_colors(list_of_windows, n):
    different_colors = []
    different_colors.append(list_of_windows[0])
    h1,s1,v1 = weight_average_hsv(list_of_windows[0])

    if len(different_colors) != n:    
        for window in list_of_windows:
            h2,s2,v2 = weight_average_hsv(window)
            if abs(h1 - h2) > CONSTANTS.HUE_DIFFERENCE:
                different_colors.append(window)
                break

    return different_colors
    


def sliding_h(color_dict:dict, different_colors=CONSTANTS.DIFERENT_COLORS):
    color_list = list(map( 
        lambda item: (string_to_color(item[0]),item[1]),
        color_dict.items() 
        ))

    sorted_items = sorted(
        color_list,
        key=lambda item: item[0][0],
        reverse=True
        )
    
    WINDOW = 1
    STEP = 0.5
    list_of_windows = []
    
    for i in  np.arange(0.0, 360-WINDOW+STEP, STEP):
        colors_in_window = list (filter(lambda item: item[0][0] >= i and item[0][0] < i+WINDOW,sorted_items))
        if len(colors_in_window) > 0: 
            list_of_windows.append(colors_in_window)

    list_of_windows.sort(key=lambda window: _get_pixel_count_from_window(window), reverse=True)
    
    windows_selected = _get_top_n_different_colors(list_of_windows, different_colors)


    r = weight_average_hsv([
            color 
            for window in windows_selected 
            for color in window
        ])

    return r


def custom_algorithm(color_dict:dict):
    sorted_items = sorted(color_dict.items(), key=lambda item: item[1], reverse=True) # sort by saturation