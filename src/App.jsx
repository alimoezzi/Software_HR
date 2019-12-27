import React from 'react'
import { Route, Switch } from 'react-router-dom'
import '../templates/App.css'
import Homepage from "./school/HomePage/Homepage.js"
import AdminHome from "./school/AdminHome/AdminHome.js"
import StudentHome from "./school/StudentHome/StudentHome.js"
import TeacherHome from "./school/TeacherHome/TeacherHome.js"
import "../templates/App.css"

class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        console.log("APP RENDER")

        return (
            <div>
                <Switch>
                    <Route
                        exact
                        path="/"
                        render={(routeProps) => <Homepage {...routeProps}/>}
                    />
                    <Route
                        exact
                        path="/home/students"
                        render={(routeProps) => <StudentHome {...routeProps}/>}
                    />
                    <Route
                        exact
                        path="/home/teachers"
                        render={(routeProps) => <TeacherHome {...routeProps}/>}
                    />
                    <Route
                        exact
                        path="/home/admins"
                        render={(routeProps) => <AdminHome {...routeProps}/>}
                    />
                </Switch>
            </div>
        );
    }
}


export default App;