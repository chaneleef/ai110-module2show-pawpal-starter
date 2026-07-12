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

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
