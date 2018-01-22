import React, { Component } from 'react';
import logo from './bus-icon.svg';
import './App.css';

class App extends Component {

  componentDidMount() {
    var csrftoken;
    var cookies = ('; ' + document.cookie).split('; csrftoken=');
    if (cookies.length == 2)
      csrftoken = cookies.pop().split(';').shift();

    fetch('/graphql/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify({ query: '{ timeSheets { version } }' }),
      credentials: 'include'
    })
      .then(resp => resp.text())
      .then(body => {
        console.log(JSON.parse(body))
      })
  }

  render() {
    return (
      <div className="cb-app">
        <header className="cb-app-header">
          <div className="cb-app-header__brand">
            {/* <img src={logo} className="cb-app-logo" alt="logo" /> */}
            <h1 className="cb-app-name">condobus</h1>
          </div>
        </header>
        <main className="cb-app-main">
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World

          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World

          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
          Hello World Hello World Hello World Hello WorldHello World Hello World Hello World Hello World
        </main>
        <footer className="cb-app-footer">
          Hi
        </footer>
      </div>
    );
  }
}

export default App;
