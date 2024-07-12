from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Завершено" if self.completed else "В процессе"
        return f"[{status}] {self.description} (Дата: {self.due_date})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        due_date_dt = datetime.strptime(due_date, "%Y-%m-%d")
        task = Task(description, due_date_dt)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print(f"Task index {task_index} is out of range.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def print_pending_tasks(self):
        pending_tasks = self.get_pending_tasks()
        if pending_tasks:
            print("Текущие задачи:")
            for i, task in enumerate(pending_tasks):
                print(f"{i}: {task}")
        else:
            print("Нет текущих задач.")

    def print_all_tasks(self):
        if self.tasks:
            print("Все задачи:")
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")
        else:
            print("Задачи отсутствуют.")

# Пример использования:
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Съездить за продуктами", "2024-07-12")
    manager.add_task("Выполнить домашнее задание урока OB01", "2024-07-12")
    manager.add_task("Забрать куст, отвезти на дачу", "2024-07-12")

    print("Начальный список задач:")
    manager.print_all_tasks()

    manager.mark_task_as_completed(1)

    print("\nОдна задача выполнена, остались задачи:")
    manager.print_all_tasks()

 #   print("\nPending tasks:")
    manager.print_pending_tasks()
