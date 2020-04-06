from .yaml_database import YamlDatabase

class MoveClickTool():
    def __init__(self, data_maker):
        self.__data_maker = data_maker

    def add(self, data):
        self.__data_maker.xy_abs_move(data["move"]["x"], data["move"]["y"])
        if data["click"] == 1:
            self.__data_maker.one_click()
        self.__data_maker.wait(data["wait_ms"])
    
    def make_data(self, move_x, move_y, click_val, wait_ms, database):
        data = {
            'move': {
                'x': int(move_x),
                'y': int(move_y),
            },
            'click':int(click_val),
            'wait_ms': int(wait_ms),
        }
        database.register(data)


