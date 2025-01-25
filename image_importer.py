import cv2
import sys

def import_image():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
        
    img_path = sys.argv[1]
    img = cv2.imread(img_path)

    if img is None:
        print(f"Error: Unable to load image at '{img_path}'")
        sys.exit(1)

    return cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    