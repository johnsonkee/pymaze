from PyQt5.QtCore import QPoint
import copy
import numpy
import time

[BASE_ROAD, WALL, RABBIT, RADISH] = [0, 1, 2, 3]


class Map:
    """
    Map(width, height)
    """

    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height

        self.wall = []  # QPoint Type
        self.path = []  # QPoint Type

        self.rabbit = QPoint(0, 0)
        self.radish = QPoint(width - 1, height - 1)

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

    def clear_one_wall(self, position):
        if not self.on_special_object("radish", position):
            if not self.on_special_object("rabbit", position):
                if self.on_special_object("wall", position):
                    wall_index = self.wall.index(position)
                    self.wall.pop(wall_index)

    def clear_all_wall(self):
        self.wall.clear()

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
        if position.x() < 0 or position.x() > self.width - 1 or \
           position.y() < 0 or position.y() > self.height - 1:
            return True
        else:
            return False

    def is_valid(self, position):
        """
        when the point is not in the wall or out of the map,
        it is valid.
        :param position: QPoint Type position
        :return: True or False
        """
        if self.out_map(position) or \
           self.on_special_object("wall", position):
            return False
        else:
            return True

    def manhattan_length(self, pos1, pos2):
        """
        compute the manhattan distance between pos1 and pos2
        """
        distance = pos1-pos2
        return distance.manhattanLength()

    def a_star_searching(self):
        """
        Use A* algorithm to find the best path between rabbit and radish
        :return:
        """
        # time.clock() to compute the running time of a_star_searching

        if self.rabbit == QPoint(-1,-1) or self.radish == QPoint(-1,-1):
            return [False]
        start_time = time.clock()
        self.path.clear()
        open_list, close_list = [], []
        # temp_point 在生成open表时有用，current_point表示目前搜索到的点
        temp_point, current_point = QPoint(), QPoint()
        path_length = [[0 for i in range(self.height)] for j in range(self.width)]
        parent_point = [[QPoint(-1, -1) for i in range(self.height)] for j in range(self.width)]

        min_cost, temp_cost, sequence= 0, 0, 0
        close_list.append(self.rabbit)

        while True:
            open_list.clear()
            # find the adjacent points of every point in close_list
            for i in range(len(close_list)):
                current_point = close_list[i]
                # temp_point is the adjacent points(4) of current_point
                temp_point = [copy.deepcopy(current_point) for i in range(4)]
                temp_point[0].setX(temp_point[0].x()-1)
                temp_point[1].setX(temp_point[1].x()+1)
                temp_point[2].setY(temp_point[2].y()-1)
                temp_point[3].setY(temp_point[3].y()+1)

                for j in range(4):
                    if close_list.count(temp_point[j]) == 0 :
                        if open_list.count(temp_point[j]) == 0:
                            if self.is_valid(temp_point[j]):
                                # use deepcopy to assure the open_list unchangeable when
                                # the temp_point changes
                                open_list.append(copy.deepcopy(temp_point[j]))
            if len(open_list) == 0:
                return [False]
            # find all the distance of between points in open_list and beginning point
            for i in range(len(open_list)):
                current_point = open_list[i]
                # makes the min_cost as large as possible
                min_cost = self.width * self.height
                for j in range(len(close_list)):
                    temp_point = close_list[j]
                    if self.manhattan_length(current_point, temp_point) == 1:
                        temp_cost = path_length[temp_point.x()][temp_point.y()] + 1
                        if temp_cost < min_cost:
                            min_cost = copy.deepcopy(temp_cost)
                            sequence = j
                parent_point[current_point.x()][current_point.y()] = copy.deepcopy(close_list[sequence])
                path_length[current_point.x()][current_point.y()] = min_cost

            min_cost = self.width * self.height
            for i in range(len(open_list)):
                current_point = open_list[i]
                temp_cost = path_length[current_point.x()][current_point.y()] + \
                            self.manhattan_length(current_point, self.radish)
                if temp_cost < min_cost:
                    min_cost = temp_cost
                    sequence = i
            temp_point = copy.deepcopy(open_list[sequence])
            close_list.append(temp_point)
            if temp_point == self.radish:
                while True:
                    self.path.append(copy.deepcopy(temp_point))
                    temp_point = parent_point[temp_point.x()][temp_point.y()]
                    if temp_point.x() == -1:
                        return [True, time.clock() - start_time]

    def save_map(self, file_path):
        """
        save the map as a numpy matrix
        """
        map_matrix = [[BASE_ROAD for i in range(self.width)] for j in range(self.height)]
        map_matrix = numpy.array(map_matrix).T
        for i in range(len(self.wall)):
            map_matrix[self.wall[i].x()][self.wall[i].y()] = WALL
        map_matrix[self.rabbit.x()][self.rabbit.y()] = RABBIT
        map_matrix[self.radish.x()][self.radish.y()] = RADISH

        map_matrix = numpy.array(map_matrix).T
        numpy.savetxt(file_path, map_matrix, fmt='%d')

    def load_map(self, file_path):
        """
        read the map from a numpy matrix
        """
        # 加转置保证地图文件和ui画面上物品位置匹配
        map_matrix = numpy.loadtxt(file_path, dtype=int)
        self.path.clear()
        self.wall.clear()
        self.set_map_size(map_matrix.shape[1], map_matrix.shape[0])
        # 存在才画出来
        if len(numpy.argwhere(map_matrix == RABBIT)):
            self.set_rabbit(QPoint(numpy.argwhere(map_matrix == RABBIT)[0][1],
                                   numpy.argwhere(map_matrix == RABBIT)[0][0]))
        if len(numpy.argwhere(map_matrix == RADISH)):
            self.set_radish(QPoint(numpy.argwhere(map_matrix == RADISH)[0][1],
                                   numpy.argwhere(map_matrix == RADISH)[0][0]))
        temp_wall = numpy.argwhere(map_matrix == WALL)
        for i in range(temp_wall.shape[0]):
            self.set_wall(QPoint(temp_wall[i][1], temp_wall[i][0]))


if  __name__ == "__main__":
    myMap = Map(5, 5)
    print(myMap.on_special_object("wall", QPoint(-1, 1)))
    print(myMap.is_valid(QPoint(-1, 1)))
    myMap.load_map("initMap.txt")
    print(myMap.a_star_searching())
    print(myMap.path)
