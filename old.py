#!/usr/bin/env python3
import sys


file_name = sys.argv[1]
f = open(file_name, 'r')
maze = f.read().split('\n')
f.close()

if len(maze[-1]) == 0:
    maze = maze[:-1]

def findStart(maze):
    for chr in maze[0]:
        if chr == ' ':
            return (maze[0].index(chr), 0)
    for line in maze:
        if line[0] == ' ':
            return (0, maze.index(line))
    # return (maze[0].index(' '), 0)


def findGoal(maze):
    for chr in maze[-1]:
        if chr == ' ':
            return (maze[-1].index(chr), len(maze) - 1)
    for line in maze:
        if line[-1] == ' ':
            return (len(line) - 1, maze.index(line))
    # return (maze[len(maze) - 1].index(' '), len(maze) - 1)


def findPath(maze, start):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [[start]]
    checked = set(start)
    while queue:
        path = queue.pop(0)
        last_x, last_y = path[-1]
        if (last_x, last_y) == findGoal(maze):
            return path

        for d in direction:
            x, y = last_x + d[0], last_y + d[1]
            if (
                0 <= x < len(maze[0]) and 0 <= y < len(maze) and
                maze[y][x] != '*' and (x, y) not in checked
               ):
                queue.append(path + [(x, y)])
                checked.add((x, y))


start = findStart(maze)
path = findPath(maze, start)
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if (x, y) not in path and maze[y][x] == ' ':
            maze[y] = maze[y][:x] + '*' + maze[y][x+1:]
for i in maze:
    print(i)
