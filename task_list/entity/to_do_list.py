from .project import Project



class ToDoList:
    projects: list[Project]

    def __init__(self):
        self.projects = []
    
    def get(self, key):
        for project in self.projects:
            if project.name == key:
                return project.tasks
        return None
    
    def items(self):
        return ((project.name, project.tasks) for project in self.projects)
    
    def __setitem__(self, key, value):
        project = Project(key)
        self.projects.append(project)