import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Map:
    """
    Map(width, height)
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.wall = []  # QPoint Type
        self.path = []  # QPoint Type

        self.radish = QPoint(0, 0)
        self.rabbit = QPoint(width - 1, height - 1)
        self.set_init_map()

    def set_init_map(self):
        self.set_wall(QPoint(1, 1))
        self.set_wall(QPoint(1, 2))
        self.set_wall(QPoint(2, 1))

    def set_map_size(self, width, height):
        self.width = width
        self.height = height

    def set_wall(self, position):
        """
        The type of parameter:"position" is QPoint
        """
        self.wall.append(position)

    def set_radish(self, position):
        self.radish = position

    def set_rabbit(self, position):
        self.rabbit = position

    def on_special_object(self, spe_object, position):
        """
        To judge  whether the selected position is on the special object
        :param spe_object: "wall", "radish", "rabbit"
        :param position: QPoint type
        :return: True or False
        """
        if spe_object == "wall":
            for i in range(len(self.wall)):
                if self.wall[i] == position:
                    return True
            return False
        elif spe_object == "radish":
            if self.radish == position:
                return True
            else:
                return False
        elif spe_object == "rabbit":
            if self.radish == position:
                return True
            else:
                return False

    def out_map(self, position):
        if position.x() < 0 or position.x() > self.width or \
           position.y() < 0 or position.y() > self.height:
            return True
        else:
            return False

    def is_invalid(self, position):
        """
        when the point is in the wall or out of the map,
        it is invalid.
        :param position: QPoint Type position
        :return: True or False
        """
        if self.out_map(position) or \
           self.on_special_object("wall", position):
            return True
        else:
            return False

    def manhattan_length(self, pos1, pos2):
        """
        compute the manhattan distance between pos1 and pos2
        """
        distance = pos1-pos2
        return distance.manhattanLength()

    def a_star_searching(self):
        self.path.clear()
        open_list, close_list = [], []
        temp_point, current_point = QPoint(), QPoint()


if  __name__ == "__main__":
    myMap = Map(3, 3)
    print(myMap.on_special_object("wall", QPoint(-1, 1)))
    print(myMap.is_invalid(QPoint(-1, 1)))




