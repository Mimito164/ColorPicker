import math

def average_hsv(colors):
    
    hues = [math.radians(h) for h, _, _ in colors]
    saturations = [s for _, s, _ in colors]
    values = [v for _, _, v in colors]

    x = sum(math.cos(h) for h in hues)
    y = sum(math.sin(h) for h in hues)

    h_avg = math.degrees(math.atan2(y, x)) % 360

    s_avg = sum(saturations) / len(saturations)
    v_avg = sum(values) / len(values)

    return h_avg, s_avg, v_avg