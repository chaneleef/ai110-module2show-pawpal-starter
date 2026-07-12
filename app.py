import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)


# Keep Owner object between Streamlit refreshes
if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        "Jordan",
        "jordan@email.com",
        60,
        "8:00 AM"
    )


st.title("🐾 PawPal+")

st.markdown(
    """
PawPal+ is a pet care planning assistant that helps owners organize
pet tasks based on priority, available time, and scheduling conflicts.
"""
)


st.divider()


# -------------------------
# Add Pet Section
# -------------------------

st.subheader("🐶 Add a Pet")

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
breed = st.text_input("Breed", value="Golden Retriever")
age = st.number_input("Age", min_value=0.0, value=2.0)


if st.button("Add Pet"):

    new_pet = Pet(
        pet_name,
        species,
        breed,
        age
    )

    st.session_state.owner.add_pet(new_pet)

    st.success(f"{pet_name} added successfully!")


# Display pets
if st.session_state.owner.pets:

    st.subheader("🐾 Your Pets")

    pet_data = []

    for pet in st.session_state.owner.list_pets():
        pet_data.append(
            {
                "Name": pet.name,
                "Species": pet.species,
                "Breed": pet.breed,
                "Age": pet.age,
                "Tasks": len(pet.tasks)
            }
        )

    st.table(pet_data)



st.divider()


# -------------------------
# Add Task Section
# -------------------------

st.subheader("📝 Add a Task")


task_title = st.text_input(
    "Task title",
    value="Morning walk"
)


category = st.selectbox(
    "Category",
    [
        "Feeding",
        "Exercise",
        "Medication",
        "Grooming"
    ]
)


duration = st.number_input(
    "Duration (minutes)",
    min_value=1,
    max_value=240,
    value=20
)


priority = st.slider(
    "Priority",
    min_value=1,
    max_value=5,
    value=3
)


recurrence = st.selectbox(
    "Recurrence",
    [
        "Daily",
        "Weekly",
        "Once"
    ]
)


scheduled_time = st.text_input(
    "Scheduled Time (HH:MM)",
    value="08:00"
)



if st.button("Add Task"):

    if st.session_state.owner.pets:

        new_task = Task(
            task_title,
            category,
            int(duration),
            priority,
            recurrence,
            scheduled_time=scheduled_time
        )


        # Add task to first pet
        st.session_state.owner.pets[0].add_task(new_task)

        st.success("Task added successfully!")

    else:
        st.warning(
            "Please add a pet before creating a task."
        )



# -------------------------
# Display Tasks
# -------------------------

if st.session_state.owner.pets:

    st.subheader("📋 Current Tasks")

    scheduler = Scheduler(
        st.session_state.owner
    )

    tasks = scheduler.sort_by_time()


    if tasks:

        task_data = []

        for task in tasks:

            task_data.append(
                {
                    "Task": task.name,
                    "Category": task.category,
                    "Time": task.scheduled_time,
                    "Duration": f"{task.duration_min} min",
                    "Priority": task.priority,
                    "Status": (
                        "Completed"
                        if task.completed
                        else "Pending"
                    )
                }
            )


        st.table(task_data)

    else:
        st.info("No tasks added yet.")



st.divider()


# -------------------------
# Generate Schedule Section
# -------------------------

st.subheader("📅 Today's Schedule")


if st.button("Generate Schedule"):

    scheduler = Scheduler(
        st.session_state.owner
    )


    # Check conflicts first
    conflicts = scheduler.detect_schedule_conflicts()


    if conflicts:

        st.warning(
            "⚠️ Scheduling conflicts found. "
            "Please review these tasks:"
        )


        for conflict in conflicts:
            st.warning(conflict)



    schedule = scheduler.generate_plan()


    if schedule:

        st.success(
            "Schedule created successfully!"
        )


        schedule_data = []


        for task in schedule:

            schedule_data.append(
                {
                    "Task": task.name,
                    "Duration": f"{task.duration_min} min",
                    "Priority": task.priority,
                    "Time": task.scheduled_time
                }
            )


        st.table(schedule_data)


    else:

        st.warning(
            "No tasks fit within the available time."
        )


    st.info(
        scheduler.explain_plan()
    )