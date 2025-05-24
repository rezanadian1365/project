from models.user import Admin, RegularUser
from models.task import Task, TaskManager


def main():
    # Create a user object

    tm = TaskManager()
    u1 = RegularUser(1, "john", "john@gmail.com", "1234", True, task_manager=tm)

    a1 = Admin(4, "reza", "reza@gmail.com", "1234", True, task_manager=tm)
    task1 = Task("Task", a1, u1, False)

    print(u1.username, u1.email, u1.password, u1.is_active)

    a1.create_task("Task1", a1, u1)
    a1.create_task("Task2", a1, u1)
    print(a1.task_manager, "-1")
    print("_" * 50)
    a1.delete_task("Task2")
    print("_" * 50)
    print(a1.task_manager)
    print("_" * 50)

    print("_" * 50)
    print(u1.finish_task(task1))
    print(task1.done)

    # print(task1)


if __name__ == "__main__":
    main()
