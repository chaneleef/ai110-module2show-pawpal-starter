from pawpal_system import Task, Pet, Owner, Scheduler


# Create an owner
owner = Owner(
    name="Alex",
    email="alex@example.com",
    minutes_available=60,
    preferred_start_time="8:00 AM"
)

# Create pets
dog = Pet("Buddy", "Dog", "Golden Retriever", 4)
cat = Pet("Luna", "Cat", "Siamese", 2)

# Create tasks
task1 = Task("Feed Buddy", "Feeding", 15, 5, "Daily")
task2 = Task("Walk Buddy", "Exercise", 30, 4, "Daily")
task3 = Task("Feed Luna", "Feeding", 10, 5, "Daily")

# Add tasks to pets
dog.add_task(task1)
dog.add_task(task2)
cat.add_task(task3)

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler(owner)

# Generate today's schedule
schedule = scheduler.generate_plan()

# Print today's schedule
print("Today's Schedule")
print("-" * 20)
print(f"Owner: {owner.name}")
print(f"Available Time: {owner.minutes_available} minutes\n")

for task in schedule:
    print(
        f"- {task.name} ({task.category}) "
        f"- {task.duration_min} min | Priority: {task.priority}"
    )

print("\n" + scheduler.explain_plan())