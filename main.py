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
        vertices = load(input_file)
        
        try:
            earcut = Earcut(vertices)
            earcut.triangulate()
            triangles = earcut.triangles
        except ValueError:
            error = 'ERROR: Incorrect input'
        except IndexError:
            error = 'ERROR: Try to get ear from empty list. Possible reason: incorrect polygon vertices direction'
            
        save(output_file, triangles, None)
        # p = Polygon(n=5, w=10, h=10)
        # save(fname, p.vertices, None)
        # vertices = p.vertices
    else:
        points = load(args.input)
        vertices = Polygon(points=points).vertices
        triangles, error = triangulate(vertices)
        save(args.output, triangles, error)
    