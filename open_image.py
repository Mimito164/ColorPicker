
import sys
from PIL import Image
import requests

def open_image():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path or image_url>")
        sys.exit(1)


    img_path = sys.argv[1]

    
    try:
        if( img_path.startswith("https://")):
            img = Image.open(requests.get(img_path, stream=True).raw)
        else:
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