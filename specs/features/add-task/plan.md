# Implementation Plan: Add Task

## 1. Overview
This plan details the steps required to implement the "Add Task" feature. The implementation will strictly follow the project constitution, prioritizing simplicity, readability, and the use of only built-in Python libraries. It covers creating the data structure for a task, implementing the logic to add it, and connecting it to the main user menu.

**Constitutional Alignment**:
- **Extreme Simplicity**: The implementation will use basic Python constructs.
- **No External Dependencies**: Only standard Python libraries will be used.
- **Strict Spec-Driven Development**: This plan is derived directly from `specs/features/add-task.md`.

## 2. Components & Files Affected
- `models.py`: This new file will define the `Task` data structure.
- `todo.py`: This new file will contain the `TodoManager` class, which will include the `add_task` method.
- `main.py`: This new file will handle the main menu loop and user input/output, calling `TodoManager` to perform actions.

## 3. Step-by-Step Implementation Plan

**Step 1: Define `Task` Data Structure (`models.py`)**
- Create a new file `models.py`.
- Inside `models.py`, define a `Task` class (or dataclass) to hold task data.
- The structure will include `id: int`, `title: str`, `description: str`, and `completed: bool`.

**Step 2: Create `TodoManager` (`todo.py`)**
- Create a new file `todo.py`.
- Define a `TodoManager` class.
- In the constructor (`__init__`), initialize an empty list to store tasks (e.g., `self.tasks = []`) and a counter for the next available ID (e.g., `self.next_id = 1`).

**Step 3: Implement `add_task` Method (`todo.py`)**
- Within `TodoManager`, create a method `add_task(self, title: str, description: str) -> Task:`.
- This method will:
  1. Create a new `Task` instance.
  2. Assign `self.next_id` to the task's `id`.
  3. Add the new task to the `self.tasks` list.
  4. Increment `self.next_id`.
  5. Return the newly created task.

**Step 4: Handle Menu Option in `main.py`**
- Create a new file `main.py`.
- Implement the main application loop that displays the menu.
- When the user selects option 1 ("Add task"):
  1. Prompt the user for the `title`.
  2. Validate that the `title` is not empty (after stripping whitespace). If it is, show an error and loop back to the prompt.
  3. Prompt the user for the `description`.
  4. Instantiate `TodoManager`.
  5. Call the `todo_manager.add_task()` method with the user's input.

**Step 5: Show Confirmation**
- After the `add_task` method returns, `main.py` will display a confirmation message to the user, such as `Success: Task '[Task Title]' added.`.
- The application will then loop back to display the main menu.

## 4. High-Level Code Structure

**`models.py`**
```python
# Option 1: Using dataclasses
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool = False
```

**`todo.py`**
```python
from models import Task
from typing import List

class TodoManager:
    def __init__(self):
        # self.tasks: List[Task] = []
        # self.next_id: int = 1
        pass

    def add_task(self, title: str, description: str) -> Task:
        # ... implementation ...
        pass
```

**`main.py`**
```python
from todo import TodoManager

def main():
    # todo_manager = TodoManager()
    # while True:
        # print menu
        # choice = input(...)
        # if choice == '1':
            # title = input(...)
            # description = input(...)
            # if title.strip():
                # task = todo_manager.add_task(...)
                # print confirmation
            # else:
                # print error
        # ...
```
**Data Flow**: `main.py` (UI) -> `TodoManager` (Logic) -> `Task` (Data Model)

## 5. Error Handling Strategy
- **Empty Title**: Input for the task title will be validated in `main.py`. The `strip()` method will be used to check for titles containing only whitespace. If validation fails, the message "Error: Title cannot be empty." will be displayed.
- **Other Inputs**: For Phase I, no other complex validation is required.

## 6. SOLID Compliance
- **Single Responsibility Principle (SRP)**: The architecture respects SRP:
  - `models.py` is responsible only for data structure.
  - `todo.py` is responsible only for business logic (managing tasks).
  - `main.py` is responsible only for user interaction (display and input).
- **Dependency Inversion Principle (DIP)**: `main.py` depends on the `TodoManager` abstraction, not its concrete implementation details.

## 7. Manual Testing Steps
1. Run `main.py`.
2. Select option '1' from the menu.
3. At the title prompt, press Enter without typing. Verify the error "Error: Title cannot be empty." is shown.
4. Enter a title containing only spaces. Verify the same error is shown.
5. Enter a valid title (e.g., "My First Task").
6. Enter a description (e.g., "This is the description.").
7. Verify the confirmation message "Success: Task 'My First Task' added." is displayed.
8. (Future step) Run the "List Tasks" feature and verify the new task appears with the correct ID (1), title, description, and a status of "Incomplete".
