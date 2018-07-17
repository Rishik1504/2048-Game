import random
import pygame
from texttable import Texttable

class Grid2048:

	def __init__(self):
		self.grid = [[0 for i in range(4)] for j in range(4)]

	def initiate(self):

		for i in range(4):
			for j in range(4):
				self.grid[i][j] = 0

		sq1 = self.ChooseRandomSquare()
		self.grid[sq1[0]][sq1[1]] = sq1[2]

		sq2 = self.ChooseRandomSquare()
		self.grid[sq2[0]][sq2[1]] = sq2[2]

	def ChooseRandomSquare(self):

		possibilities = []
		twoORfour = [2, 2, 2, 4]

		for i in range(4):
			for j in range(4):
				if self.grid[i][j] == 0:
					possibilities.append([i, j])

		val = random.choice(possibilities)
		val.append(random.choice(twoORfour))

		return val

	def moveUp(self):
		flag = False
		for i in range(4):
			for j in range(4):
				if self.grid[i][j] != 0:
					k = i
					val = self.grid[i][j]
					while k > 0:
						k -= 1
						if self.grid[k][j] != 0 and self.grid[k][j] == val:
							self.grid[k+1][j] = 0
							self.grid[k][j] *= 2
							flag = True
							break
						elif self.grid[k][j] != 0:
							break

						flag = True
						self.grid[k][j] = val
						self.grid[k+1][j] = 0

		if flag:				
			sq = self.ChooseRandomSquare()
			self.grid[sq[0]][sq[1]] = sq[2]

	def moveDown(self):
		flag = False
		for i in range(3, -1, -1):
			for j in range(3, -1, -1):
				if self.grid[i][j] != 0:
					k = i
					val = self.grid[i][j]
					while k < 3:
						k += 1
						if self.grid[k][j] != 0 and self.grid[k][j] == val:
							self.grid[k-1][j] = 0
							self.grid[k][j] *= 2
							flag = True
							break
						elif self.grid[k][j] != 0:
							break

						flag = True
						self.grid[k][j] = val
						self.grid[k-1][j] = 0
		if flag:
			sq = self.ChooseRandomSquare()
			self.grid[sq[0]][sq[1]] = sq[2]

	def moveLeft(self):
		flag = False
		for i in range(4):
			for j in range(4):
				if self.grid[i][j] != 0:
					k = j
					val = self.grid[i][j]
					while k > 0:
						k -= 1
						if self.grid[i][k] != 0 and self.grid[i][k] == val:
							self.grid[i][k+1] = 0
							self.grid[i][k] *= 2
							flag = True
							break
						elif self.grid[i][k] != 0:
							break
						flag = True
						self.grid[i][k] = val
						self.grid[i][k+1] = 0
		if flag:
			sq = self.ChooseRandomSquare()
			self.grid[sq[0]][sq[1]] = sq[2]


	def moveRight(self):
		flag = False
		for i in range(3, -1, -1):
			for j in range(3, -1, -1):
				if self.grid[i][j] != 0:
					k = j
					val = self.grid[i][j]
					while k < 3:
						k += 1
						if self.grid[i][k] != 0 and self.grid[i][k] == val:
							self.grid[i][k-1] = 0
							self.grid[i][k] *= 2
							flag = True
							break
						elif self.grid[i][k] != 0:
							break
						flag = True
						self.grid[i][k] = val
						self.grid[i][k-1] = 0

		if flag:
			sq = self.ChooseRandomSquare()
			self.grid[sq[0]][sq[1]] = sq[2]

	def moveRightCheck(self):
		for i in range(3, -1, -1):
			for j in range(3, -1, -1):
				if self.grid[i][j] != 0:
					k = j
					val = self.grid[i][j]
					while k < 3:
						k += 1
						if self.grid[i][k] != 0 and self.grid[i][k] == val:
							return True
						elif self.grid[i][k] != 0:
							break
						return True

		return False

	def moveLeftCheck(self):
		for i in range(4):
			for j in range(4):
				if self.grid[i][j] != 0:
					k = j
					val = self.grid[i][j]
					while k > 0:
						k -= 1
						if self.grid[i][k] != 0 and self.grid[i][k] == val:
							return True
						elif self.grid[i][k] != 0:
							break
						return True
		return False

	def moveDownCheck(self):
		for i in range(3, -1, -1):
			for j in range(3, -1, -1):
				if self.grid[i][j] != 0:
					k = i
					val = self.grid[i][j]
					while k < 3:
						k += 1
						if self.grid[k][j] != 0 and self.grid[k][j] == val:
							return True
						elif self.grid[k][j] != 0:
							break
						return True

		return False

	def moveUpCheck(self):
		for i in range(4):
			for j in range(4):
				if self.grid[i][j] != 0:
					k = i
					val = self.grid[i][j]
					while k > 0:
						k -= 1
						if self.grid[k][j] != 0 and self.grid[k][j] == val:
							return True
						elif self.grid[k][j] != 0:
							break

						return True
		return False

	def checkGrid(self):

		if self.moveRightCheck() or self.moveLeftCheck() or self.moveUpCheck() or self.moveDownCheck():
			return True

		return False

	def printGrid(self):

		t = Texttable()
		for i in self.grid:
			row = i[:]
			for j in range(4):
				if i[j] == 0:
					row[j] = ''
			t.add_row(row)

		print t.draw()

def main():

	print "Hello! Welcome to 2048!"
	print "The Game Starts NOW:"
	print

	pygame.init()
	screen = pygame.display.set_mode((1, 1))


	G = Grid2048()
	G.initiate()
	G.printGrid()
	print

	while True:
		if G.checkGrid() == False:
			print "Game Over!"
			return 
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == 273:
					G.moveUp()
				elif event.key == 274:
					G.moveDown()
				elif event.key == 276:
					G.moveLeft()
				elif event.key == 275:
					G.moveRight()
				elif event.key == 27:
					return
				G.printGrid()
				print

main()