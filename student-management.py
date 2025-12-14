# ======================================================================
# STUDENT ACADEMIC PERFORMANCE SYSTEM
# Full Project: Data Collection, Processing, Analysis & Menu Navigation
# ======================================================================


# --------------------------------------------------
# PART 1: DATA COLLECTION & STORAGE
# --------------------------------------------------

# Single student basic information (Task 1.1)
student_name = "Adebayo Kolade"
matric_number = "24/30CS101"
age = 21
cgpa = 4.45
is_active = True
courses_registered = ["Python", "Data Science"]
grades = {"Python": "A", "Data Science": "A"}

# Multiple students stored using list of dictionaries (Task 1.2)
students = [
    {
        "name": "Adebayo Kolade",
        "matric": "24/30CS101",
        "age": 21,
        "cgpa": 4.45,
        "is_active": True,
        "courses": ["Python", "Data Science"],
        "grades": {"Python": "A", "Data Science": "A"}
    },
    {
        "name": "Zainab Musa",
        "matric": "24/30CS102",
        "age": 19,
        "cgpa": 3.72,
        "is_active": True,
        "courses": ["Statistics", "Algorithms"],
        "grades": {"Statistics": "B", "Algorithms": "A"}
    },
    {
        "name": "Daniel Okorie",
        "matric": "24/30CS103",
        "age": 22,
        "cgpa": 2.95,
        "is_active": False,
        "courses": ["Python"],
        "grades": {"Python": "C"}
    },
    {
        "name": "Fatima Lawal",
        "matric": "24/30CS104",
        "age": 20,
        "cgpa": 4.10,
        "is_active": True,
        "courses": ["Algorithms", "Data Science"],
        "grades": {"Algorithms": "A", "Data Science": "B"}
    },
    {
        "name": "Ibrahim Sadiq",
        "matric": "24/30CS105",
        "age": 23,
        "cgpa": 3.30,
        "is_active": True,
        "courses": ["Statistics", "Python"],
        "grades": {"Statistics": "B", "Python": "B"}
    }
]

# Set containing all unique courses offered
unique_courses = {"Python", "Statistics", "Algorithms", "Data Science"}

# Tuple storing fixed department information
department_info = ("Computer Science Department", "Faculty of Computing", 2025)


# --------------------------------------------------
# PART 2: DATA PROCESSING & LOGIC
# --------------------------------------------------

# Function to compute grade from a given score
def compute_grade(score):
    # Validate score range
    if score < 0 or score > 100:
        print("Invalid score! Score must be between 0 and 100.")
        return None

    # Grade computation logic
    if 70 <= score <= 100:
        grade = "A"
    elif 60 <= score < 70:
        grade = "B"
    elif 50 <= score < 60:
        grade = "C"
    elif 45 <= score < 50:
        grade = "D"
    elif 40 <= score < 45:
        grade = "E"
    else:
        grade = "F"

    # Match-case used for feedback messages
    match grade:
        case "A":
            print("Feedback: Excellent performance!")
        case "B":
            print("Feedback: Very good performance.")
        case "C":
            print("Feedback: Good effort.")
        case "D":
            print("Feedback: Fair performance.")
        case "E":
            print("Feedback: Weak performance.")
        case "F":
            print("Feedback: Failed — Improvement needed!")

    return grade


# Function to validate user age and CGPA
def validate_user_input():
    try:
        age_input = int(input("Enter your age: "))
        cgpa_input = float(input("Enter your CGPA: "))

        # Age validation
        if 16 <= age_input <= 40:
            print("Valid age ✔")
        else:
            print("Invalid age ❌ (Must be 16–40)")

        # CGPA validation
        if 0.0 <= cgpa_input <= 5.0:
            print("Valid CGPA ✔")
        else:
            print("Invalid CGPA ❌ (Must be 0.0–5.0)")

    except ValueError:
        print("Error: Numeric values only!")


# --------------------------------------------------
# PART 3: ANALYSIS & REPORTING
# --------------------------------------------------

# Function demonstrating list slicing techniques
def analyze_scores():
    assignment_scores = [78, 92, 85, 60, 74, 88, 95, 67, 80, 90]

    # Extract top 3 highest scores
    top_3 = sorted(assignment_scores, reverse=True)[:3]

    # Extract last 5 scores
    last_5 = assignment_scores[-5:]

    # Extract every other score
    step_scores = assignment_scores[::2]

    print("Top 3 scores:", top_3)
    print("Last 5 scores:", last_5)
    print("Every other score:", step_scores)


# --------------------------------------------------
# MENU SYSTEM (INTEGRATING ALL PARTS)
# --------------------------------------------------

def menu():
    while True:
        print("\n=========== STUDENT ACADEMIC SYSTEM MENU ===========")
        print("1. Show department information")
        print("2. View all students")
        print("3. Validate user age and CGPA")
        print("4. Compute grade from score")
        print("5. Analyze assignment scores")
        print("6. Show unique courses")
        print("7. Exit")
        print("===================================================")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("Department Info:", department_info)

            case "2":
                print("\nList of students:")
                for stu in students:
                    status = "Active" if stu["is_active"] else "Inactive"
                    print(f'{stu["name"]} | Matric: {stu["matric"]} | CGPA: {stu["cgpa"]} | {status}')

            case "3":
                validate_user_input()

            case "4":
                try:
                    score = int(input("Enter score (0–100): "))
                    grade = compute_grade(score)
                    if grade:
                        print("Grade:", grade)
                except ValueError:
                    print("Invalid input! Enter a number.")

            case "5":
                analyze_scores()

            case "6":
                print("Unique courses offered:", unique_courses)

            case "7":
                print("Exiting system... Goodbye!")
                break

            case _:
                print("Invalid choice, try again.")


# --------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------

if __name__ == '__main__':
	menu()
