import React from 'react';
import {Link} from 'react-router-dom';

const UserItem = ({user, delete_user}) => {
    return (
        <tr>
            <td>
                <Link to={`/users/${user.id}`}>{user.username}</Link>
            </td>
            <td>
                {user.email}
            </td>
             <td><button onClick={()=>delete_user(user.id)} type='button'>Delete</button>
             </td>
        </tr>
    )
}

const UsersList = ({users, delete_user}) => {
    return (
        <table>
            <th>
                Username
             </th>
             <th>
                Email
             </th>
             <th>
                Delete
             </th>
             {users.map((user)=> <UserItem user={user} delete_user={delete_user}/> )}
        </table>
    )
}

export default UsersList