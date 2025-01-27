import PIL
import PIL.ImageFile
from rgb_to_hsv import rgb_to_hsv


def get_colors_freq(img:PIL.ImageFile):
    detected_colors = {}
    px = img.load()
    width,height = img.size
    for i in range(width):
        for j in range(height):
            r,g,b = px[i,j]
            
            hsv_color = rgb_to_hsv(r,g,b) # esta funcion realizo la conversion de manera correcta
            
            if f"{hsv_color}" in detected_colors:
                detected_colors[f"{hsv_color}"] += 1
            else:
                detected_colors[f"{hsv_color}"] = 1

    return detected_colors

def get_colors(img:PIL.ImageFile):
    detected_colors = []
    px = img.load()
    width,height = img.size
    for i in range(width):
        for j in range(height):
            r,g,b = px[i,j]
            hsv_color = rgb_to_hsv(r,g,b)
            detected_colors.append(hsv_color)
            
    return detected_colors