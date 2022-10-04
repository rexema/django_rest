import React from 'react';
import UsersList from './components/UsersList.js';
import axios from 'axios';
import NaviBar from './components/NaviBar';
import Footer from './components/Footer';
import 'bootstrap/dist/css/bootstrap.min.css';
import ProjectList from './components/ProjectList.js';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";
import NotFound404 from './components/NotFound404';
import ProjectsUsers from './components/ProjectsUsers';
import ToDoList from './components/ToDoList.js';
import ProjectsDetail from './components/ProjectsDetail'

class App extends React.Component {
    constructor(props){
           super(props)
           this.state = {
                'users':[],
                'projects':[],
                'todos':[],
           }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
         axios
            .get('http://127.0.0.1:8000/api/project/')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))
           axios
            .get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render(){
        return(
        <div>
        <NaviBar />
        <BrowserRouter>
            <nav>
                <li>
                    <Link to='/'>Users</Link>
                </li>
                <li>
                    <Link to='/projects'>Projects</Link>
                </li>
                 <li>
                    <Link to='/todos'>ToDos</Link>
                </li>
            </nav>

            <Routes>

                <Route exact path='/' element={<Navigate to='/users'/>}/>
                <Route path='/users'>
                    <Route index element ={<UsersList users={this.state.users}/>} />
                    <Route path=':userId' element ={<ProjectsUsers projects={this.state.projects}/>} />
                </Route>
                <Route path='/projects'>
                    <Route index element = {<ProjectList projects={this.state.projects}/>} />
                    <Route path = ':projectId' element = {<ProjectsDetail projects={this.state.projects}/>} />
                </Route>
                <Route exact path='/todos'element =  {<ToDoList todos={this.state.todos}/>} />
                <Route path='*' element={<NotFound404/>}/>
                <Route path = '/projects1' element={<Navigate to='/projects' />} />
            </Routes>

        </BrowserRouter>
        <Footer />
        </div>
        )
    }
}
export default App;
