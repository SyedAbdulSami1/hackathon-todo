# Feature Specification: Add Task

**Feature Branch**: `1-add-task`  
**Created**: 2026-01-04  
**Status**: Draft  
**Input**: User description: "Feature: Add Task"

## 1. Feature Summary
This feature allows a user to add a new task to the in-memory todo list. The user will be prompted to enter a title and a description for the task, which is then created and stored.

## 2. User Story
As a user, I want to add a new task with a title and description, so that I can keep track of what I need to do.

## 3. Scope
**IN SCOPE**:
- Prompting the user for a new task's title and description.
- Creating a new task object in memory.
- Assigning a unique, auto-incrementing ID to the new task.
- Adding the new task to the in-memory list.
- Displaying a success confirmation message to the user.

**NOT IN SCOPE**:
- Editing or deleting a task.
- Setting due dates, priorities, or tags.
- Persisting tasks to a file or database.
- Listing tasks (this is a separate feature).

## 4. Functional Requirements
- **FR-001**: The system MUST provide an option in the main menu to "Add a new task".
- **FR-002**: When selected, the system MUST prompt the user to enter a title for the task.
- **FR-003**: The system MUST then prompt the user to enter a description for the task.
- **FR-004**: The system MUST validate that the title is not empty. If it is, an error message "Error: Title cannot be empty." MUST be displayed, and the process should restart.
- **FR-005**: Upon receiving a valid title and description, the system MUST create a `Task` object.
- **FR-006**: The system MUST assign a new, unique, and sequential integer ID to the task, starting from 1.
- **FR-007**: The newly created task MUST be added to the global in-memory list of tasks.
- **FR-008**: The system MUST display a confirmation message, "Success: Task '[Task Title]' added."

## 5. Data Model Impact
The feature will create instances of a `Task` object with the following fields:
- `id`: `int` (Unique, sequential identifier)
- `title`: `str` (User-provided title)
- `description`: `str` (User-provided description)
- `completed`: `bool` (Defaulted to `False`)

Tasks will be stored in a simple Python `list` in memory.

## 6. Acceptance Criteria
- **AC-001**: A user can select the "Add Task" option from the menu and is prompted for a title and description.
- **AC-002**: A task with a non-empty title and a description is successfully added to the in-memory list.
- **AC-003**: Each new task is assigned a unique ID, starting from 1 and incrementing for each subsequent task.
- **AC-004**: An attempt to add a task with an empty title results in an error message, and the task is not added.
- **AC-005**: After a task is successfully added, a confirmation message is displayed containing the task's title.

## 7. Out of Scope
- Persisting tasks to disk.
- Adding priorities, tags, or due dates.
- Allowing multi-line descriptions.
- Updating or deleting existing tasks.
- Batch adding multiple tasks.
