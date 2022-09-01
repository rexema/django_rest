const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
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
                First name
             </th>
             <th>
                Last name
             </th>
             {users.map((user)=> <UserItem user={user} /> )}
        </table>
    )
}

export default UsersList