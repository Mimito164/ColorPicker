import numpy as np

def _get_pixel_count_from_window(window_list:list):
    pixel_count = sum(list(map(lambda color: color[1], window_list)))
    return pixel_count

def weight_average_hsv(color_list):
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