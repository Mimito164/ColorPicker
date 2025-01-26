import numpy as np
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

    """
    Blend HSV colors based on their appearance counts.

    Args:
        hsv_tuples (list of tuples): List of tuples in the format ((H, S, V), count).
        total_count (float): Total sum of appearances.

    Returns:
        tuple: Blended HSV color as (H, S, V).
    """
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
    
    WINDOW = 10

    list_of_windows = []
    
    for i in range(0,360,WINDOW):
        print(i, i+WINDOW)
        colors_in_window = list (filter(lambda item: item[0][0] >= i and item[0][0] < i+WINDOW,sorted_items))
        if len(colors_in_window) > 0: 
            list_of_windows.append(colors_in_window)
    list_of_windows.sort(key=lambda window: _get_pixel_count_from_window(window), reverse=True)
    print(*list_of_windows, sep='\n')
    r = weight_average(list_of_windows[0])
    return r


def algoritmo_custom(color_dict:dict):
    sorted_items = sorted(color_dict.items(), key=lambda item: item[1], reverse=True)
    
