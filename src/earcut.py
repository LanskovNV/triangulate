from src.ear import Ear


class Earcut:
    def __init__(self, points): 
        self.vertices = []
        self.ears = []
        self.neighbours = []
        self.triangles = []
        self.vertices = points
        self.length = len(points)
    
    def update_neighbours(self):
        neighbours = []
        self.neighbours = neighbours

    def add_ear(self, new_ear):
        self.ears.append(new_ear)
        self.neighbours.append(new_ear.prew)
        self.neighbours.append(new_ear.next)

    def find_ears(self):
        i = 0
        indexes = list(range(self.length))
        while True:
            if i >= self.length:
                break
            new_ear = Ear(self.vertices, indexes, i)
            if new_ear.validate(self.vertices, indexes, self.ears):
                self.add_ear(new_ear)
                indexes.remove(new_ear.index)
            i += 1        

    def triangulate(self):
        indexes = list(range(self.length))
        self.find_ears()
        
        num_of_ears = len(self.ears)

        if num_of_ears == 0:
            raise ValueError
        if num_of_ears == 1:
            self.triangles.append(self.ears[0].get_triangle())
            return 

        while True:   
            if len(self.ears) == 2 and len(indexes) == 4:
                self.triangles.append(self.ears[0].get_triangle())
                self.triangles.append(self.ears[1].get_triangle())
                break
            
            if len(self.ears) == 0:
                raise IndexError
            current = self.ears.pop(0)
            
            indexes.remove(current.index)
            self.neighbours.remove(current.prew)
            self.neighbours.remove(current.next)

            self.triangles.append(current.get_triangle())

            # check if prew and next is new ears
            prew_ear_new = Ear(self.vertices, indexes, current.prew)
            next_ear_new = Ear(self.vertices, indexes, current.next)
            if prew_ear_new.validate(self.vertices, indexes, self.ears) and prew_ear_new.index not in self.neighbours:
                self.add_ear(prew_ear_new)
                continue
            if next_ear_new.validate(self.vertices, indexes, self.ears) and next_ear_new.index not in self.neighbours:
                self.add_ear(next_ear_new)
                continue