# PawPal+ Project Reflection

## 1. System Design

- add pet, add pet tasks, gather info like owners preferences and times

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Main objects:
Pet-> all tasks associated with pet
Human -> time constraints preferences daily plan actions
My initial UML design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages the user's pets and available time, Pet stores information about each pet and its care tasks, Task represents individual care activities like feeding or walking, and Scheduler organizes tasks into a daily plan based on priority and time constraints. I assigned each class a single responsibility to keep the design organized and easy to maintain.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
  Yes, my design changed a little during implementation. Instead of having the Scheduler keep its own separate list of tasks, I made it work directly with the Owner and collect tasks from each pet. This avoids storing the same data twice and keeps everything connected, making the code simpler and easier to maintain.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers the owner's available time, task priority, and task completion status. I prioritized time and priority because important pet care tasks should be completed first while still fitting into the owner's schedule.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
  One tradeoff is that the scheduler only detects conflicts when tasks have the same exact scheduled time instead of checking overlapping task durations. This keeps the logic simple and easier to use, but a more advanced system would need to consider how long each task takes.

---

## 3. AI Collaboration

### a. How you used AI

I used AI as a coding assistant throughout the project for brainstorming my class design, debugging errors, improving my code structure, and writing tests. The most helpful prompts were asking AI to explain errors, suggest methods for my classes, and review whether my UML diagram matched my final implementation.

### b. Judgment and verification

I did not accept every AI suggestion automatically. For example, when adding conflict detection, AI suggested comparing every task with nested loops. I changed it to use a dictionary grouped by scheduled time because it was cleaner and more efficient.

Using separate chat sessions for each phase helped me stay organized because I could focus on one goal at a time, such as UML design, implementation, testing, and documentation.

The AI features that helped the most were debugging explanations, code suggestions, and reviewing my design decisions. I learned that I needed to act as the lead architect by making the final decisions, checking AI output, and making sure the code matched my project goals.

---

## 4. Testing and Verification

### a. What you tested

I tested task completion, adding tasks to pets, sorting tasks by time, recurring task creation, and conflict detection. These tests were important because they verified that the scheduler worked correctly for both normal scenarios and edge cases.

### b. Confidence

I am confident that my scheduler works for the features I implemented. If I had more time, I would test more complex cases like overlapping task durations, multiple pets with large numbers of tasks, and different scheduling constraints.

---

## 5. Reflection

### a. What went well

I am most satisfied with how my scheduler evolved from a simple task organizer into a system that can sort tasks, detect conflicts, and handle recurring care routines.

### b. What I would improve

I would improve the scheduling algorithm by adding smarter time management, such as detecting overlapping task durations instead of only checking exact time matches.

### c. Key takeaway

I learned that working with AI requires clear direction and decision-making. AI can help build faster, but I still need to understand the code, test solutions, and make design choices that fit the system.
