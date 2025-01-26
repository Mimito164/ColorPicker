import PIL
import PIL.ImageFile
from PIL import Image
import sys

from rgb_to_hsv import rgb_to_hsv
import filters
import color_picker_algorithms as algorithms

def open_image():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
        
    img_path = sys.argv[1]
    
    try:
        img = Image.open(img_path)
        if(img.size >= (256,256)):
            img = Image.Image.resize(img, (256,256))
        else:
            print("Error: The image is smaller than 256x256px")
        img = img.convert("RGB")
        return img
    except:
        print(f"Error: Unable to load image at '{img_path}'")
        sys.exit(1)

def get_colors(img:PIL.ImageFile):
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

def print_colors_dictionary(color_dict):
    sorted_items = sorted(color_dict.items(), key=lambda item: item[1], reverse=True)

    for color, count in sorted_items:
        print(f"{color}, {count}")



def main():
    chosen_color = None

    img = open_image()
    detected_colors = get_colors(img)

    detected_colors = filters.filter_garbage_pixels(detected_colors)
    detected_colors, grey_colors = filters.filter_grey(detected_colors)

    if len(detected_colors) != 0:
        chosen_color = algorithms.sliding_h(detected_colors)
    else:
        white,black = filters.filter_black_white(grey_colors)
        white_pixels = sum([value for _,value in white.items()])
        black_pixels = sum([value for _,value in black.items()])
        if white_pixels > black_pixels:
            chosen_color = algorithms.sliding_h(white,1)
        else:
            chosen_color = algorithms.sliding_h(black,1)

        # algorithms.highest_appearance()
    print(chosen_color)
    # img.show()
    
if __name__ == "__main__":
    main()