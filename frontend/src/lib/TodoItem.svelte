<script>
  import { updateTodo, deleteTodo } from './api.svelte.js';
  
  export let todo;
  export let onUpdate;
  
  async function toggleComplete() {
    await updateTodo(todo.id, { completed: !todo.completed });
    onUpdate();
  }
  
  async function handleDelete() {
    await deleteTodo(todo.id);
    onUpdate();
  }
</script>

<div class="todo-item">
  <input 
    type="checkbox" 
    checked={todo.completed} 
    on:change={toggleComplete}
  />
  <span class:completed={todo.completed}>{todo.title}</span>
  <button on:click={handleDelete}>Delete</button>
</div>

<style>
  .todo-item {
    display: flex;
    gap: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    margin: 5px 0;
    align-items: center;
  }
  
  .completed {
    text-decoration: line-through;
    color: #888;
  }
  
  button {
    margin-left: auto;
    padding: 5px 10px;
    background: #ff4444;
    color: white;
    border: none;
    cursor: pointer;
  }
</style>
