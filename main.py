import argparse
import csv
# import numpy as np


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
    triangles = []
    ears = []

    def find_all_ears():
        i = 0
        length = len(vertices)
        while True:
            if i >= length:
                break
            if is_convex(vertices[i]): 
                ears.append(i)
                i += 2

    def convert_bounds(ind):
        length = len(vertices)
        right_neighbour_ind = (ind + 1) % length
        if ind == 0:
            left_neighbour_ind = length - 1
        else: 
            left_neighbour_ind = ind - 1
        return left_neighbour_ind, right_neighbour_ind

    def is_convex(vert):
        return True


    #TODO: fix this func
    def update_ears(ind):
        left_neighbour_ind, right_neighbour_ind = convert_bounds(ind)
        if is_convex(vertices[left_neighbour_ind]):
            ears.append(left_neighbour_ind)
            return
        if is_convex(vertices[right_neighbour_ind]):
            ears.append(right_neighbour_ind)
            return

    def add_triangle(ind):
        left_neighbour_ind, right_neighbour_ind = convert_bounds(ind)
        triangles.append([left_neighbour_ind, ind, right_neighbour_ind])

    def cut_ear():
        ear_ind = ears.pop(0)
        add_triangle(ear_ind)
        update_ears(ear_ind)

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