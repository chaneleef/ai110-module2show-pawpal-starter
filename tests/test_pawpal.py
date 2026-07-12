import unittest
import sys
import os
from datetime import date, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pawpal_system import Task, Pet, Owner, Scheduler


class TestPawPal(unittest.TestCase):

    def test_task_completion(self):
        task = Task("Feed Buddy", "Feeding", 15, 5, "Daily")

        self.assertFalse(task.completed)

        task.mark_done()

        self.assertTrue(task.completed)


    def test_task_addition(self):
        pet = Pet("Buddy", "Dog", "Golden Retriever", 4)
        task = Task("Walk Buddy", "Exercise", 30, 4, "Daily")

        self.assertEqual(len(pet.tasks), 0)

        pet.add_task(task)

        self.assertEqual(len(pet.tasks), 1)


    def test_sorting_correctness(self):
        owner = Owner(
            "Alex",
            "alex@email.com",
            60,
            "8:00 AM"
        )

        pet = Pet("Buddy", "Dog", "Golden Retriever", 4)

        task1 = Task(
            "Walk",
            "Exercise",
            30,
            4,
            "Daily",
            scheduled_time="09:00"
        )

        task2 = Task(
            "Feed",
            "Feeding",
            15,
            5,
            "Daily",
            scheduled_time="08:00"
        )

        pet.add_task(task1)
        pet.add_task(task2)
        owner.add_pet(pet)

        scheduler = Scheduler(owner)

        sorted_tasks = scheduler.sort_by_time()

        self.assertEqual(sorted_tasks[0].name, "Feed")
        self.assertEqual(sorted_tasks[1].name, "Walk")


    def test_daily_task_creates_next_task(self):
        task = Task(
            "Feed Buddy",
            "Feeding",
            15,
            5,
            "Daily"
        )

        next_task = task.mark_done()

        self.assertTrue(task.completed)
        self.assertIsNotNone(next_task)

        self.assertEqual(
            next_task.due_date,
            task.due_date + timedelta(days=1)
        )

        self.assertFalse(next_task.completed)


    def test_conflict_detection(self):
        owner = Owner(
            "Alex",
            "alex@email.com",
            60,
            "8:00 AM"
        )

        pet = Pet("Buddy", "Dog", "Golden Retriever", 4)

        task1 = Task(
            "Feed Buddy",
            "Feeding",
            15,
            5,
            "Daily",
            scheduled_time="08:00"
        )

        task2 = Task(
            "Give Medication",
            "Medication",
            10,
            5,
            "Daily",
            scheduled_time="08:00"
        )

        pet.add_task(task1)
        pet.add_task(task2)

        owner.add_pet(pet)

        scheduler = Scheduler(owner)

        conflicts = scheduler.detect_schedule_conflicts()

        self.assertEqual(len(conflicts), 1)
        self.assertIn("08:00", conflicts[0])


if __name__ == "__main__":
    unittest.main()