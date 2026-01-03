---
id: 001
title: Establish Initial Project Constitution v1.0.0
stage: constitution
date: 2026-01-04
surface: agent
model: gemini-cli
feature: null
branch: null
user: unknown
command: /sp.constitution
labels: [constitution, project-setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

/sp.constitution

You are an expert AI assistant following strict Spec-Driven Development using SpecifyPlus on a simple in-memory Python console Todo app for Hackathon Phase I.

First, carefully read and follow all instructions in GEMINI.md.

Project Name: Hackathon II - Evolution of Todo (Phase I: In-Memory Console App)

Generate a clear, concise, and complete constitution.md file that defines the non-negotiable principles, constraints, and standards for this project.

The constitution MUST include the following sections:

1. Project Overview
   - Simple command-line Todo app
   - Storage: in-memory only (no files, no database)
   - Phase I scope: only 5 basic CRUD operations + menu

2. Core Principles
   - Extreme simplicity and readability over cleverness
   - No external dependencies (only built-in Python)
   - Strict spec-driven development — no code without spec
   - Clean, well-documented, beginner-friendly code

3. Code Quality Standards
   - Short functions (max 15 lines when possible)
   - Meaningful variable and function names
   - Type hints required
   - Docstrings for all classes and public functions
   - Basic error handling (invalid input, task not found)

4. Architecture Guidelines
   - Recommended structure:
     - models.py → Task class (dataclass allowed)
     - todo.py   → TodoManager class with operations
     - main.py   → Menu loop and user interaction only
   - Apply SOLID principles simply (especially SRP)
   - Avoid global variables when reasonably possible

5. User Experience
   - Clear, numbered console menu
   - Friendly confirmation and error messages
   - Task listing with ID, title, status, and description

6. Constraints
   - No external libraries
   - No persistence (data lost on exit)
   - No advanced features beyond the 5 basic ones in Phase I

7. Development Process
   - Must follow SpecifyPlus flow: specify → plan → tasks → implement
   - Every change must trace back to a spec
   - Create Prompt History Record (PHR) after each completed session

Output only the complete content of constitution.md in proper Markdown format.
Do not add any explanation outside the file content.

After outputting the file, suggest creating a PHR in:
history/prompts/constitution/

## Response snapshot

Generated the initial project constitution `v1.0.0` based on the user's detailed requirements. The constitution defines core principles, standards, and processes for the "Hackathon II - Evolution of Todo" project.

## Outcome

- ✅ Impact: Established the foundational governance document for the project, ensuring all future development aligns with clear, explicit standards.
- 🧪 Tests: none
- 📁 Files: - .specify/memory/constitution.md
- 🔁 Next prompts: The next logical step is to specify the first feature using `/sp.specify`.
- 🧠 Reflection: The user provided a very specific and structured prompt, which made generating the constitution straightforward. This highlights the value of clear user input. The initial `sp.constitution` command definition was slightly ambiguous regarding agent-specific files, but I correctly chose not to modify files belonging to another agent (`.claude/`).
