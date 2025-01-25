def string_to_color(color_str:str) -> tuple:
    color_str = color_str.strip("()")
    channels = color_str.split(",")
    return float(channels[0]), float(channels[1]), float(channels[2])
