from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    name: str
    category: str
    duration_min: int
    priority: int
    recurrence: str
    completed: bool = False
    scheduled_time: str = ""
    due_date: date = field(default_factory=date.today)

    def mark_done(self):
        """Marks the task complete and creates the next recurring task."""
        self.completed = True

        if self.is_recurring():
            return self.create_next_task()

        return None

    def is_recurring(self):
        """Checks if the task repeats."""
        return self.recurrence.lower() in ["daily", "weekly"]

    def create_next_task(self):
        """Creates the next occurrence of a recurring task."""
        if self.recurrence.lower() == "daily":
            next_date = self.due_date + timedelta(days=1)

        elif self.recurrence.lower() == "weekly":
            next_date = self.due_date + timedelta(days=7)

        else:
            return None

        return Task(
            name=self.name,
            category=self.category,
            duration_min=self.duration_min,
            priority=self.priority,
            recurrence=self.recurrence,
            completed=False,
            scheduled_time=self.scheduled_time,
            due_date=next_date
        )

    def reset(self):
        """Resets recurring tasks for a new schedule."""
        if self.is_recurring():
            self.completed = False

    def __str__(self):
        """Returns a readable task description."""
        status = "Completed" if self.completed else "Pending"

        return (
            f"{self.name} - {self.category} | "
            f"{self.duration_min} min | "
            f"Priority: {self.priority} | "
            f"Due: {self.due_date} | {status}"
        )


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: float
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        """Adds a task to the pet."""
        self.tasks.append(task)

    def remove_task(self, task):
        """Removes a task from the pet."""
        if task in self.tasks:
            self.tasks.remove(task)

    def complete_task(self, task):
        """Completes a task and adds a recurring replacement if needed."""
        if task in self.tasks:
            new_task = task.mark_done()

            if new_task:
                self.tasks.append(new_task)

    def tasks_due_today(self):
        """Returns incomplete tasks."""
        return [
            task for task in self.tasks
            if not task.completed
        ]

    def get_tasks_by_category(self, category):
        """Returns tasks matching a category."""
        return [
            task for task in self.tasks
            if task.category.lower() == category.lower()
        ]

    def __str__(self):
        """Returns a readable pet description."""
        return (
            f"{self.name} ({self.species}) "
            f"- {len(self.tasks)} tasks"
        )


@dataclass
class Owner:
    name: str
    email: str
    minutes_available: int
    preferred_start_time: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        """Adds a pet to the owner."""
        self.pets.append(pet)

    def remove_pet(self, pet):
        """Removes a pet from the owner."""
        if pet in self.pets:
            self.pets.remove(pet)

    def list_pets(self):
        """Returns all pets."""
        return self.pets

    def get_all_tasks(self):
        """Collects tasks from all pets."""
        tasks = []

        for pet in self.pets:
            tasks.extend(pet.tasks)

        return tasks

    def __str__(self):
        """Returns owner information."""
        return f"{self.name} owns {len(self.pets)} pet(s)"


class Scheduler:
    def __init__(self, owner):
        """Creates a scheduler for an owner."""
        self.owner = owner

    def collect_tasks(self):
        """Gets all tasks from owner's pets."""
        return self.owner.get_all_tasks()

    def filter_incomplete_tasks(self):
        """Removes completed tasks from schedule."""
        return [
            task for task in self.collect_tasks()
            if not task.completed
        ]

    def filter_by_pet(self, pet_name):
        """Returns tasks for a specific pet."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                return pet.tasks

        return []

    def filter_by_status(self, completed=False):
        """Filters tasks by their completion status."""
        return [
            task for task in self.collect_tasks()
            if task.completed == completed
        ]

    def detect_schedule_conflicts(self):
        """Finds tasks scheduled at the same time and returns warnings."""
        time_slots = {}
        conflicts = []

        for task in self.collect_tasks():
            if task.scheduled_time:
                if task.scheduled_time not in time_slots:
                    time_slots[task.scheduled_time] = []

                time_slots[task.scheduled_time].append(task)

        for time, tasks in time_slots.items():
            if len(tasks) > 1:
                task_names = [task.name for task in tasks]

                conflicts.append(
                    f"Warning: Multiple tasks scheduled at {time}: "
                    + ", ".join(task_names)
                )

        return conflicts

    def sort_by_priority(self):
        """Sorts incomplete tasks by highest priority first."""
        tasks = self.filter_incomplete_tasks()

        return sorted(
            tasks,
            key=lambda task: task.priority,
            reverse=True
        )

    def sort_by_time(self):
        """Sorts tasks based on their scheduled time."""
        tasks = self.collect_tasks()

        return sorted(
            tasks,
            key=lambda task: task.scheduled_time or "99:99"
        )

    def detect_conflicts(self, tasks):
        """Checks if tasks exceed available time."""
        total_time = sum(
            task.duration_min for task in tasks
        )

        return total_time > self.owner.minutes_available

    def filter_by_time(self):
        """Selects tasks that fit within the owner's available time."""
        selected = []
        total_time = 0

        for task in self.sort_by_priority():
            if total_time + task.duration_min <= self.owner.minutes_available:
                selected.append(task)
                total_time += task.duration_min

        return selected

    def generate_plan(self):
        """Creates a daily schedule using priorities and time limits."""
        schedule = self.filter_by_time()

        if self.detect_conflicts(schedule):
            return []

        return schedule

    def explain_plan(self):
        """Explains how the schedule was created."""
        return (
            "The schedule prioritizes incomplete tasks, "
            "handles recurring tasks, and selects activities "
            "that fit within the owner's available time."
        )