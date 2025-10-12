"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    subjects = load_data(FILENAME)
    print(subjects)  # Print the raw nested list
    print_report(subjects)

def load_data(filename):
    """Read data from file and return a list of [subject, lecturer, number of students]."""
    subjects = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()  # Remove newline characters
            if line:  # Skip empty lines
                parts = line.split(",")  # Split into [subject, lecturer, students]
                # Convert student number to integer safely
                students = int(parts[2]) if parts[2].isdigit() else 0
                subjects.append([parts[0], parts[1], students])
    return subjects

def print_report(subjects):
    """Print each subject in a readable format."""
    for code, lecturer, students in subjects:
        print(f"{code} is taught by {lecturer} and has {students} students")

main()
