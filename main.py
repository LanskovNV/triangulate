import argparse
import csv
from earcut import Earcut


def register_launch_arguments():
    parser = argparse.ArgumentParser(description='Serve the app')
    parser.add_argument('-i', '--input', help='specify input file', default='./data/in3.csv')
    parser.add_argument('-o', '--output', help='specify output file', default='./data/out.csv')

    return parser.parse_args()

def parse_input(input_file):
    points = []
    with open(input_file) as input:
        vertices = csv.reader(input)
        for point in vertices:
               points.append([ int(point[0]), int(point[1]) ])
    return points

def save_ans(output_file, triangles, error):
    if error != None:
        data = [error]
    else:
        data = triangles
    with open(output_file, 'w', newline='', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerows(data)

if __name__ == '__main__':
    args = register_launch_arguments()
    error = None

    try:
        vertices = parse_input(args.input)
        earcut = Earcut(vertices)
        earcut.triangulate()
        triangles = earcut.triangles
    except ValueError:
        error = 'ERROR: Incorrect input'

    save_ans(args.output, triangles, error)