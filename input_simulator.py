
"""Program that outputs a line from "input_simulator" file.
input() will output a new line every time you call it.
Only run it for as many lines you have in the file

"""


def input_generator_initiation(): 
    global idx
    idx = 0
    read_file()

def read_file():
    global line_list
    line_list = []
    file = open("input.txt")
    for line in file:
        line_list.append(line.strip().strip("\n"))
    file.close()

def input():
    global idx
    global line_list
    if idx != len(line_list):
        sim_input = line_list[idx]
        idx += 1
        return sim_input
    else:
        raise Exception('No more lines in file!')

input_generator_initiation()
