# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## ✨ Features

PawPal+ includes smart scheduling features that help pet owners organize and manage daily care tasks.

- **Task Sorting**
  - Uses `Scheduler.sort_by_time()` to organize tasks chronologically.
  - Uses `Scheduler.sort_by_priority()` to prioritize important tasks first.

- **Task Filtering**
  - Uses `Scheduler.filter_by_status()` to view completed or incomplete tasks.
  - Uses `Scheduler.filter_by_pet()` to display tasks for a specific pet.
  - Uses `Scheduler.filter_incomplete_tasks()` to remove completed tasks from schedules.

- **Smart Schedule Generation**
  - Uses `Scheduler.generate_plan()` to create a schedule based on task priority and the owner's available time.
  - Prevents tasks from exceeding the owner's time limit.

- **Conflict Warnings**
  - Uses `Scheduler.detect_schedule_conflicts()` to identify tasks scheduled at the same time.
  - Displays warnings instead of causing the program to fail.

- **Recurring Tasks**
  - Supports daily and weekly recurring tasks.
  - Uses `Task.mark_done()` and `Task.create_next_task()` to automatically create the next occurrence after completion.

- **Pet and Task Management**
  - Owners can manage multiple pets.
  - Pets can store, add, remove, and complete their own tasks.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## Today's Schedule

Owner: Alex
Available Time: 60 minutes

- Feed Buddy (Feeding) - 15 min | Priority: 5
- Feed Luna (Feeding) - 10 min | Priority: 5
- Walk Buddy (Exercise) - 30 min | Priority: 4

Tasks were sorted by priority and selected until the available time was filled.

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest
python -m pytest

# Run with coverage:
pytest --cov
```

The tests verify the core functionality of PawPal+, including task completion, adding tasks to pets, sorting tasks by scheduled time, recurring task creation, and detecting scheduling conflicts. These tests help ensure the scheduler works correctly for both normal use cases and edge cases.

Sample test output:

```
collected 5 items

tests\test_pawpal.py ..... [100%]

==================== 5 passed in 0.08s ====================
```

Confidence Level: 5 Stars

## 📐 Smarter Scheduling

PawPal+ includes scheduling features that help organize pet care tasks based on priority, time, and task status.

| Feature           | Method(s)                                                                                          | Notes                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Task sorting      | `Scheduler.sort_by_time()`, `Scheduler.sort_by_priority()`                                         | Sorts tasks by scheduled time and prioritizes higher priority tasks first.                             |
| Filtering         | `Scheduler.filter_by_pet()`, `Scheduler.filter_by_status()`, `Scheduler.filter_incomplete_tasks()` | Allows users to view tasks for a specific pet or filter tasks based on completion status.              |
| Conflict handling | `Scheduler.detect_schedule_conflicts()`                                                            | Checks for multiple tasks scheduled at the same time and returns warning messages instead of crashing. |
| Recurring tasks   | `Task.mark_done()`, `Task.create_next_task()`, `Pet.complete_task()`                               | Automatically creates the next occurrence of daily or weekly tasks after completion.                   |

### Scheduling Logic

The scheduler first collects tasks from all pets, removes completed tasks when needed, and organizes tasks based on priority or scheduled time. It also checks for conflicts between tasks that have the same scheduled time. For recurring tasks, completing a daily or weekly task automatically creates a new task for the next occurrence using date calculations.

## 📸 Demo Walkthrough

Follow these steps to use PawPal+:

1. **Add a pet**
   - The user enters pet information such as name, species, breed, and age.
   - The pet is added to the owner's profile and displayed in the app.

2. **Create pet care tasks**
   - The user creates tasks by entering details like task name, category, duration, priority, recurrence, and scheduled time.
   - Tasks are connected to the selected pet.

3. **Generate a daily schedule**
   - The user selects the "Generate Schedule" button.
   - The Scheduler collects tasks, filters incomplete tasks, sorts them by priority, and creates a schedule that fits the owner's available time.

4. **Review schedule results**
   - The user can view organized tasks in the schedule.
   - Tasks are displayed with important information including duration, priority, and scheduled time.

5. **View smart scheduling features**
   - PawPal+ detects scheduling conflicts when multiple tasks have the same scheduled time.
   - Recurring tasks automatically create the next occurrence after completion.
   - Users can filter tasks by pet or completion status.

### Example Workflow

A user opens PawPal+, adds their dog Buddy, creates a daily feeding task and a walk task, then generates a schedule. The Scheduler prioritizes important tasks, checks available time, and displays the recommended plan.

### Sample CLI Output

```text
Today's Schedule
--------------------
Owner: Alex
Available Time: 60 minutes

08:00 - Feed Luna | Feeding | 10 min | Priority: 5
09:00 - Walk Buddy | Exercise | 30 min | Priority: 4
10:00 - Groom Buddy | Grooming | 20 min | Priority: 3

The schedule prioritizes incomplete tasks, handles recurring tasks,
and selects activities that fit within the owner's available time.

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or link to a demo video here -->
```
