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
        p1 = self.coords
        p2 = self.neighbour_coords[0]
        p3 = self.neighbour_coords[1]
        p0 = point
        
        d = [
            (p1[0] - p0[0]) * (p2[1] - p1[1]) - (p2[0] - p1[0]) * (p1[1] - p0[1]),
            (p2[0] - p0[0]) * (p3[1] - p2[1]) - (p3[0] - p2[0]) * (p2[1] - p0[1]),
            (p3[0] - p0[0]) * (p1[1] - p3[1]) - (p1[0] - p3[0]) * (p3[1] - p0[1])
        ]

        if d[0] * d[1] >= 0 and d[2] * d[1] >= 0 and d[0] * d[2] >= 0:
            return True
        return False


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
        a = self.neighbour_coords[0]
        b = self.coords
        c = self.neighbour_coords[1]
        ab = [b[0] - a[0], b[1] - a[1]]
        bc = [c[0] - b[0], c[1] - b[1]]
        if ab[0] * bc[1] - ab[1] * bc[0] <= 0:
            return False
        return True

    def get_triangle(self):
        return [self.prew, self.index, self.next]
