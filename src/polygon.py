import math
import random


class Polygon:
    """
        Class used for testing only
    """
    def __init__(self, **kwargs):
        points = kwargs.get('points')
        
        self.points = []
        self.vertices = []
        self.n = 16
        self.h = 16
        self.w = 16

        if points != None:
            self.points = points
        else:
            n = kwargs.get('n')
            w = kwargs.get('w')
            h = kwargs.get('h')
            if n: self.n = n
            if w: self.w = w
            if h: self.h = h
            self.generate()

        self.sort()

    def sort(self):
        center_point = [self.w / 2, self.h / 2]
        self.vertices = self.points.copy()

        def sort_by_angle(p1, p2):
            a = math.atan2(p1[1] - center_point[1], p1[0] - center_point[0]) * 180 / math.pi
            b = math.atan2(p2[1] - center_point[1], p2[0] - center_point[0]) * 180 / math.pi
            return a - b

        def cmp_to_key(mycmp):
            class K:
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0
                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0
                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0
            return K

        self.vertices.sort(key=cmp_to_key(sort_by_angle))
    
    def generate(self):
        while len(self.points) != self.n:
            new_p = [random.randint(0, self.w), random.randint(0, self.h)]
            if new_p not in self.points:
                self.points.append(new_p)
    
    