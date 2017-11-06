from model.map_element import MapElement, NullMapElement


class Rodillo:
    """
    una lista con los elementos que tiene el mapa
    """

    def __init__(self):
        self.elementos = []
        self.velocidad_inicial = 1.0
        self.n_elem_in_slice = 6
        self.start_rodillo()

    def start_rodillo(self):
        """
        genera un primer grupo de elementos para el mapa
        """
        for i in range(3):  # cantidad de elementos a agregar en un comienzo:
            elemento = MapElement()
            MapElement.set_default_size()
            elemento.move_to_valid_place(self.elementos, self.velocidad_inicial)
            self.elementos.append(elemento)

    def girar_rodillo(self, valor_giro):
        """
        mueve los elementos segun el valor de giro dado, si un elemento queda fuera del mapa, es reposicionado.
        :param valor_giro: cantidad de desplazamiento del rodillo
        :return:
        """
        for elemento in self.elementos:
            elemento.update_pos(valor_giro)
            if elemento.out_of_map():
                elemento.move_to_valid_place(self.elementos, self.velocidad_inicial)

    def get_ground(self, x_pos):
        """
        entrega el elemento en el cual se para, o se podría parar el actor, si no existe tal elemento entrega un
        elemento nulo.
        :param x_pos:
        :return: elemento sobre el que se para el actor
        """
        for elemento in self.elementos:
            if elemento.is_ground(x_pos):
                return elemento
        return NullMapElement()

    def rotar_der(self):
        pass

    def rotar_izq(self):
        pass
