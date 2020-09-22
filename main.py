from src.earcut import Earcut
from src.polygon import Polygon
from src.utils import register_launch_arguments
from src.utils import load, save
from src.utils import draw_polygon


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

    if args.test:
        input_file = './data/rnd.csv'
        output_file = './data/out.csv'
        polygon_file = './data/rnd.png'
        num_nodes = 7

        for _ in range(100):
            vertices = Polygon(n=num_nodes, w=100, h=100).vertices
            draw_polygon(vertices, polygon_file)
            save(input_file, vertices, None)
            
        # vertices = load(input_file)

            triangles, error = triangulate(vertices)
            if len(triangles) == num_nodes - 2:
                print('OK')
            else:
                print('Incorrect triangulation')
                break
            save(output_file, triangles, None)

        # p = Polygon(n=5, w=10, h=10)
        # save(fname, p.vertices, None)
        # vertices = p.vertices
    else:
        points = load(args.input)
        vertices = Polygon(points=points).vertices
        triangles, error = triangulate(vertices)
        save(args.output, triangles, error)
    