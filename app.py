"""
Student Grade Management System
A comprehensive system for managing and analyzing student grades.
"""

# Constants
PASSING_GRADE = 55
MIN_GRADE = 0
MAX_GRADE = 100


def get_grade(subject):
    """
    Prompts the user to input a grade for the given subject.

    Args:
        subject (str): The name of the subject (e.g., 'English', 'Math')

    Returns:
        float: A valid grade between 0 and 100
    """
    while True:
        try:
            grade = float(input(f"Enter {subject} grade: ").strip())
            if grade < MIN_GRADE:
                print(
                    f"Invalid input. Grade cannot be negative. Please enter a number between {MIN_GRADE} and {MAX_GRADE}."
                )
                continue
            if grade > MAX_GRADE:
                print(
                    f"Invalid input. Grade cannot exceed {MAX_GRADE}. Please enter a number between {MIN_GRADE} and {MAX_GRADE}."
                )
                continue
            return grade
        except ValueError:
            print(
                f"Invalid input. Please enter a valid number between {MIN_GRADE} and {MAX_GRADE}."
            )


def get_student_info():
    """
    Prompts the user for a student's name and their English and Math grades.

    Returns:
        dict: A dictionary containing 'Name', 'English', and 'Math' keys
    """
    while True:
        name = input("Enter student's name: ").strip()
        if not name or name.isdigit():
            print(
                "Invalid input. Name cannot be empty or a digit. Please enter a valid name."
            )
            continue
        break

    english_grade = get_grade("English")
    math_grade = get_grade("Math")

    return {"Name": name, "English": english_grade, "Math": math_grade}


def print_student_info(students):
    """
    Prints individual student information including best grade and average.

    Args:
        students (list): List of student dictionaries containing grade information
    """
    print("\nStudent Information:")
    for student in students:
        name = student["Name"]
        english_grade = student["English"]
        math_grade = student["Math"]
        best_grade = max(english_grade, math_grade)
        avg = (english_grade + math_grade) / 2
        print(f"Student {name}, Best Grade: {best_grade:.2f}, Average Grade: {avg:.2f}")


def calculate_average_grades(students):
    """
    Calculates average grades per subject and overall average.

    Args:
        students (list): List of student dictionaries containing grade information

    Returns:
        tuple: (dict of average grades per subject, float overall average)
    """
    if not students:
        return {"English": 0, "Math": 0}, 0

    english_sum = sum(student["English"] for student in students)
    math_sum = sum(student["Math"] for student in students)
    count = len(students)

    english_avg = english_sum / count
    math_avg = math_sum / count
    overall_average_grade = (english_sum + math_sum) / (count * 2)

    average_grades_per_subject = {"English": english_avg, "Math": math_avg}

    return average_grades_per_subject, overall_average_grade


def calculate_failing_grades(students):
    """
    Calculates and displays failing grades per student and total failing grades.

    Args:
        students (list): List of student dictionaries containing grade information
    """
    print("\nFailing grades per student:")
    total_failing = 0

    for student in students:
        student_failing = 0

        if student["English"] <= PASSING_GRADE:
            student_failing += 1
            total_failing += 1

        if student["Math"] <= PASSING_GRADE:
            student_failing += 1
            total_failing += 1

        print(f"{student['Name']}: {student_failing} failing grade(s)")

    print(f"\nTotal failing grades across all students: {total_failing}")


def main():
    """
    Main entry point for the Student Grade Management System.
    Handles user input and orchestrates grade collection and analysis.
    """
    while True:
        try:
            number = int(input("Enter the number of students: ").strip())
            if number <= 0:
                print("Please enter a positive number greater than 0.")
                continue

            students = []
            for i in range(1, number + 1):
                print(f"\nEnter details for student {i}:")
                student_info = get_student_info()
                students.append(student_info)

            # Display individual student information
            print_student_info(students)

            # Calculate and display average grades
            average_grades_per_subject, overall_average_grade = (
                calculate_average_grades(students)
            )
            print("\nAverage grades per subject:")
            for subject, average_grade in average_grades_per_subject.items():
                print(f"{subject}: {average_grade:.2f}")

            print(
                f"\nOverall average grade across all subjects: {overall_average_grade:.2f}"
            )

            # Calculate and display failing grades
            calculate_failing_grades(students)

            # Exit the loop after successful execution
            break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
