class Task:
    def __init__(self, title, create_by, doer, done=False):
        self.doer = doer
        self.create_by = create_by
        self.title = title
        self.done = done
        self.description = None

    def __str__(self):
        return f"Task(title={self.title}, create_by={self.create_by},done={self.done})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task: Task):
        self.tasks.append(task)
        return f"Task {task.title} added successfully"

    def remove(self, title: str):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                break
        return f"Task {title} removed successfully"

    def __str__(self):
        task_str = "\n".join([str(task) for task in self.tasks])
        return f"TaskManager(tasks=[\n{task_str}\n])"
