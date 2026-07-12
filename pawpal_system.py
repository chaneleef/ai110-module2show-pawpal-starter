from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    category: str
    duration_min: int
    priority: int
    recurrence: str
    completed: bool = False
    scheduled_time: str = ""

    def mark_done(self):
        """Marks the task as completed."""
        self.completed = True

    def is_recurring(self):
        """Checks if the task repeats."""
        return self.recurrence.lower() != "once"

    def reset(self):
        """Resets recurring tasks for the next schedule."""
        if self.is_recurring():
            self.completed = False

    def __str__(self):
        """Returns a readable task description."""
        status = "✓" if self.completed else "✗"
        time = self.scheduled_time if self.scheduled_time else "Not Scheduled"
        return (
            f"{status} {self.name} "
            f"({self.category}) - {self.duration_min} min "
            f"at {time}"
        )


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: float
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        """Adds a task to the pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task):
        """Removes a task from the pet's task list."""
        if task in self.tasks:
            self.tasks.remove(task)

    def tasks_due_today(self):
        """Returns incomplete tasks for the pet."""
        return [task for task in self.tasks if not task.completed]

    def get_tasks_by_category(self, category):
        """Filters tasks by category."""
        return [
            task for task in self.tasks
            if task.category.lower() == category.lower()
        ]

    def __str__(self):
        """Returns a readable pet description."""
        return (
            f"{self.name} ({self.species}, {self.breed}) "
            f"- {len(self.tasks)} task(s)"
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
        """Returns the owner's pets."""
        return self.pets

    def get_all_tasks(self):
        """Collects tasks from all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks

    def __str__(self):
        """Returns a readable owner description."""
        return f"{self.name} - {len(self.pets)} pet(s)"


class Scheduler:
    def __init__(self, owner):
        """Creates a scheduler for an owner."""
        self.owner = owner

    def collect_tasks(self):
        """Gets all tasks from the owner's pets."""
        return self.owner.get_all_tasks()

    def sort_by_priority(self):
        """Sorts tasks from highest to lowest priority."""
        tasks = self.collect_tasks()
        return sorted(tasks, key=lambda task: task.priority, reverse=True)

    def filter_by_time(self):
        """Selects tasks that fit the owner's available time."""
        tasks = self.sort_by_priority()

        available = self.owner.minutes_available
        selected = []
        total_time = 0

        for task in tasks:
            if total_time + task.duration_min <= available:
                selected.append(task)
                total_time += task.duration_min

        return selected

    def generate_plan(self):
        """Creates the daily task schedule."""
        return self.filter_by_time()

    def explain_plan(self):
        """Explains how the schedule was generated."""
        return (
            "Tasks were sorted by priority and selected until "
            "the available time was filled."
        )