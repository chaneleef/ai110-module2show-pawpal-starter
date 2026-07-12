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
        pass

    def is_recurring(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: float
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def tasks_due_today(self):
        pass