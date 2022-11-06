import React from 'react';
import {Link} from 'react-router-dom';
import Table from "react-bootstrap/Table";


const ToDoItem = ({todo,  delete_todo}) => {
    return (
        <tr>
            <td>
                {todo.text}
            </td>
             <td>
              {todo.user}
            </td>
            <td>
               {todo.project}
            </td>
             <td>{todo.is_deleted === true ? 'deleted' : 'not deleted'}</td>
            <td>
                 <button onClick={()=>delete_todo(todo.id)}   type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ToDoList = ({todos,  delete_todo}) => {

    return (
        <div>
      <Table striped bordered hover>
                <thead>
                <tr>
            <th>Text</th>
            <th>User</th>
            <th>Project</th>
            <th>Status</th>
            <th></th>
            </tr>
             </thead>
             <tbody>
             {todos.map((todo_, index)=> <ToDoItem  key={index} todo={todo_}  delete_todo={delete_todo}/> )}
             </tbody>
        </Table>
        <Link to='/todos/create'>Create</Link>
        </div>
    )
}

export default ToDoList


