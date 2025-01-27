# ColorPicker

This is a code to choose a representative color based on an image.

## Run this code

To run this code
```bash
# 0. Create and activate a virtual enviroment in the repository root (recomended).
python -m venv .venv && source .venv/bin/activate

# 1. Install pip packages.
pip install -r requirements.txt

# 2. Run the code.
python main_kmeans.py logos/nvidia.png
```

- You can choose any image from logos directory or you can paste an url form internet

```bash
python main_kmeans.py https://www.criptonoticias.com/wp-content/uploads/2023/10/BC_Logo_.png
```
  

## Modes

In this repository there are two different algorithms for solving this problem.

- [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithm 
  - To run in this mode use `main_kmeans.py`
- The other algorithm uses a sliding window along the H values of all the colors present in the image, and then it averages the window with the biggest number of pixels
  - To run in this mode use `main_hsv.py`