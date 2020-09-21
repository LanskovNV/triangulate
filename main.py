import argparse
import csv
import numpy as np

from ear import Ear


def register_launch_arguments():
    parser = argparse.ArgumentParser(description='Serve the app')
    parser.add_argument('-i', '--input', help='specify input file', default='./data/in.csv')
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

# vertices shoutd go in counterclock-wise
def earcut(vertices):
    length = len(vertices)
    triangles = []
    ears = []

    def find_ears():
        i = 0
        while True:
            if i >= length:
                break
            new_ear = Ear(vertices, i)
            if (new_ear.validate()):
                ears.append(new_ear)
            i += 2

    
    def update_ears(ear):
        pass

    def cut_ear():
        ear = ears.pop(0)
        triangles.append(ear.get_triangle())
        update_ears(ear)

    # main triangulation block
    find_all_ears()
    while True:
        if len(ears) == 1:
            add_triangle(ears[0])
            break    
        cut_ear()

    return triangles

if __name__ == '__main__':
    args = register_launch_arguments()
    error = None

    try:
        vertices = parse_input(args.input)
        triangles = earcut(vertices)
    except ValueError:
        error = 'ERROR: Incorrect input'

    save_ans(args.output, triangles, error)