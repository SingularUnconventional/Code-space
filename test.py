from dataclasses import dataclass

import numpy as np


WORLD_WIDTH_SCALE = 50
WORLD_HIGHT_SCALE = 50

PLAYERS_SIZE		= 50
PLAYER_MAX_HP		= 200
PLAYER_MAX_ENERGY	= 200
PLAYER_MAX_SPEED	= 3
PLAYER_BMR_ENERGY	= 3

FOODS_SIZE			= 30
FOOD_START_ENERGY	= 30

SUBSTANCE_A_ENERGY	= 1


@dataclass
class Color:
	r : int #0-255
	g : int #0-255
	b : int #0-255

class Vector2:...
@dataclass
class Vector2:
	x : int
	y : int

	def __add__(self, vector : Vector2) -> Vector2:
		return Vector2(self.x + vector.x, self.y + vector.y)

	
class World:
	def __init__(self):
		self.players: list[Player] 	= []
		self.foods 	: list[_Food] 	= []

		for _ in range(PLAYERS_SIZE):
			player = Player(Vector2(
							np.random.uniform(WORLD_WIDTH_SCALE), 
							np.random.uniform(WORLD_HIGHT_SCALE)
							))
			
			self.players.append(player)
		
		for _ in range(FOODS_SIZE):
			food = _Food()
			food.regenerate()

			self.foods.append(food)
			
	def Trun(self):
		for player in self.players:
			player.move()

		self.players = [player for player in self.players if player.alive]

	def __str__(self):
		grid = [["⬛"
				for _ in range(WORLD_WIDTH_SCALE)]
		  		for _ in range(WORLD_HIGHT_SCALE)]
		
		for player in self.players:
			yPos = int(player.position.y % WORLD_WIDTH_SCALE)
			xPos = int(player.position.x % WORLD_HIGHT_SCALE)
			
			grid[yPos][xPos] = "🟦🟪⬜🟨🟧🟥"[int((5*player.energy)/(player.energy+1000))]

		for food in self.foods:
			yPos = int(food.position.y)
			xPos = int(food.position.x)
			
			grid[yPos][xPos] = "🟩"

		return "⬜️"*WORLD_WIDTH_SCALE+"\n"+"\n".join(["".join(x_line) for x_line in grid])


class Player:
	def __init__(self, position : Vector2):
		self.speciesId	: Color
		self.position	: Vector2	= position
		self.hp			: int
		self.maxEnergy	: int
		self.breedEnergy: int
		self.energy		: int
		self.speed		: float
		self.alive 		: bool		= True

		self.set_value()
	
	def move(self):
		closestFood = world.foods[
		find_closest_point_arg(
			points=np.array([[food.position.x, food.position.y] for food in world.foods]),
			target=np.array([self.position.x, self.position.y])
		)]

		foodLocalPosX = closestFood.position.x - self.position.x
		foodLocalPosY = closestFood.position.y - self.position.y

		Scale = self.speed / (np.abs(foodLocalPosX) + np.abs(foodLocalPosY))

		self.position += Vector2(foodLocalPosX*Scale, foodLocalPosY*Scale)
		self.eat()

		if True: self.energy += SUBSTANCE_A_ENERGY
		self.energy -= PLAYER_BMR_ENERGY
		if self.energy < 0:
			self.alive = False


	def eat(self):
		foodLength, foodNum = find_closest_point(
			points=np.array([[food.position.x, food.position.y] for food in world.foods]),
			target=np.array([self.position.x, self.position.y])
		)

		food = world.foods[foodNum]

		if foodLength < 1:
			self.energy += food.energy
			food.regenerate()

	def set_value(self):
		self.speciesId 	= Color(np.random.randint(256), np.random.randint(256), np.random.randint(256))
		self.hp			= np.random.randint(PLAYER_MAX_HP)
		self.maxEnergy	= np.random.randiht(PLAYER_MAX_ENERGY)
		self.breedEnergy= np.random.randint(self.maxEnergy)
		self.energy		= np.random.randint(self.maxEnergy)
		self.speed		= np.random.uniform(PLAYER_MAX_SPEED)

	def breed(self):
		if self.energy > self.breedEnergy:
			...

#임시
class _Food:
	def __init__(self):
		self.position	: Vector2
		self.energy		: int = FOOD_START_ENERGY

	def regenerate(self):
		self.position = Vector2(
						np.random.uniform(WORLD_WIDTH_SCALE), 
					   	np.random.uniform(WORLD_HIGHT_SCALE))

	
def find_closest_point_arg(points: np.array, target: np.array) -> int:
	dists = np.sum((points - target)**2, axis=1)
	return np.argmin(dists)

def find_closest_point(points: list[Vector2], target: Vector2):
	dists = np.sum((points - target)**2, axis=1)
	return np.min(dists), np.argmin(dists)

def Loop():
	world.Trun()

	input(world)

if __name__ == "__main__":
	np.random.seed(394900038)
	world = World()
	while True:
		Loop()