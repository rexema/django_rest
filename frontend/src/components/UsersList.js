import React from 'react';
import {Link} from 'react-router-dom';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`/users/${user.id}`}>{user.first_name}</Link>
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UsersList = ({users}) => {
    return (
        <table>
            <th>
                First name
             </th>
             <th>
                Last name
             </th>
             <th>
                Email
             </th>
             {users.map((user)=> <UserItem user={user}/> )}
        </table>
    )
}

export default UsersList