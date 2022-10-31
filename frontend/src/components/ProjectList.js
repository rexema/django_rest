import React from 'react';
import {Link} from 'react-router-dom';



const ProjectItem = ({project, delete_project}) => {
    return (
        <tr>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </td>
            <td>
                {project.link}
            </td>
            <td>
                {project.user}
            </td>
            <td>
                 <button onClick={()=>delete_project(project.id)}   type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, delete_project}) => {

    return (
        <div>
        <table>
            <th>
                Name
             </th>
             <th>
                Link
             </th>
             <th>
                Users
             </th>
             <th>

             </th>
             {projects.map((project_)=> <ProjectItem project={project_} delete_project={delete_project}/> )}
        </table>
        <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectList
