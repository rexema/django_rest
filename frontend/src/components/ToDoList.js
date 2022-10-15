import React from 'react';
import {Link} from 'react-router-dom';

const ToDoItem = ({todo}) => {
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
        </tr>
    )
}

const ToDoList = ({todos}) => {
    return (
        <table>
            <th>
                Text
             </th>

             <th>
                User
             </th>
             <th>
                Project
             </th>
             {todos.map((todo_)=> <ToDoItem todo={todo_}/> )}
        </table>
    )
}


export default ToDoList