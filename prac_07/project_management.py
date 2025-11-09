"""CP1404 Practical 07"""

from project import Project
from datetime import datetime
import os

DEFAULT_FILE = "projects.txt"

def main():
    filename = DEFAULT_FILE
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    running = True
    menu = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit\n")

    while running:
        print(menu)
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            fname = input("Filename to load: ").strip()
            if fname:
                projects = load_projects(fname)
            else:
                print("No filename entered.")
        elif choice == 's':
            fname = input("Filename to save to (leave blank for default): ").strip()
            if fname:
                save_projects(projects, fname)
            else:
                save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            ans = input(f"Would you like to save to {filename}? ").strip().lower()
            if ans in ('y', 'yes'):
                save_projects(projects, filename)
            else:
                print("Not saved.")
            print("Thank you for using custom-built project management software.")
            running = False
        else:
            print("Invalid option.")

def load_projects(filename=DEFAULT_FILE):
    projects = []
    if not os.path.exists(filename):
        print(f"File not found: {filename}. Starting with empty project list.")
        return projects
    try:
        with open(filename, encoding='utf-8') as in_file:
            header = in_file.readline()  # consume header
            for line in in_file:
                line = line.strip()
                if not line:
                    continue
                try:
                    project = Project.from_file_line(line)
                    projects.append(project)
                except Exception as e:
                    print(f"Skipping bad line: {line} -> {e}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return projects


def save_projects(projects, filename=DEFAULT_FILE):
    with open(filename, "w", encoding='utf-8') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            out_file.write(p.to_file_line() + "\n")
    print(f"Saved {len(projects)} projects to {filename}.")


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    incomplete_sorted = sorted(incomplete, key=lambda x: x.priority)
    complete_sorted = sorted(complete, key=lambda x: x.priority)

    if incomplete_sorted:
        print("Incomplete projects:")
        for p in incomplete_sorted:
            print(f"  {p}")
    else:
        print("No incomplete projects.")

    if complete_sorted:
        print("Completed projects:")
        for p in complete_sorted:
            print(f"  {p}")
    else:
        print("No completed projects.")


def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        target_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return
    filtered = [p for p in projects if p.start_date >= target_date]
    filtered.sort(key=lambda x: x.start_date)
    for p in filtered:
        print(p)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ").strip()
    if not name:
        print("Project must have a name.")
        return
    date_str = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Project not added.")
        return
    priority_str = input("Priority: ").strip()
    cost_str = input("Cost estimate: ").strip()
    completion_str = input("Percent complete: ").strip()
    try:
        priority = int(priority_str)
        cost = float(cost_str)
        completion = int(completion_str)
    except ValueError:
        print("Invalid numeric input. Project not added.")
        return
    projects.append(Project(name, start_date, priority, cost, completion))
    print("Project added.")


def update_project(projects):
    if not projects:
        print("No projects to update.")
        return
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    choice_str = input("Project choice: ").strip()
    try:
        idx = int(choice_str)
        if idx < 0 or idx >= len(projects):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return
    project = projects[idx]
    print(project)
    new_completion = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()
    if new_completion:
        try:
            project.completion = int(new_completion)
        except ValueError:
            print("Invalid completion percent. Not changed.")
    if new_priority:
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid priority. Not changed.")
    print("Project updated.")

main()