<script>
  import { onMount } from 'svelte';
  import TodoItem from './lib/TodoItem.svelte';
  import { fetchTodos, createTodo } from './lib/api.svelte.js';
  
  let todos = [];
  let newTodoTitle = '';
  let loading = true;
  
  async function loadTodos() {
    loading = true;
    todos = await fetchTodos();
    loading = false;
  }
  
  async function addTodo() {
    if (newTodoTitle.trim()) {
      await createTodo(newTodoTitle);
      newTodoTitle = '';
      await loadTodos();
    }
  }
  
  onMount(loadTodos);
</script>

<main>
  <h1>Svelte + Flask Todo App</h1>
  
  <div class="add-todo">
    <input 
      type="text" 
      bind:value={newTodoTitle} 
      placeholder="Enter new todo"
      on:keypress={(e) => e.key === 'Enter' && addTodo()}
    />
    <button on:click={addTodo}>Add</button>
  </div>
  
  {#if loading}
    <p>Loading...</p>
  {:else}
    <div class="todo-list">
      {#each todos as todo (todo.id)}
        <TodoItem {todo} onUpdate={loadTodos} />
      {/each}
    </div>
  {/if}
</main>

<style>
  main {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
  }
  
  h1 {
    text-align: center;
    color: #333;
  }
  
  .add-todo {
    display: flex;
    gap: 10px;
    margin: 20px 0;
  }
  
  input {
    flex: 1;
    padding: 10px;
    font-size: 16px;
  }
  
  button {
    padding: 10px 20px;
    background: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  .todo-list {
    margin-top: 20px;
  }
</style>
