# GEMINI.md – Todo Console App (Hackathon Phase I)

This file defines project-specific instructions for **Gemini Code / Gemini CLI** while working on the Todo Console App during Hackathon Phase I.

You are building a **very simple, in-memory, command-line Todo application in Python**.  
This project follows **strict spec-driven development** using **SpecifyPlus** and prioritizes clarity, simplicity, and traceability over complexity.

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

## SpecifyPlus Workflow (MANDATORY)

This project uses **SpecifyPlus** for disciplined, traceable development.  
Follow this exact flow for every change:

1. `/sp.specify` → Create or update feature specification in `specs/features/`
2. `/sp.plan` → Generate implementation plan from the spec
3. `/sp.tasks` → Break plan into small, testable tasks
4. Only after tasks are defined → implement code

**Rules:**

- Never write code before completing `/sp.specify` and `/sp.plan`.
- Always reference the spec file (e.g., `@specs/features/add-task.md`).
- Treat specs as the single source of truth — not code or memory.

---

## Prompt History Record (PHR) — Must Create After Every Session

After completing any request (implementation, planning, debugging, etc.), you **MUST** create a Prompt History Record (PHR) to keep full traceability.

**Process:**

1. Determine stage: `spec` | `plan` | `tasks` | `implementation` | `general`
2. Create a short title (3–7 words)
3. Save the PHR in the correct folder:
   - Constitution → `history/prompts/constitution/`
   - Feature → `history/prompts/<feature-name>/`
   - General → `history/prompts/general/`
4. File name format: `<ID>-<slug>.<stage>.prompt.md`
5. Include:
   - Full user prompt (verbatim)
   - Key response/output
   - Files created/modified
   - Date and stage

If a template exists (`.specify/templates/phr-template.prompt.md`), use it.  
Final step: Confirm the path and say:  
**“PHR created at: history/prompts/…”**

---

## Architectural Decision Records (ADR) — Suggest When Needed

When you detect a significant architectural choice (e.g., data structure, separation of concerns, extensibility), **suggest** creating an ADR but never auto-create one.

Say:

> 📋 Architectural decision detected: *<short description>*  
> Document reasoning and trade-offs? Run `/sp.adr <title>`

Wait for user confirmation.

---

## SOLID Principles (Apply Simply)

Apply SOLID in the simplest, most practical way:

1. **Single Responsibility** → One job per class/function  
2. **Open/Closed** → Extend via new functions, avoid modifying stable code  
3. **Liskov Substitution** → Subtypes must behave exactly like parent  
4. **Interface Segregation** → Keep interfaces minimal and focused  
5. **Dependency Inversion** → Pass dependencies instead of using globals when reasonable

---

## Recommended Project Structure

- `models.py` → Simple `Task` class (id, title, description, completed)
- `todo.py` → `TodoManager` class (add, list, update, delete, toggle)
- `main.py` → Menu loop and user interaction only
- `specs/features/` → All feature specifications
- `history/prompts/` → PHR and ADR records

---

## Implementation Guidelines

- Use type hints and short docstrings
- Clean console menu:
  1. Add task  
  2. List tasks  
  3. Update task  
  4. Delete task  
  5. Mark complete/incomplete  
  6. Exit
- Basic error handling (invalid ID, empty input, etc.)
- Friendly confirmation messages

---

## When Implementing a Feature

Example:  
`Implement add-task using @specs/features/add-task.md`

Flow:

1. Read `constitution.md` and the spec
2. Confirm understanding of requirements
3. Plan minimal changes
4. Generate only required code
5. State which files to update/create
6. Apply SOLID simply
7. End with PHR creation

---

## Safety & Project Philosophy

- Never add unsolicited features
- Make only small, atomic changes
- Prioritize: Correctness > Simplicity > Readability > Spec compliance
- This is a learning/demo project — avoid over-engineering

Good luck with the hackathon! 🚀
