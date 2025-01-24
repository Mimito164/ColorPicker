import cv2
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    
    img_path = sys.argv[1]
    img = cv2.imread(img_path)

    if img is None:
        print(f"Error: Unable to load image at '{img_path}'")
        sys.exit(1)
    
    cv2.imshow("Logo", img)
    cv2.waitKey(0)  # Wait indefinitely for a key press
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()