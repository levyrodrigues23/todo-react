import { useState } from "react";
import "./TodoApp.css";
import Swal from "sweetalert2";



const TodoApp = () => {
  //lista de tarefas
  const [todos, setTodos] = useState([]);

  //estado de texto da tarefa
  const [inputValue, setInputValue] = useState("");

  //adicionar tarefa
  const handleSubmit = (e) => {
    e.preventDefault();

    if (inputValue.trim() !== "") {
      const newTodo = {
        id: Date.now(),
        text: inputValue,
      };

      setTodos((prevTodos) => [...prevTodos, newTodo]);

      setInputValue("");
    } else if(inputValue.trim() === "") {
      Swal.fire({
        title: 'Calma aí!',
        text: 'Você precisa digitar uma tarefa!',
        icon: 'warning',
        confirmButtonText: 'Ok'
      });
    }
  };

  const handleDelete = (id) => {
setTodos(todos.filter((todo) => todo.id !== id))
  }

  return (
    <div className="app-container">
      {/* titulo inicial */}
      <h1 className="title">lista de tarefas</h1>
      {/* form para adicionar tarefas */}
      <form onSubmit={handleSubmit} className="form-container">
        <input
          type="text"
          className="input-field"
          placeholder="adicione uma tarefa"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button type="submit" className="add-button">
          {" "}
          adicionar
        </button>
      </form>
      {/* lista de tarefas */}
      {todos.length === 0 && <p className="empty">não ha tarefas</p>}

      <ul className="todo-list">
        {todos.map((todo) => (
          <li key={todo.id} className="todo-item">{todo.text}
          <button className="delete-buttom" onClick={() => handleDelete(todo.id)}>Excluir tarefa</button>

          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoApp;
