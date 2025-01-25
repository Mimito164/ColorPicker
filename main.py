from PIL import Image
import PIL
import PIL.ImageFile
import colorsys
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

def detect_colors(img:PIL.ImageFile):
    px = img.load()
    width,height = img.size
    for i in range(width):
        for j in range(height):
            h,s,v = px[i,j]
            
            # print(f"h:{int(h)}\ts:{int(s)}\tv:{int(v)}")
            color = (int(h),int(s),int(v))
            if f"{color}" in detected_colors:
                detected_colors[f"{color}"] += 1
            else:
                detected_colors[f"{color}"] = 1





def main():
    img = open_image()    
    detect_colors(img)
    
    # print(detected_colors)
    sorted_items = sorted(detected_colors.items(), key=lambda item: item[1], reverse=True)
    for color in sorted_items:
        print(color,end='\n')

if __name__ == "__main__":
    main()