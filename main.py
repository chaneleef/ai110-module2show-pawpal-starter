from pawpal_system import Task, Pet, Owner, Scheduler


# Create owner
owner = Owner(
    name="Alex",
    email="alex@example.com",
    minutes_available=60,
    preferred_start_time="8:00 AM"
)


# Create pets
dog = Pet("Buddy", "Dog", "Golden Retriever", 4)
cat = Pet("Luna", "Cat", "Siamese", 2)


# Create tasks out of order
task1 = Task(
    "Walk Buddy",
    "Exercise",
    30,
    4,
    "Daily",
    scheduled_time="09:00"
)

task2 = Task(
    "Feed Luna",
    "Feeding",
    10,
    5,
    "Daily",
    scheduled_time="08:00"
)

task3 = Task(
    "Groom Buddy",
    "Grooming",
    20,
    3,
    "Weekly",
    scheduled_time="10:00"
)

# New tasks with the same scheduled time to test conflicts
task4 = Task(
    "Give Buddy Medication",
    "Medication",
    10,
    5,
    "Daily",
    scheduled_time="08:00"
)

task5 = Task(
    "Play with Luna",
    "Exercise",
    20,
    3,
    "Daily",
    scheduled_time="08:00"
)


# Mark one task complete
task3.mark_done()


# Add tasks to pets
dog.add_task(task1)
dog.add_task(task3)
dog.add_task(task4)

cat.add_task(task2)
cat.add_task(task5)


# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)


# Create scheduler
scheduler = Scheduler(owner)


# Test sorting
print("Tasks Sorted By Time")
print("--------------------")

sorted_tasks = scheduler.sort_by_time()

for task in sorted_tasks:
    print(f"{task.scheduled_time} - {task.name}")


# Test filtering incomplete tasks
print("\nIncomplete Tasks")
print("----------------")

incomplete_tasks = scheduler.filter_by_status(False)

for task in incomplete_tasks:
    print(f"- {task.name}")


# Test filtering by pet
print("\nBuddy's Tasks")
print("-------------")

buddy_tasks = scheduler.filter_by_pet("Buddy")

for task in buddy_tasks:
    print(f"- {task.name}")


# Test conflict detection
print("\nSchedule Conflicts")
print("------------------")

conflicts = scheduler.detect_schedule_conflicts()

if conflicts:
    for warning in conflicts:
        print(warning)
else:
    print("No conflicts detected.")