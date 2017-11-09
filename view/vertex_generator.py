from math import cos, sin, tan, radians


class Vertex_generator:
    def __init__(self, radius: float, faces: int, high: float, center_deep: float):
        self.radius = radius + high / 2
        self.center_deep = center_deep
        self.delta_ang = 360.0 / faces
        self.faces = faces
        self.high = high

    def define(self, radius: float, faces: int, high: float, center_deep: float):
        self.radius = radius + high / 2
        self.center_deep = center_deep
        self.delta_ang = 360.0 / faces
        self.faces = faces
        self.high = high


    def centers_pos(self):
        centers = []
        ang = 0
        for i in range(self.faces):
            v = []
            v.append(self.radius * cos(radians(ang)))
            v.append(self.radius * sin(radians(ang)))
            v.append(self.center_deep)
            centers.append(v)
            ang += self.delta_ang
        return centers

    def rot_angs(self):
        rot_angs = []
        ang = -90.0
        for i in range(self.faces):
            rot_angs.append(ang)
            ang += self.delta_ang
        return rot_angs

    def face_size(self):
        return 2 * (self.radius - self.high / 2) * tan(radians(self.delta_ang / 2))

    def face_verteces(self):
        verteces = []
        verteces.append([])
        verteces.append([])
        verteces.append([])
        verteces.append([])
        verteces[0].append(self.face_size() / 2)
        verteces[0].append(-self.high / 2)
        verteces[1].append(self.face_size() / 2 + self.high * tan(radians(self.delta_ang / 2)))
        verteces[1].append(self.high / 2)
        verteces[2].append(-(self.face_size() / 2 + self.high * tan(radians(self.delta_ang / 2))))
        verteces[2].append(self.high / 2)
        verteces[3].append(-self.face_size() / 2)
        verteces[3].append(-self.high / 2)
        return verteces

    def all_body_verteces(self, deep: float):
        vertices = self.face_verteces()
        vertices[0].append(deep / 2)
        vertices[1].append(deep / 2)
        vertices[2].append(deep / 2)
        vertices[3].append(deep / 2)
        vertices2 = self.face_verteces()
        vertices2[0].append(-deep / 2)
        vertices2[1].append(-deep / 2)
        vertices2[2].append(-deep / 2)
        vertices2[3].append(-deep / 2)

        all_vertices = []
        all_vertices.append(vertices)
        all_vertices.append(vertices2)
        return all_vertices
