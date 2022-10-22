import React from 'react';
import {useParams} from 'react-router-dom';

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
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

const ProjectsUsers = ({projects}) => {
    let {userId}= useParams()
    console.log(userId)
    let filter_projects = projects.filter((project)=> project.user.includes(parseInt(userId)))
    console.log(filter_projects)
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
             {filter_projects.map((project_)=> <ProjectItem project={project_}/> )}
        </table>
    )
}

export default ProjectsUsers