# Task Breakdown: Add Task

## 1. Task List Overview
- **Total Tasks**: 6
- **Goal**: To implement the complete "Add Task" feature as defined in the feature specification and implementation plan, resulting in a functional, in-memory task creation capability.

## 2. Individual Tasks

### **T-001: Create `Task` Data Structure** (Completed)
- **Description**: Create the `Task` dataclass in `models.py` to represent a single todo item.
- **Files to Create/Modify**:
  - `models.py` (create)
- **Acceptance Criteria**:
  - The `models.py` file exists.
  - It contains a `Task` dataclass with the fields: `id: int`, `title: str`, `description: str`, and `completed: bool`.
  - The `completed` field defaults to `False`.
- **Reference**: `plan.md` (Step 1), `spec.md` (Section 5)

### **T-002: Initialize `TodoManager`** (Completed)
- **Description**: Create the `TodoManager` class in `todo.py` and initialize its state in the constructor.
- **Files to Create/Modify**:
  - `todo.py` (create)
- **Acceptance Criteria**:
  - The `todo.py` file exists.
  - It contains a `TodoManager` class.
  - The `__init__` method initializes `self.tasks` as an empty list and `self.next_id` as `1`.
- **Reference**: `plan.md` (Step 2)

### **T-003: Implement `add_task` Method** (Completed)
- **Description**: Implement the `add_task` method within the `TodoManager` class to handle the logic of creating and storing a new task.
- **Files to Create/Modify**:
  - `todo.py`
- **Acceptance Criteria**:
  - The `add_task` method correctly creates a `Task` instance with the provided title and description.
  - It assigns the current `next_id` to the new task and adds it to the `self.tasks` list.
  - `self.next_id` is incremented by 1 after the task is added.
  - The method returns the newly created `Task` object.
- **Reference**: `plan.md` (Step 3)

### **T-004: Add Menu Option in `main.py`** (Completed)
- **Description**: Create the main application entry point in `main.py` and implement the menu loop that displays the "Add task" option.
- **Files to Create/Modify**:
  - `main.py` (create)
- **Acceptance Criteria**:
  - The `main.py` file exists and runs without errors.
  - A menu is displayed to the user with "1. Add task" as an option.
  - The application waits for user input.
- **Reference**: `plan.md` (Step 4)

### **T-005: Handle User Input and Call `add_task`** (Completed)
- **Description**: In `main.py`, implement the logic to handle the user selecting option '1', prompt for input, and call the `TodoManager.add_task` method.
- **Files to Create/Modify**:
  - `main.py`
- **Acceptance Criteria**:
  - When the user inputs '1', the app prompts for a title and then a description.
  - Input for the title is validated to not be empty (after stripping whitespace). An error is shown if it is.
  - A `TodoManager` instance is created, and `add_task` is called with the user's input.
- **Reference**: `plan.md` (Step 4)

### **T-006: Display Confirmation Message** (Completed)
- **Description**: After a task is successfully created, display a confirmation message to the user.
- **Files to Create/Modify**:
  - `main.py`
- **Acceptance Criteria**:
  - Upon successful return from `add_task`, a message like "Success: Task '[Task Title]' added." is printed to the console.
  - The application then returns to the main menu.
- **Reference**: `plan.md` (Step 5), `spec.md` (FR-008)

## 3. Task Dependencies
- **T-002** depends on **T-001** (TodoManager needs the Task class).
- **T-003** depends on **T-001** and **T-002** (The method needs the class and the manager's state).
- **T-005** depends on **T-003** and **T-004** (It needs the menu to exist and the `add_task` method to call).
- **T-006** depends on **T-005**.

**Execution Order**: T-001 -> T-002 -> T-003 -> T-004 -> T-005 -> T-006

## 4. Final Verification
After all tasks are completed, the feature can be tested manually:
1. Run `python main.py`.
2. Select option '1'.
3. Test the empty title validation by pressing Enter.
4. Provide a valid title and description.
5. Verify the success message is displayed.
6. (Manual Check) Although not part of this feature, a temporary print statement could be added to `add_task` to verify the `self.tasks` list contains the new task object.