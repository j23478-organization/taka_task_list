import random

class TaskId:
	id: int

	def __init__(self):
		self.id = random.randint(1, 100)