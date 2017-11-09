from model.interactions import efects

MITAD_DE_PANTALLA = 10
FINAL_DE_IMAGEN = 0


class Block:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        self.vertices = []

        self.vertices.append([])
        self.vertices.append([])
        self.vertices_default()

        self.z_pos = -100.0
        self.speed = 0.05
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.rot_ang = 0.0

        self._width = 0
        self._high = 0
        self._deep = 0
        self.effect = efects.NullEffect()

    def vertices_default(self):
        self.vertices[0].append((1.0, 0.25, -2.0))
        self.vertices[0].append((-1.0, 0.25, -2.0))
        self.vertices[0].append((-1.0, 0.25, 2.0))
        self.vertices[0].append((1.0, 0.25, 2.0))

        self.vertices[1].append((1.0, -0.25, -2.0))
        self.vertices[1].append((-1.0, -0.25, -2.0))
        self.vertices[1].append((-1.0, -0.25, 2.0))
        self.vertices[1].append((1.0, -0.25, 2.0))

    def def_vertices(self, vertices):
        self.vertices = vertices

    def set_default_size(self):
        self._width = 4
        self._high = 2
        self._deep = 10

    def get_center(self):
        return self.pos_x, self.pos_y, self.pos_z

    def set_pos(self, x, y, z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos += z

    def set_rot_ang(self, rot_ang):
        self.rot_ang = rot_ang

    def out_of_map(self):
        return self.pos_z + self._deep / 2 < FINAL_DE_IMAGEN

    def is_ground(self, z_pos):
        return self.pos_z < z_pos < self.pos_z + self._deep and \
               MITAD_DE_PANTALLA - self._width / 2 == self.pos_y


class NullMapUnit(Block):
    pass
