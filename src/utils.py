import argparse
import csv
import matplotlib.pyplot as plt


def register_launch_arguments():
    parser = argparse.ArgumentParser(description='Serve the app')
    parser.add_argument('-i', '--input', help='specify input file', default='./data/in.csv')
    parser.add_argument('-o', '--output', help='specify output file', default='./data/out.csv')
    parser.add_argument('-t', '--test', help='run tests', action='store_true')

    return parser.parse_args()

def load(input_file):
    points = []
    with open(input_file) as input:
        vertices = csv.reader(input)
        for point in vertices:
               points.append([ int(point[0]), int(point[1]) ])

    return points

def save(output_file, triangles, error):
    with open(output_file, 'w', newline='', encoding='utf-8') as output:
        if error != None:
            output.write(error)
        else:
            writer = csv.writer(output)
            writer.writerows(triangles)

def draw_polygon(shape, fname):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    shape = plt.Polygon(shape, color='g', alpha=0.3)
    ax.add_patch(shape)
    plt.plot()
    # plt.show()
    plt.savefig(fname)