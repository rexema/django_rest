import React from 'react';
import {ReactComponent as ReactLogo} from './logo.svg';
import UsersList from './components/UsersList.js';
import axios from 'axios';
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
import ToDoForm from './components/ToDoForm';
import {Container, Nav, Navbar} from "react-bootstrap";


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
        }
    delete_todo(id){
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers})
            .then(response => {
               this.load.data()
              }).catch(error => {
            this.setState({todos:[]})
            })
    }
    create_todo(text, user, project){
        const headers = this.get_headers()
        const data = {text: text, user: user, project: project}
        axios.post(`http://127.0.0.1:8000/api/todo/`, data, {headers})
             .then(response => {
               this.load.data()
              }).catch(error => {
            this.setState({todos:[]})
            })
    }



    create_project(name, link, users){
        const headers = this.get_headers()
        const data = {name: name, link: link,users: users}
        axios.post(`http://127.0.0.1:8000/api/project/`,data, {headers})
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
          <Container className="p-2">

                    <BrowserRouter>
                        <Navbar bg="dark" variant="dark">
                            <Container>
                                <ReactLogo width="30" height="30"/>
                                <Nav className="me-auto">
                                    <Nav.Link as={Link} to='/'>Users</Nav.Link>
                                    <Nav.Link as={Link} to="/projects">Projects</Nav.Link>
                                    <Nav.Link as={Link} to="/todos">Todo</Nav.Link>

                                    {this.is_auth() ?
                                        <Nav.Link onClick={() => this.logout()}>Exit</Nav.Link> :
                                        <Nav.Link as={Link} to="/login">Enter</Nav.Link>}
                                </Nav>
                            </Container>
                        </Navbar>

            <Routes>

                <Route exact path='/' element={<Navigate to='/users'/>}/>
                <Route path='/users'>
                    <Route index element ={<UsersList users={this.state.users} />} />
                    <Route path=':userId' element ={<ProjectsUsers projects={this.state.projects}/>} />

                </Route>
                <Route exact path='/projects'>
                    <Route index element = {<ProjectList projects={this.state.projects} users={this.state.users} delete_project={(id)=>this.delete_project(id)}/>} />
                    <Route path = ':projectId' element = {<ProjectsDetail projects={this.state.projects}/>} />
                   <Route path='/projects/create' element={
                                <ProjectForm users={this.state.users}
                                             create_project={(name, link, users) => this.create_project(name, link, users)}
                                />}
                            />

                </Route>

                <Route exact path='/todos' element={
                            <ToDoList todos={this.state.todos} delete_todo={(id) => this.delete_todo(id)}
                            />}
                        />
                        <Route exact path='/todos/create' element={
                            <ToDoForm projects={(this.state.projects)} users={this.state.users} create_todo={(text, user, project) => this.create_todo(text, user, project)}
                            />}
                        />

                 <Route path='*' element={<NotFound404/>}/>
                <Route path = '/projects1' element={<Navigate to='/projects' />} />
                 <Route exact path='/login' element =  {<LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>
                 </Routes>
               <Footer />
        </BrowserRouter>

        </Container>


            )}
}

export default App