from .task import Task

class Project:
    name: str
    tasks: list[Task]
    
    def __init__(self, name):
        self.name = name
        self.tasks = []
        
class ReadOnlyList:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)
        

class ReadOnlyProject(Project):
    def __init__(self, p: Project):
        self.__inner_p = p
    
	
    @property
    def name(self):
        return self.__inner_p.namne
    
    @property
    def tasks(self):
        return ReadOnlyList(self.__inner_p.tasks)