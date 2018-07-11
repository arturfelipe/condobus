import React, { Component } from 'react';
import apiClient from "./graphql";
import './App.css';


class App extends Component {
  state = { organizations: [] }

  componentDidMount() {
    const query = '{ organizations { name, logo } }'
    apiClient(query)
      .then(({ data }) => {
        const { organizations } = data;
        this.setState({ organizations })
      });
  }

  render() {
    const { organizations } = this.state;
    return (
      <div className="App">
        {organizations.map(org => {
          return (
            <div key={`organization-${org.id}`}>
              {org.name}
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;
