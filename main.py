from PIL import Image
import PIL
import PIL.ImageFile
import cv2
import sys
import numpy as np

detected_colors = {}

def open_image():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
        
    img_path = sys.argv[1]
    
    try:
        img = Image.open(img_path)
        img = img.convert("HSV")
        return img
    except:
        print(f"Error: Unable to load image at '{img_path}'")
        sys.exit(1)

def detect_pixels(img:PIL.ImageFile):
    px = img.load()
    width,height = img.size
    for i in range(width):
        for j in range(height):
            print(px[i,j])



def main():
    img = open_image()    
    detect_pixels(img)
    
    
    # hls_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    # width, height, channel = hls_img.shape
    # h_values, l_values, s_values = cv2.split(hls_img)
  
    # print(np.unique(h_values))

    # for i in range(width):
    #     for j in range(height):
            
    #         h,l,s = hls_img[i][j][0], hls_img[i][j][1], hls_img[i][j][2]
    #         color_tuple = (h,l,s)
    #         color_key = f"{color_tuple}" 
    #         if color_key in color_count:
    #             color_count[color_key] += 1
    #         else:
    #             color_count[color_key] = 1

    # print(color_count)
    # for i in range(hls_img):
    #     for j in row:
    #         h,l,s = hls_img[]
    #         print(pixel, end=' ')



    # cv2.imshow("Logo", hls_img)
    # cv2.waitKey(0)  # Wait indefinitely for a key press
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()