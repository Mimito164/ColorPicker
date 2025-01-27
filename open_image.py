
import sys
import PIL
import PIL.ImageFile
from PIL import Image

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