from task_list.entity.task_id import TaskId

class Task:
    def __init__(self, id_: TaskId, description: str, done: bool) -> None:
        self.id = id_
        self.description = description
        self.done = done

    def set_done(self, done: bool) -> None:
        self.done = done

    def is_done(self) -> bool:
        return self.done