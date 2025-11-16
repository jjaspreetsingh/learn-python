"""
Todo App Project
=================

A simple command-line todo list application.
"""

import json
import os

TODO_FILE = "todos.json"

def load_todos():
    """Load todos from file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    """Save todos to file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=2)

def display_todos(todos):
    """Display all todos."""
    if not todos:
        print("No todos! Add one to get started.")
        return
    
    print("\n=== Your Todos ===")
    for index, todo in enumerate(todos, 1):
        status = "✓" if todo['completed'] else " "
        print(f"{index}. [{status}] {todo['task']}")

def add_todo(todos, task):
    """Add a new todo."""
    todo = {
        'task': task,
        'completed': False
    }
    todos.append(todo)
    save_todos(todos)
    print(f"Added: {task}")

def complete_todo(todos, index):
    """Mark a todo as completed."""
    if 1 <= index <= len(todos):
        todos[index - 1]['completed'] = True
        save_todos(todos)
        print(f"Completed: {todos[index - 1]['task']}")
    else:
        print("Invalid todo number!")

def delete_todo(todos, index):
    """Delete a todo."""
    if 1 <= index <= len(todos):
        deleted_task = todos[index - 1]['task']
        todos.pop(index - 1)
        save_todos(todos)
        print(f"Deleted: {deleted_task}")
    else:
        print("Invalid todo number!")

def main():
    """Main function."""
    todos = load_todos()
    
    print("=== Todo App ===")
    print("Commands: add, list, complete, delete, quit\n")
    
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == 'quit':
            print("Goodbye!")
            break
        elif command == 'list':
            display_todos(todos)
        elif command == 'add':
            task = input("Enter task: ").strip()
            if task:
                add_todo(todos, task)
            else:
                print("Task cannot be empty!")
        elif command == 'complete':
            display_todos(todos)
            try:
                index = int(input("Enter todo number to complete: "))
                complete_todo(todos, index)
            except ValueError:
                print("Please enter a valid number!")
        elif command == 'delete':
            display_todos(todos)
            try:
                index = int(input("Enter todo number to delete: "))
                delete_todo(todos, index)
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("Unknown command! Use: add, list, complete, delete, quit")
        
        print()

if __name__ == "__main__":
    main()

