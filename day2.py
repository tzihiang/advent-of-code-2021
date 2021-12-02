import sys

horizontal_dist = 0
depth = 0
aim = 0

f = open(sys.argv[1], "r")

for line in f.readlines():
    line_list = line.split("\n")[0].split(" ")
    direction = line_list[0]
    dist = int(line_list[1])
    print(line_list)
    if (direction=="forward"):
        horizontal_dist += dist
        depth += aim*dist
    elif (direction=="up"):
        aim -= dist
    elif (direction=="down"):
        aim += dist

print(horizontal_dist*depth)