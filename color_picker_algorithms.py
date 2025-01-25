from string_to_color import string_to_color 

def highest_appearance(color_dict:dict) -> tuple:
    from string_to_color import string_to_color
    if not color_dict:  # Verificar si el diccionario está vacío
        return None  # Retorna None si el diccionario está vacío

    return string_to_color(max(color_dict, key=color_dict.get))

def sliding_h(color_dict:dict):
    
    color_list = list(map( 
        lambda item: (string_to_color(item[0]),item[1]),
        color_dict.items() 
        ))

    sorted_items = sorted(
        color_list,
        key=lambda item: item[0][0],
        reverse=True
        )
    
    WINDOW = 10
    print(sorted_items)
    # for i in range(0,360,2):
    #     sorted_items.ma   


def algoritmo_custom(color_dict:dict):
    sorted_items = sorted(color_dict.items(), key=lambda item: item[1], reverse=True)
    
