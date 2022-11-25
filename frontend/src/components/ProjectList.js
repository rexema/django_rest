import React, { useState } from 'react';
import {Link} from 'react-router-dom';
import Table from "react-bootstrap/Table";
import { Button } from "react-bootstrap";
import { Navbar, Nav, Container } from 'react-bootstrap';


const ProjectItem = ({project,all_users, delete_project}) => {

    return (
        <tr>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </td>
             <td>
                {project.link}
            </td>
            <td>
                {project.users.map((user_id)=>{
                let user =all_users.find(user => user.id===user_id)
                return user.username + ' '
                })}
            </td>
            <td>
                 <Button onClick={()=>delete_project(project.id)}  variant="outline-danger" type='button'>Delete</Button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects,users, delete_project}) => {
    const [value, setValue] = useState('')
    const filteredProjects = projects.filter(project => {
        return project.name.toLowerCase().includes(value.toLowerCase())
    })

    return (
        <div>
            <div className="form">
                <form className="search__form">
                    <input
                        type="text"
                        placeholder = "Search in projects..."
                        className = "search__input"
                        onChange = {(event) => setValue(event.target.value)}
                        />
                </form>
            </div>

      <Table striped bordered hover>
                <thead>
                <tr>
            <th>Name</th>
            <th>Link</th>
            <th>Users</th>
            <th></th>
            </tr>
             </thead>
             <tbody>
             {filteredProjects.map((project_)=> <ProjectItem project={project_} all_users={users} delete_project={delete_project}/> )}
             </tbody>
        </Table>
        <Link to='/projects/create'>Create</Link>

        </div>
    )
}

export default ProjectList
