import numpy as np


class Ear:
        index = 0
        prew = 0
        next = 0
        coords = []
        neighbour_coords = []

        def __init__(self, points, indexes, ind):
            self.index = ind
            self.coords = points[ind]    
            length = len(indexes)
            index_in_indexes_arr = indexes.index(ind)
            self.next = indexes[(index_in_indexes_arr + 1) % length]
            if index_in_indexes_arr == 0:
                self.prew = indexes[length - 1]
            else: 
                self.prew = indexes[index_in_indexes_arr - 1]
            self.neighbour_coords = [
                points[self.prew],
                points[self.next]
            ]
        
        def is_inside(self, point):
            det = []
            a = [point[0], point[1], 1]
            b = [self.neighbour_coords[0][0], self.neighbour_coords[0][1], 1]
            c = [self.neighbour_coords[1][0], self.neighbour_coords[1][1], 1]
            
            det.append([a, b, c])
            det.append([b, c, a])
            det.append([c, a, b])
            
            for d in det:
                if np.linalg.det(d) > 0:
                    return False
            return True

        def is_ear_point(self, p):
            if p == self.coords or p in self.neighbour_coords:
                return True
            return False

        def validate(self, points, indexes, ears):
            not_ear_points = []
            for i in indexes:
                if points[i] != self.coords and points[i] not in self.neighbour_coords:
                    not_ear_points.append(points[i])
            insides = [self.is_inside(p) for p in not_ear_points]
            if self.is_convex() and True not in insides:
                for e in ears:
                    if e.is_ear_point(self.coords):
                        return False
                return True
            return False

        def is_convex(self):
            a = [self.coords[0], self.coords[1], 1]
            b = [self.neighbour_coords[0][0], self.neighbour_coords[0][1], 1]
            c = [self.neighbour_coords[1][0], self.neighbour_coords[1][1], 1]
            
            if np.linalg.det([b, a, c]) < 0:
                return False
            return True

        def get_triangle(self):
            return [self.prew, self.index, self.next]