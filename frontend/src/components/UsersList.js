import React, { useState } from 'react';
import {Link} from 'react-router-dom';
import Table from "react-bootstrap/Table";


const UserItem = ({user, delete_user}) => {
    return (

        <tr>
            <td>
                <Link to={`/users/${user.id}`}>{user.username}</Link>
            </td>
            <td>
                {user.email}
            </td>

        </tr>
    )
}

const UsersList = ({users}) => {
    const [value, setValue ] = useState('')
    const filteredUsers = users.filter(user => {
        return user.username.toLowerCase().includes(value.toLowerCase())
    })
    return (
        <div>
             <div className="form">
                <form className="search__form">
                    <input
                        type="text"
                        placeholder = "Search in users..."
                        className = "search__input"
                        onChange = {(event) => setValue(event.target.value)}
                        />
                </form>
            </div>
        <Table striped bordered hover>
            <th>
                Username
             </th>
             <th>
                Email
             </th>
            <tbody>
             {filteredUsers.map((user)=> <UserItem user={user}/> )}
            </tbody>
        </Table>

    </div>
    )
}

export default UsersList