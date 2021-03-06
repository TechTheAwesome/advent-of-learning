import array
from ast import parse
import os
from tkinter.tix import Tree
from typing import List


with open(os.path.dirname(__file__) + '/input.txt') as txt:
	lines = txt.readlines()
# with 'input' as array of lines

ON     = 'turn on'
OFF    = 'turn off'
TOGGLE = 'toggle'

def parseInstruction(string):
	handle = string.replace(ON,"").replace(OFF, "").replace(TOGGLE, "").strip().split(' through ')
	return parseCord(handle)
size = 1000
grid = [[False for _ in range(size)] for _ in range(size)]

def parseCord(arr):
	res = []
	for cord in arr:
		c = cord.split(',')
		res.append([int(c[0]), int(c[1])])
	return res

def getPos(cords: array):
	res = []
	for x in range(cords[0][0], cords[1][0] +1):
		for y in range(cords[0][1], cords[1][1] +1):
			res.append([x, y])
	return res

def applyGrid(grid: array, cords, apply: bool):
	for pos in getPos(cords):
		grid[pos[0]][pos[1]] += apply
		if grid[pos[0]][pos[1]] < 0:
			grid[pos[0]][pos[1]] = 0
	return grid

for instruction in lines:
	cords = parseInstruction(instruction)
	if instruction.find(ON) == 0:
		applyGrid(grid, cords, 1)
	elif instruction.find(OFF) == 0:
		applyGrid(grid, cords, -1)
	elif instruction.find(TOGGLE) == 0:
		applyGrid(grid, cords, 2)
total = 0
for row in grid:
	total += sum(row)

print(total)