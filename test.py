from src.polygon import Polygon
from src.earcut import Earcut
from main import save_ans, parse_input
import matplotlib.pyplot as plt


def draw(shape):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    shape = plt.Polygon(shape, color='g', alpha=0.3)
    ax.add_patch(shape)
    plt.plot()
    plt.show()


if __name__ == '__main__':
    error = None
    triangles = []

    try:
        # p = Polygon(n=5, w=10, h=10)
        # save_ans('./data/rnd.csv', p.vertices, None)
        # vertices = p.vertices
        
        vertices = parse_input('./data/rnd.csv')

        # draw(vertices)
        
        earcut = Earcut(vertices)
        earcut.triangulate()
        triangles = earcut.triangles
    except ValueError:
        error = 'ERROR: Incorrect input'
    except IndexError:
        error = 'ERROR: Try to get ear from empty list. Possible reason: incorrect polygon vertices direction'
    save_ans('./data/out.csv', triangles, error)         
    