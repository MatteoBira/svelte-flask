todos = [
    {"id": 1, "title": "Learn Svelte", "completed": False},
    {"id": 2, "title": "Learn Flask", "completed": False},
]

def get_all_todos():
    return todos

def get_todo(todo_id):
    return next((t for t in todos if t["id"] == todo_id), None)

def add_todo(title):
    new_id = max([t["id"] for t in todos]) + 1 if todos else 1
    new_todo = {"id": new_id, "title": title, "completed": False}
    todos.append(new_todo)
    return new_todo

def update_todo(todo_id, data):
    todo = get_todo(todo_id)
    if todo:
        todo.update(data)
    return todo

def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return True
