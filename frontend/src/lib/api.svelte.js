const API_BASE = 'http://localhost:5000/api';

export async function fetchTodos() {
  const response = await fetch(`${API_BASE}/todos`);
  return response.json();
}

export async function createTodo(title) {
  const response = await fetch(`${API_BASE}/todos`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title })
  });
  return response.json();
}

export async function updateTodo(id, data) {
  const response = await fetch(`${API_BASE}/todos/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return response.json();
}

export async function deleteTodo(id) {
  await fetch(`${API_BASE}/todos/${id}`, {
    method: 'DELETE'
  });
}
