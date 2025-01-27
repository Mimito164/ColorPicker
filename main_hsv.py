
from open_image import open_image
import filters
import color_picker_algorithms as algorithms
from color_scanner import get_colors_freq



def print_colors_dictionary(color_dict):
    sorted_items = sorted(color_dict.items(), key=lambda item: item[1], reverse=True)

    for color, count in sorted_items:
        print(f"{color}, {count}")



def main():
    chosen_color = None

    img = open_image()
    detected_colors = get_colors_freq(img)

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