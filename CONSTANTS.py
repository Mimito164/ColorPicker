"""
This constant is used to separate gey colors. Where a grey color has in the S channel (saturation) less than 30.
White and black colors also are considered as grey.
"""
GREY = 30

"""
This constant is for dismiss garbage pixels. A garbage pixel is the one wich appears less than 10 times. 
"""
GARBAGE = 10

"""
This constant is for selecting the amount of different colors to combine.
"""
DIFERENT_COLORS=2

"""
This is the minimum difference two hues must have to be considered as different colors
"""
HUE_DIFFERENCE=10
