import numpy as np
import CONSTANTS
from string_to_color import string_to_color 

def highest_appearance(color_dict:dict) -> tuple:
    from string_to_color import string_to_color
    if not color_dict:  # Verificar si el diccionario está vacío
        return None  # Retorna None si el diccionario está vacío

    return string_to_color(max(color_dict, key=color_dict.get))

def _get_pixel_count_from_window(window_list:list):
    pixel_count = sum(list(map(lambda color: color[1], window_list)))
    return pixel_count


def weight_average(color_list):
    total_count = _get_pixel_count_from_window(color_list)
    # Initialize accumulators for Hue Cartesian components, Saturation, and Value
    x = 0.0
    y = 0.0
    weighted_s = 0.0
    weighted_v = 0.0

    for (h, s, v), count in color_list:
        weight = count / total_count  # Compute weight
        # Convert Hue to Cartesian coordinates
        x += np.cos(np.radians(h)) * weight
        y += np.sin(np.radians(h)) * weight
        # Weighted sums for Saturation and Value
        weighted_s += s * weight
        weighted_v += v * weight

    # Convert Cartesian coordinates back to Hue
    h = np.degrees(np.arctan2(y, x)) % 360
    s = weighted_s
    v = weighted_v

    return h, s, v

def _get_top_n_different_colors(list_of_windows, n=CONSTANTS.DIFERENT_COLORS):
    different_colors = []
    different_colors.append(list_of_windows[0])
    h1,s1,v1 = weight_average(list_of_windows[0])

    if len(different_colors) != n:    
        for window in list_of_windows:
            h2,s2,v2 = weight_average(window)
            print("loop", h1, h2)
            if abs(h1 - h2) > CONSTANTS.HUE_DIFFERENCE:
                different_colors.append(window)
                break

    return different_colors
    


def sliding_h(color_dict:dict):
    
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
    # print(*list_of_windows[:10], sep='\n')
    windows_selected = _get_top_n_different_colors(list_of_windows)
    # r = weight_average(list_of_windows[0])
    print(len(windows_selected))
    print(len(list_of_windows))
    r = weight_average( 
            [
                color 
                for window in windows_selected 
                for color in window
            ]
        )

    return r


def algoritmo_custom(color_dict:dict):
    sorted_items = sorted(color_dict.items(), key=lambda item: item[1], reverse=True)
    
