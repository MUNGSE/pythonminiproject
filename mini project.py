import pickle

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.title}\nDescription: {self.description}\nStatus: {status}\n"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_as_completed(self, task):
        task.mark_as_completed()

    def save_tasks(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self, filename):
        with open(filename, "rb") as file:
            self.tasks = pickle.load(file)

    def __str__(self):
        if not self.tasks:
            return "No tasks found."
        return "\n".join(str(task) for task in self.tasks)


def display_menu():
    print("===== Task Manager Menu =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("0. Exit")


def main():
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            task_manager.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            print(task_manager)
            task_index = int(input("Enter the index of the task to remove: "))
            try:
                task = task_manager.tasks[task_index]
                task_manager.remove_task(task)
                print("Task removed successfully.")
            except IndexError:
                print("Invalid task index.")

        elif choice == "3":
            print(task_manager)
            task_index = int(input("Enter the index of the task to mark as completed: "))
            try:
                task = task_manager.tasks[task_index]
                task_manager.mark_task_as_completed(task)
                print("Task marked as completed.")
            except IndexError:
                print("Invalid task index.")

        elif choice == "4":
            print(task_manager)

        elif choice == "5":
            filename = input("Enter the filename to save tasks: ")
            task_manager.save_tasks(filename)
            print("Tasks saved successfully.")

        elif choice == "6":
            filename = input("Enter the filename to load tasks: ")
            try:
                task_manager.load_tasks(filename)
                print("Tasks loaded successfully.")
            except FileNotFoundError:
                print("File not found.")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

