from open_image import open_image
from average_hsv import average_hsv
from color_scanner import get_colors
from CONSTANTS import GREY, WHITE_V,BLACK_V
import color_picker_algorithms as algorithms
import filters

NUMBER_OF_CLUSTERS = 100

def filter_black_white(grey_colors:dict):
    def _is_white(hsv_color:tuple, white_constant) -> bool:
        return hsv_color[2] >= white_constant

    def _is_black(hsv_color:tuple, black_constant) -> bool:
        return hsv_color[2] <= black_constant
    
    white = [
        color for color in grey_colors if _is_white(color, WHITE_V)
    ]

    black = [
        color for color in grey_colors if _is_black(color, BLACK_V)
    ]


    return white, black

def filter_grey(detected_colors:list):
    def _is_grey(hsv_color:tuple, grey_constant) -> bool:
        return hsv_color[1] < grey_constant

    grey_colors = [
        color for color in detected_colors if _is_grey(color, GREY)
    ]

    non_grey_colors = [
        color for color in detected_colors if not _is_grey(color, GREY)
    ]

    return non_grey_colors, grey_colors

def distance_between_colors_h(color1, color2):
    diff = abs(color1[0] - color2[0])
    return min(diff, 360 - diff)

def classify_colors(detected_colors: list, klusters_centroids: list) -> list:
    klusters = [[] for _ in range(NUMBER_OF_CLUSTERS)]
    for color in detected_colors:
        distance_to_klusters = [distance_between_colors_h(k_centroid, color) for k_centroid in klusters_centroids]
        kluster_index = distance_to_klusters.index(min(distance_to_klusters))

        klusters[kluster_index].append( color)
    return klusters

def redefine_kluster_centroids(klusters: list, old_centroids: list) -> list:
    return [
        average_hsv(kluster) if kluster else old_centroids[i]
        for i, kluster in enumerate(klusters)
    ]

def main():
    iteration = 1
    klusters_centroids = [(x,100,100) for x in range(0,360,int(360/NUMBER_OF_CLUSTERS))]
    img = open_image()

    detected_colors = get_colors(img)
    detected_colors, grey_colors = filter_grey(detected_colors)

    if len(detected_colors) != 0:
        while True:
            print("iteration:", iteration)
            klusters = classify_colors(detected_colors, klusters_centroids)

            new_klusters_centroids = redefine_kluster_centroids(klusters, klusters_centroids)

            klusters_difference = [distance_between_colors_h(klusters_centroids[i], new_klusters_centroids[i]) for i in range(NUMBER_OF_CLUSTERS) ]
            if not all([ abs(difference) <= 0.2  for difference in klusters_difference]):
                klusters_centroids = new_klusters_centroids
                iteration += 1
            else:
                break

        kluster_items = [len(kluster) for kluster in klusters]
        chosen_color_index = kluster_items.index(max(kluster_items))
        H,S,V = klusters_centroids[chosen_color_index]
    else:
        white,black = filter_black_white(grey_colors)
        white_pixels = len(white)
        black_pixels = len(black)
        print(white_pixels, black_pixels)
        if white_pixels > black_pixels:
            H,S,V = average_hsv(white)
        else:
            H,S,V = average_hsv(black)
    print(f"h:{H}\ts:{S}\tv:{V}")
    img.show()


if __name__ == "__main__":
    main()