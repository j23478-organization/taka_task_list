from .task import Task

class Project:
    name: str
    tasks: list[Task]
    
    def __init__(self, name):
        self.name = name
        self.tasks = []