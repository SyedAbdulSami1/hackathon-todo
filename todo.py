from typing import List
from models import Task

class TodoManager:
    """Manages all the operations for the to-do list."""

    def __init__(self):
        """Initializes the TodoManager with an empty list of tasks and a starting ID."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str) -> Task:
        """
        Creates and adds a new task to the list.

        Args:
            title: The title of the task.
            description: The description of the task.

        Returns:
            The newly created task.
        """
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """
        Returns the list of all tasks.

        Returns:
            A list of all Task objects.
        """
        return self.tasks
