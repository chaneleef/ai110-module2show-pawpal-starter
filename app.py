import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")


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
PawPal+ is a pet care planning assistant that helps owners organize tasks
based on priority and available time.
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
    st.success(f"{pet_name} added!")


# Display pets
if st.session_state.owner.pets:
    st.subheader("Your Pets")

    for pet in st.session_state.owner.list_pets():
        st.write(pet)


st.divider()


# -------------------------
# Add Task Section
# -------------------------

st.subheader("📝 Add a Task")

task_title = st.text_input("Task title", value="Morning walk")

category = st.selectbox(
    "Category",
    ["Feeding", "Exercise", "Medication", "Grooming"]
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
    ["Daily", "Weekly", "Once"]
)


if st.button("Add Task"):
    if st.session_state.owner.pets:

        new_task = Task(
            task_title,
            category,
            int(duration),
            priority,
            recurrence
        )

        # Add task to the first pet
        st.session_state.owner.pets[0].add_task(new_task)

        st.success("Task added!")

    else:
        st.warning("Please add a pet before creating a task.")


# Display tasks
if st.session_state.owner.pets:

    st.subheader("Current Tasks")

    for pet in st.session_state.owner.pets:
        for task in pet.tasks:
            st.write(task)


st.divider()


# -------------------------
# Generate Schedule Section
# -------------------------

st.subheader("📅 Today's Schedule")


if st.button("Generate Schedule"):

    scheduler = Scheduler(st.session_state.owner)

    schedule = scheduler.generate_plan()

    if schedule:
        for task in schedule:
            st.write(
                f"✅ {task.name} | "
                f"{task.duration_min} minutes | "
                f"Priority: {task.priority}"
            )

    else:
        st.warning("No tasks fit within the available time.")

    st.info(scheduler.explain_plan())