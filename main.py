# My AI Study Planner
# A beginner-friendly project using basic Python only.

print("===================================")
print("       MY AI STUDY PLANNER")
print("===================================")

student_name = input("Enter your name: ").strip()
while not student_name:
    student_name = input("Name cannot be empty. Enter your name: ").strip()

learning_goal = input("What is your AI learning goal? ").strip()
while not learning_goal:
    learning_goal = input("Goal cannot be empty. Enter your AI learning goal: ").strip()

while True:
    try:
        study_days = int(input("How many days per week will you study (1-7)? "))
        if 1 <= study_days <= 7:
            break
        print("Please enter a number from 1 to 7.")
    except ValueError:
        print("Please enter a whole number.")

while True:
    try:
        daily_hours = float(input("How many hours will you study each study day? "))
        if daily_hours > 0:
            break
        print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a number, such as 1 or 1.5.")

weekly_hours = study_days * daily_hours

study_plan = f"""
===================================
       MY AI STUDY PLAN
===================================
Student Name: {student_name}
AI Learning Goal: {learning_goal}
Study Days Per Week: {study_days}
Daily Study Hours: {daily_hours:g}
Total Weekly Study Hours: {weekly_hours:g}

PERSONALIZED WEEKLY PLAN
------------------------
Your goal: {learning_goal}

Study for {daily_hours:g} hour(s) on each of your {study_days} study day(s).

Suggested routine for each study day:
1. Spend the first 10 minutes reviewing what you learned previously.
2. Use the main part of your session to learn and practise your AI topic.
3. Spend the final 10 minutes writing notes or summarizing what you learned.
4. At the end of each week, review your progress and adjust your plan if needed.

Remember: Practise regularly, take breaks, and learn at a pace that works for you.
Good luck, {student_name}!
===================================
"""

print(study_plan)

try:
    with open("study_plan.txt", "w", encoding="utf-8") as file:
        file.write(study_plan)
    print("Your study plan has been saved to study_plan.txt")
except OSError:
    print("Sorry, the study plan could not be saved. Check folder permissions.")
