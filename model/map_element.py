from model.interactions import efects

MITAD_DE_PANTALLA = 10
FINAL_DE_IMAGEN = 0


class MapElement:
    def __init__(self):
        self._bl_corner_pos_x = 0
        self._bl_corner_pos_y = 0
        self._bl_corner_pos_z = 0
        self._width = 0
        self._high = 0
        self._deep = 0
        self.color = (0.0, 0.0, 0.0)
        self.effect = efects.NullEffect()

    def set_default_size(self):
        self._width = 4
        self._high = 2
        self._deep = 10

    def get_corners(self):
        return self._bl_corner_pos_x, self._bl_corner_pos_y, self._bl_corner_pos_z

    def move_to_valid_place(self, map_element_list: list, game_speed):
        last_element = map_element_list[-1]
        a, b, c = last_element.get_corners()
        a += self._deep
        self._bl_corner_pos_x, self._bl_corner_pos_y, self._bl_corner_pos_z = a, b, c

    def update_pos(self, valor_giro):
        self._bl_corner_pos_x += valor_giro

    def out_of_map(self):
        return self._bl_corner_pos_x + self._deep < FINAL_DE_IMAGEN

    def is_ground(self, x_pos):
        return self._bl_corner_pos_x < x_pos < self._bl_corner_pos_x + self._deep and \
               MITAD_DE_PANTALLA - self._width / 2 == self._bl_corner_pos_y


class NullMapElement(MapElement):
    pass
