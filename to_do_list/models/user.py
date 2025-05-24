from models.task import Task, TaskManager


class Users:

    def __init__(
        self, id: int, username: str, email: str, password: str, is_active: bool = True
    ):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.is_active = is_active


class RegularUser(Users):
    def __init__(
        self,
        id: int,
        username: str,
        email: str,
        password: str,
        is_active: bool = True,
        task_manager: TaskManager = TaskManager(),
    ):
        super().__init__(id, username, email, password, is_active)
        self.task_manager = task_manager

    def finish_task(self, task: Task):

        task.done = True
        return f"Task{task.title} done successfully"

    def view_task(self):
        return


class Admin(Users):

    def __init__(
        self,
        id: int,
        username: str,
        email: str,
        password: str,
        is_active: bool = True,
        task_manager: TaskManager = TaskManager(),
    ):
        super().__init__(id, username, email, password, is_active)
        self.task_manager = task_manager

    def create_task(self, title: str, create_by, RegularUser, done=False):
        self.done = done
        create_by = self.username

        task = Task(title=title, create_by=create_by, doer=RegularUser, done=False)
        self.task_manager.add(task)
        return f"Task {task} created successfully"

    def delete_task(self, title: str):
        self.title = title
        self.task_manager.remove(self.title)
        return f"Task {self.title} deleted successfully"
