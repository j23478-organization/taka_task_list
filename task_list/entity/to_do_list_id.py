import random

class ToDoListId:
	id: int

	def __init__(self):
		self.id = random.randint(1, 100)