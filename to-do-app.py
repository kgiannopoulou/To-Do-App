class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"Task {i}:")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Priority: {task.priority}")
                print(f"Due Date: {task.due_date}")
                print(f"Status: {'Completed' if task.completed else 'Pending'}")
                print()

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")


def main():
    todo_app = ToDoApp()

    while True:
        print("\n===== To-Do App =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, priority, due_date)
            todo_app.add_task(task)
        elif choice == "2":
            todo_app.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as completed: "))
            todo_app.complete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            todo_app.delete_task(task_number)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")


if __name__ == "__main__":
    main()
