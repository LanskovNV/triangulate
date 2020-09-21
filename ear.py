class Ear:
        index = 0
        prew = 0
        next = 0
        coords = []
        neighbour_coords = []

        def __init__(self, points, ind):
            self.index = ind
            self.coords = points[ind]    
            self.prew = (ind + 1) % length
            if ind == 0:
                self.next = length - 1
            else: 
                self.next = ind - 1
            self.neighbour_coords = [
                points[self.prew],
                points[self.next]
            ]
        
        def validate(self, points):
            if self.is_convex() and True not in [self.is_inside(p) for p in points]:
                return True
            return False

        def is_convex(self):
            return True

        def is_neighbour(self, ind):
            return True
        
        def is_inside(self, point):
            return True

        def get_triangle(self):
            return [self.prew, self.index, self.next]