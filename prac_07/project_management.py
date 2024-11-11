import datetime

from prac_07.project import Project


def main():
    projects = load_projects("projects.txt")
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")
    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter the filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter the filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            project = add_new_project()
            projects.append(project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save the changes to projects.txt? (yes/no): ").lower() == 'yes':
                save_projects("projects.txt", projects)
            print("Thank you for using Pythonic Project Management software.")
            break
        else:
            print("Invalid option, please try again.")

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                name, start_date, priority, estimate, completion = parts
                projects.append(Project(name, start_date, priority, estimate, completion))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.estimate}\t{project.completion}\n")

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(f" {project}")
    print("Completed projects:")
    for project in sorted(complete, key=lambda x: x.priority):
        print(f" {project}")

def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(f" {project}")

def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    estimate = input("Cost estimate: ")
    completion = input("Percent complete: ")
    return Project(name, start_date, priority, estimate, completion)


def update_project(projects):
    if not projects:
        print("No projects available to update.")
        return

    for i, project in enumerate(projects):
        print(f"{i} {project}")

    while True:
        try:
            project_index = int(input("Project choice: "))
            if project_index < 0 or project_index >= len(projects):
                print(f"Please enter a valid project number between 0 and {len(projects) - 1}.")
            else:
                break
        except ValueError:
            print("Invalid input; please enter a number.")

    selected_project = projects[project_index]
    new_completion = input("New completion (%): ").strip()
    if new_completion:
        try:
            new_completion = int(new_completion)
            if new_completion < 0 or new_completion > 100:
                print("Completion percentage must be between 0 and 100.")
            else:
                selected_project.completion = new_completion
        except ValueError:
            print("Invalid completion value; please enter a valid percentage.")

    new_priority = input("New priority: ").strip()
    if new_priority:
        try:
            new_priority = int(new_priority)
            if new_priority < 0:
                print("Priority must be a positive number.")
            else:
                selected_project.priority = new_priority
        except ValueError:
            print("Invalid priority; please enter a number.")


if __name__ == "__main__":
    main()
