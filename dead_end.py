#!/usr/bin/env python3
import sys


if len(sys.argv) != 2:
    raise IOError('No file included.')


def readMaze():
    file_name = sys.argv[1]
    f = open(file_name, 'r')
    maze = f.read().split('\n')
    f.close()
    for line in maze:
        if len(line) == 0:
            maze.remove(line)
    return maze


def findStart(maze):
    for i in [0, -1]:
        if ' ' in maze[i]:
            return (maze[i].index(' '), maze.index(maze[i]))
    for line in maze:
        for i in [0, len(line) - 1]:
            if line[i] == ' ':
                return (i, maze.index(line))


def findGoal(maze, start):
    for i in [0, -1]:
        if ' ' in maze[i] and (maze[i].index(' '), maze.index(maze[i])) != start:
            return (maze[i].index(' '), maze.index(maze[i]))
    for line in maze:
        for i in [0, len(line) - 1]:
            if line[i] == ' ' and (i, maze.index(line)) != start:
                return (i, maze.index(line))


def findPath(maze, start):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [[start]]
    checked = set(start)
    way = []
    while queue:
        path = queue.pop(0)
        last_x, last_y = path[-1]
        if (last_x, last_y) == findGoal(maze, start):
            way.append(path)

        for d in direction:
            x, y = last_x + d[0], last_y + d[1]
            if (
                0 <= x < len(maze[0]) and 0 <= y < len(maze) and
                maze[y][x] != '*' and (x, y) not in checked
               ):
                queue.append(path + [(x, y)])
                checked.add((x, y))
    return way


available = set()
maze = readMaze()
start = findStart(maze)
path = findPath(maze, start)
for i in path:
    for ele in i:
        available.add(ele)
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if (x, y) not in available and maze[y][x] == ' ':
            maze[y] = maze[y][:x] + '*' + maze[y][x+1:]
for i in maze:
    print(i)
