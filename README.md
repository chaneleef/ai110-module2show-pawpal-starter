# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

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
collected 5 items

tests\test_pawpal.py ..... [100%]

==================== 5 passed in 0.08s ====================

```
# Paste your pytest output here
```

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

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or link to a demo video here -->
