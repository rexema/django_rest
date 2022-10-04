import React from 'react';
import {Link} from 'react-router-dom';



const ProjectItem = ({project}) => {
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
        </tr>
    )
}

const ProjectList = ({projects}) => {

    return (
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
             {projects.map((project_)=> <ProjectItem project={project_}/> )}
        </table>
    )
}

export default ProjectList
