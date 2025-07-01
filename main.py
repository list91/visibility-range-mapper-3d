def get_vision_params():
    # тут собираем то что щас видим
    # это имеет вид:
    # 
    # {
    #     "image": "", 
    #     "distance_points": [
    #             {
    #                 "id": 000,
    #                 "coordinate": {"x": 0, "y": 0},
    #                 "distance": 00
    #             },
    #             {
    #                 "id": 000,
    #                 "coordinate": {"x": 0, "y": 0},
    #                 "distance": 00
    #             }
    #         ], 
    # }
    vision_params = None
    return vision_params

def get_build_segment(vision_params):
    result_segment = None
    return result_segment

def main():
    while 1:
        vision_params = get_vision_params()
        segment = get_build_segment(vision_params)
        # слепить по общим точкам с ласт чанком сцены
        

