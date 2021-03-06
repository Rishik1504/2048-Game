import random, pygame, os, pickle
from texttable import Texttable
import copy

class Grid2048:

	def __init__(self):
		self.grid = [[0 for i in range(4)] for j in range(4)]
		self.score = [0]
		self.history = []

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
		available = set([0, 1, 2, 3])
		for i in range(4):
			for j in range(4):
				if self.grid[i][j] != 0:
					k = i
					val = self.grid[i][j]
					while k > 0:
						k -= 1
						if self.grid[k][j] != 0 and self.grid[k][j] == val and k in available:
							self.grid[k+1][j] = 0
							self.grid[k][j] *= 2
							self.score.append(self.grid[k][j] + self.score[-1])
							available.remove(k)
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
		available = set([0, 1, 2, 3])
		for i in range(3, -1, -1):
			for j in range(3, -1, -1):
				if self.grid[i][j] != 0:
					k = i
					val = self.grid[i][j]
					while k < 3:
						k += 1
						if self.grid[k][j] != 0 and self.grid[k][j] == val and k in available:
							self.grid[k-1][j] = 0
							self.grid[k][j] *= 2
							self.score.append(self.grid[k][j] + self.score[-1])
							available.remove(k)
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
		available = set([0, 1, 2, 3])
		for i in range(4):
			for j in range(4):
				if self.grid[i][j] != 0:
					k = j
					val = self.grid[i][j]
					while k > 0:
						k -= 1
						if self.grid[i][k] != 0 and self.grid[i][k] == val and k in available:
							self.grid[i][k+1] = 0
							self.grid[i][k] *= 2
							self.score.append(self.grid[i][k] + self.score[-1])
							available.remove(k)
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
		available = set([0, 1, 2, 3])
		for i in range(3, -1, -1):
			for j in range(3, -1, -1):
				if self.grid[i][j] != 0:
					k = j
					val = self.grid[i][j]
					while k < 3:
						k += 1
						if self.grid[i][k] != 0 and self.grid[i][k] == val and k in available:
							self.grid[i][k-1] = 0
							self.grid[i][k] *= 2
							self.score.append(self.grid[i][k] + self.score[-1])
							available.remove(k)
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

		for i in range(4):
			for j in range(4):
				if self.grid[i][j] == 2048:
					return None

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

	def showScore(self):
		return self.score[-1]

	def updateHighScore(self):

		try:
			f = open("HighScore.txt", 'r')
		except:
			f = open("HighScore.txt", 'w')
			f.write(str(0))
			f.close()
			f = open("HighScore.txt", 'r')

		highscore = int(f.readline())

		f.close()

		f = open("HighScore.txt", 'w')
		f.write(str(max(self.score[-1], highscore)))
		f.close()

	def storeHistory(self):

		self.history.append(copy.deepcopy(self.grid))

	def recallHistory(self):

		self.grid = self.history.pop()

	def recallScore(self):

		return self.score.pop()

def showHighScore():

	try:
		f = open("HighScore.txt", 'r')
		highscore = int(f.readline())
		f.close()
	except:
		highscore = 0

	return highscore

def main():

	print "Hello! Welcome to 2048!"
	print "The Game Starts NOW:"
	print

	pygame.init()
	screen = pygame.display.set_mode((1, 1))


	G = Grid2048()
	G.initiate()
	G.printGrid()
	print "Score:", G.showScore()
	print "High Score:", showHighScore()
	print

	try:
		os.remove("History.dat")
	except:
		pass

	dic = {"Up": 273, "Down":274, "Left":276, "Right": 275,
			"Esc":27, "BackSpace":8
			}

	G.storeHistory()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == dic["Up"]:
					G.storeHistory()
					G.moveUp()
					G.storeHistory()
				elif event.key == dic["Down"]:
					G.storeHistory()
					G.moveDown()
					G.storeHistory()
				elif event.key == dic["Left"]:
					G.storeHistory()
					G.moveLeft()
					G.storeHistory()
				elif event.key == dic["Right"]:
					G.storeHistory()
					G.moveRight()
					G.storeHistory()
				elif event.key == dic["Esc"]:
					return
				elif event.key == dic["BackSpace"]:
					G.recallHistory()
					G.recallHistory()
					G.recallScore()

				G.updateHighScore()

				G.printGrid()
				print "Score:", G.showScore()
				print "High Score:", showHighScore()
				print

				if G.checkGrid() == False:
					G.updateHighScore()
					print "Game Over!"
					return
				elif G.checkGrid() == None:
					G.updateHighScore()
					print "You Win!"
					return


main()