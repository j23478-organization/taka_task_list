from .project import Project
from .to_do_list_id import ToDoListId


class ToDoList:
    id: ToDoListId
    projects: list[Project]

    def __init__(self):
        self.id = ToDoListId()
        self.projects = []
    
    def get(self, key):
        for project in self.projects:
            if project.name == key:
                return project.tasks
        return None
    
    def get_projects(self):
        return
    
    def items(self):
        return ((project.name, project.tasks) for project in self.projects)
    
    def __setitem__(self, key, value):
        project = Project(key)
        self.projects.append(project)