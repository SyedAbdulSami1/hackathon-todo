<!--
---
Sync Impact Report
---
Version Change: None -> 1.0.0
Principles Added:
  - I. Extreme Simplicity and Readability
  - II. No External Dependencies
  - III. Strict Spec-Driven Development
  - IV. Beginner-Friendly Code
Sections Added:
  - Project Overview
  - Core Principles
  - Code Quality Standards
  - Architecture Guidelines
  - User Experience
  - Constraints
  - Development Process
Templates Requiring Updates:
  - All templates will be checked for alignment with this initial constitution.
Follow-up TODOs: None
-->
# Hackathon II - Evolution of Todo (Phase I: In-Memory Console App) Constitution

## 1. Project Overview
This project is a simple, command-line Todo application built in Python for "Hackathon II - Evolution of Todo." All task storage is handled in-memory, meaning no data is persisted to files or a database upon exit. Phase I scope is strictly limited to five basic CRUD (Create, Read, Update, Delete) operations and a user-facing menu.

## 2. Core Principles

### I. Extreme Simplicity and Readability
All code MUST prioritize extreme simplicity and readability over clever or overly complex solutions. The goal is maintainable and understandable code.

### II. No External Dependencies
The project MUST only use built-in Python features. The inclusion of any external, third-party libraries is strictly forbidden.

### III. Strict Spec-Driven Development
No code may be written or modified without a corresponding feature specification document. Every implementation detail must trace back to an approved spec.

### IV. Beginner-Friendly Code
Code should be clean, well-documented, and easy for a beginner to understand. This includes clear naming, comments where necessary, and straightforward logic.

## 3. Code Quality Standards
- **Function Length:** Functions and methods should be short and focused, not exceeding 15 lines where possible.
- **Naming Conventions:** All variables, functions, and classes MUST have meaningful, descriptive names that clearly convey their purpose.
- **Type Hinting:** Type hints are REQUIRED for all class methods and public functions.
- **Documentation:** Docstrings are REQUIRED for all classes and public functions to explain their purpose, arguments, and return values.
- **Error Handling:** The application MUST implement basic, user-friendly error handling for common issues like invalid input or a task not being found.

## 4. Architecture Guidelines
- **Recommended Structure:** The project will adhere to the following structure to ensure a clear separation of concerns:
    - `models.py`: Contains the `Task` data class.
    - `todo.py`: Contains the `TodoManager` class, which handles all business logic for task operations.
    - `main.py`: Contains only the user-facing menu loop and handles all user interaction (input/output).
- **SOLID Principles:** SOLID principles, especially the Single Responsibility Principle (SRP), should be applied in a simple and practical manner.
- **Global State:** The use of global variables should be avoided wherever reasonably possible to improve predictability and reduce side effects.

## 5. User Experience
- **Clear Menu:** The application MUST present a clear, numbered console menu for all available actions.
- **User Feedback:** The system MUST provide friendly and explicit confirmation messages after successful operations and clear error messages when issues occur.
- **Task Display:** The task list view MUST display the task ID, title, completion status, and description for clarity.

## 6. Constraints
- **No External Libraries:** Reiteration of the core principle. The project is self-contained.
- **No Persistence:** Data is ephemeral and will be lost on application exit. This is a strict constraint for Phase I.
- **Limited Scope:** No advanced features beyond the five basic CRUD operations are to be implemented in Phase I.

## 7. Development Process
- **SpecifyPlus Workflow:** The project MUST strictly follow the SpecifyPlus flow: `specify` -> `plan` -> `tasks` -> `implement`.
- **Traceability:** Every change MUST be traceable back to a specification file.
- **History Records:** A Prompt History Record (PHR) MUST be created in the `history/prompts/` directory after each completed development session to ensure full traceability.

## Governance

This Constitution is the supreme governing document for this project. It supersedes all other practices or conventions. All development activities, code reviews, and contributions must strictly adhere to the principles outlined herein. Amendments to this constitution require documentation and a version bump.

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04
