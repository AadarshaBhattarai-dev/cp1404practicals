"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    subjects = load_subjects(FILENAME)
    # Print the nested list
    print(subjects)
    # Then print the formatted report
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            # Ensure we have three parts before proceeding
            if len(parts) < 3:
                continue
            code = parts[0].strip()
            lecturer = parts[1].strip()
            # Convert student count to integer if possible
            try:
                students = int(parts[2].strip())
            except ValueError:
                students = 0
            subjects.append([code, lecturer, students])
    return subjects

def display_subjects(subjects):
    for code, lecturer, students in subjects:
        print(f"{code} is taught by {lecturer} and has {students} students")

main()