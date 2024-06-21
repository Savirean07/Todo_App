import os

# File to store to-do items
TODO_FILE = 'todo.txt'

def load_todos():
    """Load to-do items from the file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_todos(todos):
    """Save to-do items to the file."""
    with open(TODO_FILE, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

def show_todos(todos):
    """Display the list of to-do items."""
    if not todos:
        print("No to-do items.")
        return
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {todo}")

def add_todo():
    """Add a new to-do item."""
    todo = input("Enter a new to-do item: ")
    todos.append(todo)
    save_todos(todos)
    print(f"Added: {todo}")

def remove_todo():
    """Remove a to-do item."""
    show_todos(todos)
    if not todos:
        return
    try:
        index = int(input("Enter the number of the to-do item to remove: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            save_todos(todos)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do application."""
    while True:
        print("\nTo-Do List:")
        show_todos(todos)
        print("\nOptions:")
        print("1. Add a to-do item")
        print("2. Remove a to-do item")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_todo()
        elif choice == '2':
            remove_todo()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todos = load_todos()
    main()

