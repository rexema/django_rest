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
import ProjectsDetail from './components/ProjectsDetail';
import LoginForm from './components/Auth'
import Cookies from 'universal-cookie'
import ProjectForm from './components/ProjectForm';




class App extends React.Component {
    constructor(props){
           super(props)
           this.state = {
                'users':[],
                'projects':[],
                'todos':[],
                'token':'',
                 'authorized_user': ''
           }
    }

    delete_user(id){

            const headers = this.get_headers()
            axios.delete(`http://127.0.0.1:8000/api/users/${id}`, {headers})
            .then(response => {
                this.load_data()
            }).catch(error =>{
            console.log(error)
            this.setState({users:[]})})
        }

    delete_project(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/project/${id}`, {headers})
            .then(response => {
                this.load_data()
            })
            .catch(error => {
                console.log(error)
                this.setState({projects: []})
            })
            console.log(id)
    }


    create_project(name, users){
        const headers = this.get_headers()
        const data = {name: name, users:users}
        axios.post(`http://127.0.0.1:8000/api/project`,data, {headers})
            .then(response => {
               this.load.data()
              }).catch(error => {
            this.setState({projects:[]})
            })
    }

    get_token(username, password){
        const data={username: username, password:password}
        axios.post('http://127.0.0.1:8000/api-token/', data).then(response=>{
            this.set_token(response.data['token'])
        }).catch(error => alert("Неверный пароль или логин"))
    }


    set_token(token){
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, ()=> this.load_data())
    }


    is_auth(){
        return this.state.token !== ''
    }


    logout(){
        this.set_token('')
        this.setState({'users':[]})
        this.setState({'projects':[]})
        this.setState({'todos':[]}, ()=> this.load_data())

    }


    get_headers(){
        let headers = {
            'Content-Type': 'application/json',


        }
        if (this.is_auth()){
            headers['Authorization'] = 'Token '+ this.state.token
        }
        return headers

    }

    get_token_from_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=> this.load_data())

    }


    load_data(){
         const headers = this.get_headers()
         axios
            .get('http://127.0.0.1:8000/api/users/',{headers})
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
            .get('http://127.0.0.1:8000/api/project/', {headers})
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
            .get('http://127.0.0.1:8000/api/todo/', {headers})
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



    componentDidMount() {
       this.get_token_from_storage()}

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
                <li>
                    {this.is_auth() ? <button onClick={()=> this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                </li>
            </nav>

            <Routes>

                <Route exact path='/' element={<Navigate to='/users'/>}/>
               <Route exact path='/users' element = {<UsersList users={this.state.users} delete_user={(id)=>this.delete_user(id)}/>} />
               <Route exact path='/projects' element =  {<ProjectList projects={this.state.projects} delete_project={(id)=>this.delete_project(id)}/>} />
                <Route path='/users'>
                    <Route index element ={<UsersList users={this.state.users}/>} />
                    <Route path=':userId' element ={<ProjectsUsers projects={this.state.projects}/>} />
                </Route>
//                <Route path='/projects'>
//                    <Route index element = {<ProjectList projects={this.state.projects} delete_project={(id)=>this.delete_project(id)}/>} />
//                    <Route path = ':projectId' element = {<ProjectsDetail projects={this.state.projects}/>} />
//                     <Route path='/projects/create' element={<ProjectForm users={this.state.users}
                                             create_project={(title, link, users) => this.create_project(title, link, users)}
                                />}
                            />
                </Route>

                 <Route exact path='/todos'element =  {<ToDoList todos={this.state.todos}/>} />
                 <Route path='*' element={<NotFound404/>}/>
                <Route path = '/projects1' element={<Navigate to='/projects' />} />
                 <Route exact path='/login' element =  {<LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>
                 </Routes>

        </BrowserRouter>
        <Footer />
        </div>

            )}
}

export default App