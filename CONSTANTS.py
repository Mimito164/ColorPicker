"""
The saturation value to consider a color as Grey. If the color saturation is less than this value it is grey
"""
GREY = 30

"""
The v channel of hsv color to consider a color as black. If the color value is less than this value it is black
"""
BLACK_V = 10

"""
The v channel of hsv color to consider a color as white. If the color value is less than this value it is white
"""
WHITE_V = 90

"""
The amount of pixels of same color to be considered as garbage. If a color appears less than this value it is garbage. 
"""
GARBAGE = 10

"""
This constant is for selecting the amount of different colors to combine.
"""
DIFERENT_COLORS=1

"""
This is the minimum difference two hues must have to be considered as different colors
"""
HUE_DIFFERENCE=10
