"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    subjects = load_subjects(FILENAME)
    print(subjects)  # Print the raw nested list
    print_report(subjects)

def load_subjects(filename):
    """Read data from a file and return a list of [subject, lecturer, students]."""
    subjects = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                try:
                    students = int(parts[2])
                except ValueError:
                    students = 0
                subjects.append([parts[0], parts[1], students])
    return subjects

def print_report(subjects):
    for subject in subjects:
        code = subject[0]
        lecturer = subject[1]
        students = subject[2]
        print(f"{code} is taught by {lecturer} and has {students} students")

main()
