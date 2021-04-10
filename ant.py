# April 10th 2021, alexis forestier
# 
# a simple Langton's ant implementation using matplotlib.animation 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time


class Ant:

	dirs = ['e','n','w','s'] # east, north, west, south
	
	def __init__(self, init_pos = (0,0)):
		self.coord = init_pos
		self.dir = self.dirs[0]
	
	def tleft(self):
		self.dir = self.dirs[(self.dirs.index(a.dir) + 1) % 4]
	
	def tright(self):
		self.dir = self.dirs[(self.dirs.index(a.dir) - 1) % 4]
	
	def go_pbc(self, GRID_SIZE):
		if self.dir == 'e':
			self.coord = tuple(map(lambda i, j: (i + j) % GRID_SIZE, self.coord, (1,0))) 
		if self.dir == 'n':
			self.coord = tuple(map(lambda i, j: (i + j) % GRID_SIZE, self.coord, (0,1)))
		if self.dir == 'w':
			self.coord = tuple(map(lambda i, j: (i + j) % GRID_SIZE, self.coord, (-1,0)))
		if self.dir == 's':
			self.coord = tuple(map(lambda i, j: (i + j) % GRID_SIZE, self.coord, (0,-1)))

def run(frame, grid):
	if grid[a.coord] == True:
		grid[a.coord] = not grid[a.coord]
		a.tright()
		a.go_pbc(GRID_SIZE)
	else:
		grid[a.coord] = not grid[a.coord]
		a.tleft()
		a.go_pbc(GRID_SIZE)
	imgrid.set_data(grid)
	title.set_text("frame = {}, a.coord = {}".format(frame, a.coord))
	return (imgrid, title)


if __name__ == '__main__':
	
	GRID_SIZE = 100
	grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype='bool')

	fig, ax = plt.subplots()
	imgrid = plt.imshow(grid, interpolation='None', vmin=False, vmax=True)
	title = ax.text(.04,.93, "", color='k', fontsize=13,
			bbox={'facecolor':'w', 'alpha':0.3, 'pad':4}, transform = ax.transAxes)

	a = Ant((int(GRID_SIZE/2), int(GRID_SIZE/2)))

	output = anim.FuncAnimation(fig, run, fargs=(grid,), interval=1, blit=True)
	plt.show()