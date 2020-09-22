import matplotlib.pyplot as plt
import numpy as np
import os
from src.earcut import Earcut
from src.polygon import Polygon
from src.utils import register_launch_arguments
from src.utils import load, save
from src.utils import draw_polygon
import time


def triangulate(vertices):
    error = None
    triangles = []

    try:
        earcut = Earcut(vertices)
        earcut.triangulate()
        triangles = earcut.triangles
    except ValueError:
        error = 'ERROR: Incorrect input'
    except IndexError:
        error = 'ERROR: Try to get ear from empty list. Possible reason: incorrect polygon vertices direction'
    
    return triangles, error

if __name__ == '__main__':
    args = register_launch_arguments()

    if args.asymptote:
        nodes = [4, 8, 16, 32, 64, 128, 256]
        times = []
        for n in nodes:
            vertices = Polygon(n=n, w=100, h=100).vertices
            tic = time.perf_counter()
            triangles, error = triangulate(vertices)
            toc = time.perf_counter()
            times.append(toc - tic)
            print(n)
        plt.plot(np.log(nodes), np.log(times))
        plt.plot([2, 8], [-10, 2], 'r')
        plt.show()
        
    elif args.test:
        num_nodes = 10
        subdir = f'./data/bad_{num_nodes}'
        input_file = './data/bad_{}/rnd_{}.csv'
        output_file = './data/bad_{}/out_{}.csv'
        polygon_file = './data/bad_{}/rnd_{}.png'

        if not os.path.exists(subdir):
            os.makedirs(subdir)

        for _ in range(100):
            vertices = Polygon(n=num_nodes, w=100, h=100).vertices
            triangles, error = triangulate(vertices)
            if len(triangles) == num_nodes - 2:
                print('OK')
            else:
                print('Incorrect triangulation: same vertices or bad order with intersections')
                draw_polygon(vertices, polygon_file.format(num_nodes, _))
                save(input_file.format(num_nodes, _), vertices, None)
                save(output_file.format(num_nodes, _), triangles, None)
    else:
        vertices = load(args.input)
        triangles, error = triangulate(vertices)
        save(args.output, triangles, error)
    