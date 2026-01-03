# CLAUDE.md – Todo Console App (Hackathon Phase I)

This file defines project-specific instructions for **Claude Code** while working on the Todo Console App during Hackathon Phase I.

You are building a **very simple, in-memory, command-line Todo application in Python**.  
This project follows **strict spec-driven development** and prioritizes clarity over complexity.

---

## Core Rules (STRICT)

- **Always read `constitution.md` and the relevant spec file first** before writing or modifying any code.
- Never generate or change code without a **clear reference to a spec**.
- Keep all code **extremely simple, short, and easy to understand**.
- Use **only built-in Python features** — no external libraries.
- Store tasks **in memory only** (use a simple list).
- Functions and methods must be short (ideally **5–15 lines maximum**).
- Prefer explicit, readable logic over clever or compact solutions.

---

## SOLID Principles (Apply Simply)

Apply the five SOLID principles in the **simplest and most practical way possible**:

### 1. Single Responsibility Principle (SRP)
Each class or function should have **one clear job only**.

Example:
- One class for task data
- One class for managing tasks
- One file for user input/output

---

### 2. Open/Closed Principle (OCP)
Existing code should be **open for extension but closed for modification**.

- Add new behavior by creating **new small functions**
- Avoid changing working code unless the spec explicitly requires it

---

### 3. Liskov Substitution Principle (LSP)
If subclasses are introduced, they must fully work in place of their parent class without breaking behavior.

---

### 4. Interface Segregation Principle (ISP)
Keep classes and functions **small and focused**.

- Do not force any class or function to implement behavior it does not need.

---

### 5. Dependency Inversion Principle (DIP)
High-level logic (such as the menu loop) should depend on abstractions, not concrete implementations.

- Prefer passing dependencies (e.g., task manager) into functions
- Avoid global variables when reasonably possible

---

## Recommended Project Structure

- `models.py`  
  → Contains a simple `Task` class (data + basic display only)

- `todo.py`  
  → Contains `TodoManager` class for:
  - add
  - list
  - update
  - delete
  - toggle complete/incomplete

- `main.py`  
  → Handles menu loop and all user interaction only

---

## Implementation Guidelines

- Use type hints where they improve clarity.
- Add short, clear docstrings to all classes and public functions.
- Include basic error handling:
  - invalid input
  - task not found
- Display a clean console menu with these options:

  1. Add task  
  2. List tasks  
  3. Update task  
  4. Delete task  
  5. Mark complete / incomplete  
  6. Exit  

---

## When Implementing a Feature

When asked to implement something like:

> `Implement add-task using @specs/features/add-task.md`

Follow this exact flow:

1. Read the referenced spec and `constitution.md`
2. Plan the changes step by step
3. Generate **only the minimum required code**
4. Apply SOLID principles **naturally and simply**
5. Clearly state which file(s) should be updated or created

---

## Safety & Constraints

- **Never** suggest or generate destructive operations (file deletion, system commands, etc.).
- Make only **focused, atomic changes**.
- Do **not** add features beyond what the spec explicitly requests.

---

## Project Philosophy

This is a **learning and demonstration project**, not a production system.

The top priorities are:
- Correctness
- Simplicity
- Readability
- Spec compliance

Avoid over-engineering at all costs.

Good luck with the hackathon 🚀
