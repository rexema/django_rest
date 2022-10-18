import React from 'react';
import {Link} from 'react-router-dom';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`/users/${user.id}`}>{user.first_name}</Link>
            </td>
            <td>
                {user.username}
            </td>
            <td>
                {user.email}
            </td>
             <td>
                {user.groups}
            </td>
        </tr>
    )
}

const UsersList = ({users}) => {
    return (
        <table>
            <th>
                Username
             </th>
             <th>
                Email
             </th>
             <th>
                Groups
             </th>
             {users.map((user)=> <UserItem user={user}/> )}
        </table>
    )
}

export default UsersList