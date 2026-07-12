import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pawpal_system import Task, Pet


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


if __name__ == "__main__":
    unittest.main()